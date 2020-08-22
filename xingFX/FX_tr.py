import sqlite3
from pystock_xingAPI import Xing, DBUtil
import logging
import logging.handlers
import pandas as pd

from dateutil.relativedelta import relativedelta, FR, TH ,MO
import datetime as dt
import calendar

class FX_tr:

    def __init__(self,xing_inst):
        self.xing=xing_inst


    def set_dt_index(self, dataframe):
        if 'time' in dataframe.columns:
            #pd.to_datetime(dataframe.date + dataframe.time, format='%Y%m%d%H%M%S')
            dataframe['dt'] = pd.to_datetime(dataframe.date + dataframe.time, format='%Y%m%d%H%M%S')
            dataframe.set_index(dataframe['dt'], inplace=True)
            dataframe.drop(['date', 'time', 'dt'], axis=1, inplace=True)
            dataframe.sort_index(inplace=True)
        else:
            #pd.to_datetime(dataframe.date, format='%Y%m%d')
            dataframe['dt'] = pd.to_datetime(dataframe.date, format='%Y%m%d')
            dataframe.set_index(dataframe['dt'], inplace=True)
            dataframe.drop(['date', 'dt'], axis=1, inplace=True)
            dataframe.sort_index(inplace=True)

        return dataframe

    #TODO tr추가 대상?
    """
    
    """
    def get_stock_codes(self, gubun=1):
        # 주식종목조회(t8430)
        inblock_query_t8430 = {
            't8430InBlock': {
                # 구분(0:전체1:코스피2:코스닥)
                'gubun': gubun
            }
        }


        read_stocks_master = self.xing.query('xing.t8430', inblock_query_t8430)
        stocks_codes_df = pd.DataFrame(read_stocks_master['t8430OutBlock'])

        # codes_df = pd.concat([kfx_codes_df, koptions_codes_df])
        codes_df = stocks_codes_df

        return codes_df

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

    def get_ffx_codes(self,gubun=0):

        inblock_query_o3101 = {
            'o3101InBlock': {

                'gubun': gubun
            }
        }

        ffx_master = self.xing.query('xing.o3101', inblock_query_o3101)
        ffx_codes_df = pd.DataFrame(ffx_master['o3101OutBlock'])

        codes_df = ffx_codes_df

        return codes_df


    def KFX_min(self,code, target_minute=30,  sdate=None):
        #minute data
        if sdate is None:
            first_date=0
        else:
            first_date=sdate

        FXcode=code
        # 선물/옵션챠트(N분)(t8415)
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
                'sdate': first_date,
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
        data_list=[]

        while True: #연속질의 루프
            #데이터 요청
            data = self.xing.query('xing.t8415', inblock_query_t8415)

            if  data['t8415OutBlock']['rec_count']!='' :

                if int(data['t8415OutBlock']['rec_count'])>0:
                    data_list.append(pd.DataFrame(data['t8415OutBlock1']))

                    if data['t8415OutBlock']['cts_date'] =='' :

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

                    break

            #다시 루프를 처음부터
            else:
                print("No read count")
                break
        data_df=pd.concat(data_list)
        data_df=self.set_dt_index(data_df)
        data_df = data_df.apply(pd.to_numeric, errors='ignore')
        return data_df

    def KFX_tick(self, code, target_tick=5,  sdate=None):
        #tick data
        if sdate is None:
            first_date=0
        else:
            first_date=sdate

        FXcode = code

        # 선물옵션차트(틱/n틱)(t8414)
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
                'sdate': first_date,
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

        data_list=[]
        while True: #연속질의 루프
            #데이터 요청
            data = self.xing.query('xing.t8414', inblock_query_t8414)

            if  data['t8414OutBlock']['rec_count']!='' :
                data_list.append(pd.DataFrame(data['t8414OutBlock1']))
                if int(data['t8414OutBlock']['rec_count'])>0:
                    if data['t8414OutBlock']['cts_date'] =='' :

                        print("CTS End")
                        break

                    inblock_query_t8414['continue_query'] = True

                    inblock_query_t8414['t8414InBlock']['cts_date'] = data['t8414OutBlock']['cts_date']
                    inblock_query_t8414['t8414InBlock']['cts_time'] = data['t8414OutBlock']['cts_time']

                else:
                    print("No read count")
                    break

            else:
                print("No read count")
                break

        data_df=pd.concat(data_list)
        data_df=self.set_dt_index(data_df)
        data_df = data_df.apply(pd.to_numeric, errors='ignore')
        return data_df

    def KFX_daily(self, code, sdate=None):
        #daily ohlc data
        if sdate is None:
            first_date=0
        else:
            first_date=sdate

        FXcode = code

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
                'sdate': first_date,
                # 종료일자
                'edate': 99999999,
                # 연속일자
                'cts_date': None,
                # 압축여부(Y:압축N:비압축)
                'comp_yn': 'Y'
            },
        'continue_query':False
        }

        data_list=[]
        while True: #연속질의 루프
            #데이터 요청
            data = self.xing.query('xing.t8416', inblock_query_t8416)

            if  data['t8416OutBlock']['rec_count']!='' :

                if int(data['t8416OutBlock']['rec_count'])>0:
                    data_list.append(pd.DataFrame(data['t8416OutBlock1']))

                    if data['t8416OutBlock']['cts_date'] =='' :
                        print("CTS End")
                        break

                    inblock_query_t8416['continue_query'] = True
                    inblock_query_t8416['t8416InBlock']['cts_date'] = data['t8416OutBlock']['cts_date']

                else:
                    print("No read count")
                    break

            else:
                print("No read count")
                break

        data_df=pd.concat(data_list)
        data_df=self.et_dt_index(data_df)
        data_df = data_df.apply(pd.to_numeric, errors='ignore')
        return data_df


    def KFX_con_daily(self, code,target_sdate=None):
        #연속월물 일간
        inblock_query_t2203 = {
            't2203InBlock': {
                # 단축코드
                'shcode': code,
                # 선물최근월물
                'futcheck': 1,
                # 날짜
                'date': None,
                # CTS종목코드
                'cts_code': None,
                # 전종목만기일
                'lastdate': None,
                # 조회요청건수
                'cnt': 500
            },
            'continue_query': False
        }
        data_list=[]
        while True: #연속질의 루프
            #데이터 요청
            data = self.xing.query('xing.t2203', inblock_query_t2203)

            if  len(data['t2203OutBlock1'])>0 :

                data_list.append(pd.DataFrame(data['t2203OutBlock1']))

                if (data['t2203OutBlock']['lastdate'] =='' ) or (len(data['t2203OutBlock1'])<500):
                    print("CTS End")
                    break
                if target_sdate:
                    if int(data['t2203OutBlock1'][-1]['date'])<=target_sdate:
                        print('Reached Target Sdate')
                        break

                inblock_query_t2203['continue_query'] = True
                inblock_query_t2203['t2203InBlock']['date'] = data['t2203OutBlock']['date']
                inblock_query_t2203['t2203InBlock']['cts_code'] = data['t2203OutBlock']['cts_code']
                inblock_query_t2203['t2203InBlock']['lastdate'] = data['t2203OutBlock']['lastdate']

            else:
                print("No read count")
                break

        data_df=pd.concat(data_list)
        data_df=self.set_dt_index(data_df)
        data_df = data_df.apply(pd.to_numeric, errors='ignore')
        return data_df

    def get_askbid(self, code,is_df=True):
        # 선물/옵션현재가호가조회(t2105)
        inblock_query_t2105 = {
            't2105InBlock': {
                # 단축코드
                'shcode': code
            }
        }

        data = self.xing.query('xing.t2105', inblock_query_t2105)
        res=data['t2105OutBlock']
        if is_df:
            hoga_df= pd.DataFrame([res])
            #hoga_df=hoga_df.convert_objects(convert_numeric=True)
            hoga_df=hoga_df.apply(pd.to_numeric,errors='ignore')
            return hoga_df
        else:
            return res

    def option_board(self,date=None):
        #TODO 만기일 전부 구하기, None 경우 최근월 만기일 input으로
        if date is None :
            date=99999999

        # 옵션전광판(t2301)
        inblock_query_t2301 = {
            't2301InBlock': {
                # 월물
                'yyyymm': date,
                'gubun' : 'G"'
            }
        }

        data = self.xing.query('xing.t2301', inblock_query_t2301)
        fx=data['t2301OutBlock']
        calls=data['t2301OutBlock1']
        puts=data['t2301OutBlock2']
        call_df=pd.DataFrame(calls).set_index('actprice',drop=False)
        put_df=pd.DataFrame(puts).set_index('actprice',drop=False)
        return fx, call_df, put_df

    #TODO 시간체결 조회시 작동 x, devcenter는 작동
    def che_record_bytime(self, code, cvolume=None, stime=None, etime=None ):
        # 선물옵션시간대별체결조회(t2201)
        inblock_query_t2201 = {
            't2201InBlock': {
                # 단축코드
                'focode': code,
                # 특이거래량
                'cvolume': None,
                # 시작시간
                'stime': '09000000',
                # 종료시간
                'etime': '15460000',
                # 시간CTS
                'cts_time': None
            },
        'continue_query': False
        }

        data = self.xing.query('xing.t2201', inblock_query_t2201)

    def che_by_tickmin(code,cgubun="B",bgubun=0,cnt=200):
        # 선물옵션틱분별체결조회챠트(t2209)
        inblock_query_t2209 = {
            't2209InBlock' : {
                # 단축코드
                'focode' : code,
                # 챠트구분
                'cgubun' : cgubun,
                # 분구분
                'bgubun' : bgubun,
                # 조회건수
                'cnt' : cnt
            }
        }

        data = self.xing.query('xing.t2209', inblock_query_t2209)
        res=data['t2209OutBlock1']
        data_df=pd.DataFrame(res)
        data_df = data_df.apply(pd.to_numeric, errors='ignore')

        return data_df

    def c_price(self, code, is_df=True):
        # 선물/옵션현재가(시세)조회(t2101)
        inblock_query_t2101 = {
            't2101InBlock': {
                # 단축코드
                'focode': code
            }
        }

        data = self.xing.query('xing.t2101', inblock_query_t2101)
        res=data['t2101OutBlock']
        if is_df:
            data_df=pd.DataFrame([res])
            data_df=data_df.apply(pd.to_numeric, errors='ignore')
            return data_df
        else:
            return res


    #Todo account config 설정 or 글로벌 변수로
    def get_deposit(self,acntno,pwd):
        # 선물옵션 계좌예탁금증거금조회
        inblock_query_CFOBQ10500 = {
            'CFOBQ10500InBlock1' : {
                # 레코드갯수
                'RecCnt' : 50,
                # 계좌번호
                'AcntNo' : acntno,
                # 비밀번호
                'Pwd' : pwd
            }
        }

        data = self.xing.query('xing.CFOBQ10500', inblock_query_CFOBQ10500 )
        res1 = data['CFOBQ10500OutBlock1']
        res2 = data['CFOBQ10500OutBlock2']
        res3 = data['CFOBQ10500OutBlock3']
        #TODO 출력 항목 처리

        return res2,res3

    def account_orders(self,acntno):
        #TODO arguments/ 설정
        # 선물옵션 계좌주문체결내역조회
        inblock_query_CFOAQ00600 = {
            'CFOAQ00600InBlock1' : {
                # 레코드갯수
                'RecCnt' : 50,
                # 계좌번호
                'AcntNo' : acntno,
                # 입력비밀번호
                'InptPwd' : '0000',
                # 조회시작일
                'QrySrtDt' : None,
                # 조회종료일
                'QryEndDt' : None,
                # 선물옵션분류코드 00 전체 11 선물 12 옵션
                'FnoClssCode' : '00',
                # 상품군코드 00 전체 01 지수 02 개별주식
                'PrdgrpCode' : '00',
                # 체결구분 0 전체 1 체결 2 미체결
                'PrdtExecTpCode' : '0',
                # 정렬순서구분 3 역순 4 정순
                'StnlnSeqTp' : 3,
                # 통신매체코드
                'CommdaCode' : 99
            }
        }
        data = self.xing.query('xing.CFOAQ00600 ', inblock_query_CFOAQ00600 )
        res1 = data['CFOAQ00600OutBlock1']
        res2 = data['CFOAQ00600OutBlock2']
        res3 = data['CFOAQ00600OutBlock3']

        return res2, res3

    #TODO oder 관련 bbo, bid1, ask1, trail, stop, vwap 등 부가기능

    def send_order(self,acntno,pwd):
        #TODO aragumnerts/ return 항목, 타입 설정
        # 선물옵션 정상주문
        inblock_query_CFOAT00100 = {
            'CFOAT00100InBlock1': {
                # 계좌번호
                'AcntNo': acntno,
                # 비밀번호
                'Pwd': pwd,
                # 선물옵션종목번호
                'FnoIsuNo': None,
                # 매매구분
                'BnsTpCode': None,
                # 선물옵션호가유형코드
                'FnoOrdprcPtnCode': None,
                # 주문가격
                'OrdPrc': None,
                # 주문수량
                'OrdQty': None
            }
        }

        data = self.xing.query('xing.CFOAT00100 ', inblock_query_CFOAT00100 )
        res1 = data['CFOAT00100OutBlock1']
        res2 = data['CFOAT00100OutBlock2']

        return res1, res2


    def correct_order(self,acntno,pwd):
        # TODO aragumnerts/ return 항목, 타입 설정

        # 선물옵션 정정주문
        inblock_query_CFOAT00200 = {
            'CFOAT00200InBlock1': {
                # 계좌번호
                'AcntNo': acntno,
                # 비밀번호
                'Pwd': pwd,
                # 선물옵션종목번호
                'FnoIsuNo': None,
                # 원주문번호
                'OrgOrdNo': None,
                # 선물옵션호가유형코드
                'FnoOrdprcPtnCode': None,
                # 주문가격
                'OrdPrc': None,
                # 정정수량
                'MdfyQty': None
            }
        }
        data = self.xing.query('xing.CFOAT00200 ', inblock_query_CFOAT00200)
        res1 = data['CFOAT00200OutBlock1']
        res2 = data['CFOAT00200OutBlock2']

        return res1, res2

    def cancel_order(self,acntno):
        # TODO aragumnerts/ return 항목, 타입 설정

        # 선물옵션 취소주문
        inblock_query_CFOAT00300 = {
            'CFOAT00300InBlock1': {
                # 계좌번호
                'AcntNo': acntno,
                # 비밀번호
                'Pwd': '0000',
                # 선물옵션종목번호
                'FnoIsuNo': None,
                # 원주문번호
                'OrgOrdNo': None,
                # 취소수량
                'CancQty': None
            }
        }
        data = self.xing.query('xing.CFOAT00300 ', inblock_query_CFOAT00300)
        res1 = data['CFOAT00300OutBlock1']
        res2 = data['CFOAT00300OutBlock2']

        return res1, res2

















