import sqlite3
from pystock_xingAPI import Xing, DBUtil
import logging
import logging.handlers
import pandas as pd
import datetime as dt

from . import utils

#Todo class로/ func or method에 xing instance 연결

class KFX_sql:
    def __init__(self, xing_inst, xingDB_dir):
        self.xing = xing_inst
        self.db_folder_dir = xingDB_dir
        self.cal = utils.kfx_calendar()
        self.fst_mon = self.cal.fst_monday()
        self.now_date = int(dt.datetime.now().strftime("%Y%m%d"))

    def get_kfx_codes(self, is_option=False):

        if is_option:
            inblock_query_t9944 = {
                't9944InBlock': {
                    'dummy': 0
                }
            }

            read_options_master = self.xing.query('xing.t9944', inblock_query_t9944)
            koptions_codes_df = pd.DataFrame(read_options_master['t9944OutBlock'])

            #codes_df = pd.concat([kfx_codes_df, koptions_codes_df])
            codes_df = koptions_codes_df

        else:
            inblock_query_t9943 = {
                't9943InBlock': {
                    'gubun': 1
                }
            }

            read_kfx_master = self.xing.query('xing.t9943', inblock_query_t9943)
            kfx_codes_df = pd.DataFrame(read_kfx_master['t9943OutBlock'])

            codes_df = kfx_codes_df

        return codes_df

    def KFX_min_sql(self, target_minute=30, codes_df=None, sdate=None, is_option=False):

        if codes_df is None :
            codes_df = self.get_kfx_codes(is_option)
            codes_df = codes_df.shcode

        if is_option==False:
            conn = sqlite3.connect("{0}//KFX_{1}min_db.db".format(self.db_folder_dir,target_minute))
        else:
            conn = sqlite3.connect("{0}//KFXo_{1}min_db.db".format(self.db_folder_dir,target_minute))

        if sdate is None:
            sdate = self.fst_mon


        for row in codes_df:

            FXcode = row

            table_name = 'D_{0}min_{1}_TB'.format(target_minute,FXcode)
            if conn.cursor().execute("select count(*) from sqlite_master where type='table' and name='{0}'".format(table_name)).fetchone()[0]:
                tb_exist=1
            else:
                tb_exist=0

            if not tb_exist:
                DBUtil.create_table_for_outblock(conn.cursor(), table_name, 't8415', 't8415OutBlock1')

                #테이블 포맷은 t8415 trcode의 t8415OutBlock1를 저장할 수 있는 형태로
                #테이블 생성뒤에 commit()으로 실제 db에 적용

                conn.commit()

                last_date = 0
                first_date = sdate

                print("New Table with" , first_date, last_date)

            else :
                try:
                    dates=conn.cursor().execute("select date from {0} order by date asc".format(table_name)).fetchall()
                    last_date=int(dates[-1][0])
                    first_date=int(dates[0][0])
                except:
                    last_date=0
                    first_date=sdate
                try:
                    last_time=int(conn.cursor().execute("select time from {0} order by time asc".format(table_name)).fetchall()[-1][0])
                except:
                    last_time=0
                try:
                    data_len=len(conn.cursor().execute("select date from {0}".format(table_name)).fetchall())
                except:
                    data_len=0

                print("From Existing TB", first_date, last_date,last_time,data_len)

            #2-2. Table에 데이터 삽입

            inblock_query_t8415 = {
                't8415InBlock': {
                    # 단축코드
                    'shcode': FXcode,
                    # 단위(n분)
                    'ncnt': target_minute,
                    # 요청건수(최대-압축:2000비압축:500)
                    'qrycnt': 2000,
                    # 조회영업일수(0:미사용1>=사용)
                    'nday': 0,
                    # 시작일자
                    'sdate': max(last_date-1,0),
                    # 시작시간(현재미사용)
                    'stime': None,
                    # 종료일자
                    'edate': 99999999,
                    # 종료시간(현재미사용)
                    'etime': None,
                    # 연속일자
                    'cts_date': None,
                    # 연속시간
                    'cts_time': None,
                    # 압축여부(Y:압축N:비압축)
                    'comp_yn': "Y"
                },

            # 나중에 연속질의 즉, 두번째 이후의 질의에서는 이 값을 True로
            'continue_query':False
            }

            if last_date < self.now_date-1:
                print(table_name)
                while True: #연속질의 루프
                    #데이터 요청
                    data = self.xing.query('xing.t8415', inblock_query_t8415)

                    if  data['t8415OutBlock']['rec_count']!='' :
                        #try:
                        if int(data['t8415OutBlock']['rec_count'])>0:
                            DBUtil.insert_for_outblock(conn.cursor(), table_name, data['t8415OutBlock1'], place_flag = False)

                            if data['t8415OutBlock']['cts_date'] !='' :
                                if ((int(data['t8415OutBlock']['cts_date'])<(last_date-1 )) or (int(data['t8415OutBlock']['cts_date'])<(first_date-1 )) ):
                                    # cts_date 값이 비어있거나 or target date 밖에 있음
                                    # 더이상 연속질의할 내용이 없단 뜻입니다. 즉 commit하고 루프에서 빠져나감감
                                    conn.commit()
                                    print("CTS End")
                                    break
                            else:
                                conn.commit()
                                print("CTS End")
                                break

                            #여기까지 왔단말은 최소 1번 질의는 했단것이고 다음 질의를 위해 연속질의를 활성화
                            inblock_query_t8415['continue_query'] = True
                            #연속질의를 위해서는 서버에 내가 어떤데이터를 받을차례라는 것을 알려야하는데 그것이 cts_date
                            # cts_XXXX 가 있으면 대부분 연속질의를 위한것 이라 보면됩니다.
                            # cts_XXXX 형태가 아닌 경우가 있으므로 새로운 tr code룰 사용할때는 DevCenter를 확인

                            inblock_query_t8415['t8415InBlock']['cts_date'] = data['t8415OutBlock']['cts_date']
                            inblock_query_t8415['t8415InBlock']['cts_time'] = data['t8415OutBlock']['cts_time']


                        else:
                            print("No read count")
                            conn.commit()
                            break

                        #except Exception as e :
                        #    print(e)
                        #    print(data['t8415OutBlock']['rec_count'])
                        #    conn.commit()
                        #    break

                    #다시 루프를 처음부터
                    else:
                        print("No read count")
                        conn.commit()
                        break
            else :
                print("Data is newest: {0}".format(table_name))
        conn.commit()
        conn.close()

    def KFX_tick_sql(self, target_tick=5,  codes_df=None, sdate=None,is_option=False):

        if codes_df is None :
            codes_df = self.get_kfx_codes(is_option)
            codes_df = codes_df.shcode

        if is_option == False:
            conn = sqlite3.connect("{0}//KFX_{1}tick_db.db".format(self.db_folder_dir, target_tick))
        else:
            conn = sqlite3.connect("{0}//KFXo_{1}tick_db.db".format(self.db_folder_dir, target_tick))
        #conn = sqlite3.connect("xing//KFX_{0}tick_db.db".format(target_tick))

        if sdate is None:
            sdate = self.fst_mon

        for row in codes_df:

            FXcode = row

            table_name = 'D_{0}tick_{1}_TB'.format(target_tick,FXcode)
            if conn.cursor().execute("select count(*) from sqlite_master where type='table' and name='{0}'".format(table_name)).fetchone()[0]:
                tb_exist=1
            else:
                tb_exist=0

            if not tb_exist:
                DBUtil.create_table_for_outblock(conn.cursor(), table_name, 't8414', 't8414OutBlock1')
                conn.commit()

                last_date = sdate

                print("New Table starting from :",  last_date)

            else :
                try:
                    dates=conn.cursor().execute("select date from {0} order by date asc".format(table_name)).fetchall()
                    last_date=int(dates[-1][0])
                    first_date=int(dates[0][0])
                except:
                    last_date=0
                    first_date=sdate
                try:
                    last_time=int(conn.cursor().execute("select time from {0} order by time asc".format(table_name)).fetchall()[-1][0])
                except:
                    last_time=0
                try:
                    data_len=len(conn.cursor().execute("select date from {0}".format(table_name)).fetchall())
                except:
                    data_len=0

                print("From Existing TB", first_date, last_date, last_time, data_len)

            #2-2. Table에 데이터 삽입
            inblock_query_t8414 = {
                't8414InBlock': {
                    # 단축코드
                    'shcode': FXcode,
                    # 단위(n틱)
                    'ncnt': target_tick,
                    # 요청건수(최대-압축:2000비압축:500)
                    'qrycnt': 2000,
                    # 조회영업일수(0:미사용1>=사용)
                    'nday': 0,
                    # 시작일자
                    'sdate': max(last_date-1,0),
                    # 시작시간(현재미사용)
                    'stime': None,
                    # 종료일자
                    'edate': 99999999,
                    # 종료시간(현재미사용)
                    'etime': None,
                    # 연속일자
                    'cts_date': None,
                    # 연속시간
                    'cts_time': None,
                    # 압축여부(Y:압축N:비압축)
                    'comp_yn': 'Y'
                },

            'continue_query':False
            }

            if last_date < self.now_date-1:
                print(table_name)
                while True: #연속질의 루프
                    #데이터 요청
                    data = self.xing.query('xing.t8414', inblock_query_t8414)

                    if  data['t8414OutBlock']['rec_count']!='' :
                        #try:
                        if int(data['t8414OutBlock']['rec_count'])>0:
                            DBUtil.insert_for_outblock(conn.cursor(), table_name, data['t8414OutBlock1'], place_flag = False)

                            if data['t8414OutBlock']['cts_date'] !='' :
                                if ((int(data['t8414OutBlock']['cts_date'])<(last_date-1 )) or (int(data['t8414OutBlock']['cts_date'])<(first_date-1 )) ):
                                    # cts_date 값이 비어있거나 or target date 밖에 있음
                                    # 더이상 연속질의할 내용이 없단 뜻입니다. 즉 commit하고 루프에서 빠져나감감
                                    conn.commit()
                                    print("CTS End")
                                    break
                            else:
                                conn.commit()
                                print("CTS End")
                                break

                            inblock_query_t8414['continue_query'] = True

                            inblock_query_t8414['t8414InBlock']['cts_date'] = data['t8414OutBlock']['cts_date']
                            inblock_query_t8414['t8414InBlock']['cts_time'] = data['t8414OutBlock']['cts_time']


                        else:
                            print("No read count")
                            conn.commit()
                            break
                        #except Exception as e :
                        #    print(e)
                        #    print(data['t8415OutBlock']['rec_count'])
                        #    conn.commit()
                        #    break


                    else:
                        print("No read count")
                        conn.commit()
                        break
            else :
                print("Data is newest: {0}".format(table_name))
        conn.commit()
        conn.close()

    def KFX_daily_sql(self, codes_df=None, sdate=None, is_option=False):

        if codes_df is None :
            codes_df = self.get_kfx_codes(is_option)
            codes_df = codes_df.shcode

        if is_option == False:
            conn = sqlite3.connect("xingDB//KFX_1Day_db.db")
        else:
            conn = sqlite3.connect("xingDB//KFXo_1Day_db.db")

        if sdate is None:
            sdate = self.fst_mon

        for row in codes_df:
            FXcode = row

            table_name = 'D_1Day_{0}_TB'.format(FXcode)
            if conn.cursor().execute("select count(*) from sqlite_master where type='table' and name='{0}'".format(table_name)).fetchone()[0]:
                tb_exist=1
            else:
                tb_exist=0

            if not tb_exist:
                DBUtil.create_table_for_outblock(conn.cursor(), table_name, 't8416', 't8416OutBlock1')

                conn.commit()

                last_date = sdate

                print("New Table starting from :", last_date)

            else :
                try:
                    dates=conn.cursor().execute("select date from {0} order by date asc".format(table_name)).fetchall()
                    last_date=int(dates[-1][0])
                    first_date=int(dates[0][0])
                except:
                    last_date=0
                    first_date=sdate
                try:
                    data_len=len(conn.cursor().execute("select date from {0}".format(table_name)).fetchall())
                except:
                    data_len=0

                print("From Existing TB", first_date, last_date,data_len)

            #2-2. Table에 데이터 삽입

            # 선물/옵션챠트(일주월)(t8416)
            inblock_query_t8416 = {
                't8416InBlock': {
                    # 단축코드
                    'shcode': FXcode,
                    # 주기구분(2:일3:주4:월)
                    'gubun': 2,
                    # 요청건수(최대-압축:2000비압축:500)
                    'qrycnt': 2000,
                    # 시작일자
                    'sdate': max(last_date-1,0),
                    # 종료일자
                    'edate': 99999999,
                    # 연속일자
                    'cts_date': None,
                    # 압축여부(Y:압축N:비압축)
                    'comp_yn': 'Y'
                },


            'continue_query':False
            }

            if last_date < self.now_date-1:
                print(table_name)
                while True: #연속질의 루프
                    #데이터 요청
                    data = self.xing.query('xing.t8416', inblock_query_t8416)

                    if  data['t8416OutBlock']['rec_count']!='' :
                        #try:
                        if int(data['t8416OutBlock']['rec_count'])>0:
                            DBUtil.insert_for_outblock(conn.cursor(), table_name, data['t8416OutBlock1'], place_flag = False)

                            if data['t8416OutBlock']['cts_date'] !='' :
                                if ((int(data['t8416OutBlock']['cts_date'])<(last_date-1 )) or (int(data['t8416OutBlock']['cts_date'])<(first_date-1 )) ):
                                    # cts_date 값이 비어있거나 or target date 밖에 있음
                                    # 더이상 연속질의할 내용이 없다 commit하고 루프에서 빠져나감
                                    conn.commit()
                                    print("CTS End")
                                    break
                            else:
                                conn.commit()
                                print("CTS End")
                                break

                            inblock_query_t8416['continue_query'] = True


                            inblock_query_t8416['t8416InBlock']['cts_date'] = data['t8416OutBlock']['cts_date']

                        else:
                            print("No read count")
                            conn.commit()
                            break
                        #except Exception as e :
                        #    print(e)
                        #    print(data['t8415OutBlock']['rec_count'])
                        #    conn.commit()
                        #    break

                    else:
                        print("No read count")
                        conn.commit()
                        break
            else :
                print("Data is newest: {0}".format(table_name))
        conn.commit()
        conn.close()

    def set_dt_index(self, dataframe):
        if 'time' in dataframe.columns:
            #pd.to_datetime(dataframe.date+dataframe.time, format='%Y%m%d%H%M%S')
            dataframe['dt']=pd.to_datetime(dataframe.date+dataframe.time, format='%Y%m%d%H%M%S')
            dataframe.set_index(dataframe['dt'],inplace=True)
            dataframe.drop(['date','time','dt'],axis=1,inplace=True)
            dataframe.sort_index(inplace=True)
        else:
            #pd.to_datetime(dataframe.date, format='%Y%m%d')
            dataframe['dt']=pd.to_datetime(dataframe.date, format='%Y%m%d')
            dataframe.set_index(dataframe['dt'],inplace=True)
            dataframe.drop(['date','dt'],axis=1,inplace=True)
            dataframe.sort_index(inplace=True)

        return dataframe


    #Todo call by minmum info, use utils  + @

    def read_sql_df(self, con_name,table_name):
        con=sqlite3.connect("{0}".format(con_name))
        df_tmp=pd.read_sql("SELECT * FROM {0}".format(table_name),con)
        df_tmp=df_tmp[~df_tmp.duplicated(keep='last')]
        df_tmp=self.set_dt_index(df_tmp)
        return df_tmp













