import sqlite3
from pystock_xingAPI import Xing, DBUtil

import datetime
import threading

import queue

#Todo 그외 real 추가여부
#Todo thread handle 개선
class KFX_data_stream:

    def __init__(self,xing_inst,code, tosql=False, conn=None):
        self.code=code

        self.sise_q=queue.Queue()
        self.hoga_q=queue.Queue()
        self.sql_flag=queue.Queue()

        self.xing=xing_inst
        self.tosql=tosql
        self.conn=conn


        # KOSPI체결(FC0)
        self.inblock_subscription_FC0 = {
            'InBlock': {
                # 단축코드
                'futcode': self.code
            }
        }
        # KOSPI호가(FH0)
        self.inblock_subscription_FH0 = {
            'InBlock': {
                # 단축코드
                'futcode': self.code
            }
        }

    def q_tosql(self,conn,q,table_name,q_flag):
        print("Start sql stream")
        while not q_flag.empty():
            while not q.empty():
                temp = q.get()
                #########
                nw = datetime.datetime.now().strftime('%y%m%d%H%M%S.%f')[:-4]
                temp['OutBlock']['os_time'] = nw

                #########
                DBUtil.insert_for_outblock(conn.cursor(), table_name, temp['OutBlock'], place_flag=False)

                conn.commit()
                if q_flag.empty():
                    print('Break sql stream')
                    break

        print("Out from sql stream")

    def flush_queue(self, q):

        while q.qsize() > 100:
            q.queue.clear()

    def start_sub(self):
        try:
            self.xing.subscribe('xing.FC0', self.inblock_subscription_FC0, self.sise_q)
            self.xing.subscribe('xing.FH0', self.inblock_subscription_FH0, self.hoga_q)

            if self.tosql:
                self.table_name = 'DATA_che_' + self.code
                self.table_name_ho = 'DATA_ho_' + self.code

                self.sql_flag.put(1)

                DBUtil.create_table_for_outblock(self.conn.cursor(), self.table_name, 'FCO', 'OutBlock', None, None, {'os_time':'double'})
                DBUtil.create_table_for_outblock(self.conn.cursor(), self.table_name_ho, 'FHO', 'OutBlock', None, None, {'os_time':'double'})

                #TODO Sqlite concurreny문제
                t1 = threading.Thread(target=self.q_tosql, args=(self.conn, self.sise_q, self.table_name, self.sql_flag))
                t2 = threading.Thread(target=self.q_tosql, args=(self.conn, self.hoga_q, self.table_name_ho, self.sql_flag))

                t1.daemon = True
                t2.daemon = True
                t1.start()
                t2.start()

            #Else empty queues
            #TODO Else empty queues
            else:
                t1 = threading.Thread(target=self.flush_queue, args=(self.sise_q,))
                t2 = threading.Thread(target=self.flush_queue, args=(self.hoga_q,))

                t1.daemon = True
                t2.daemon = True
                t1.start()
                t2.start()

        except Exception as e:
            if self.tosql:
                print(e, "Close Sub & Sql ")
                self.close_sub()
            else:
                print(e, "Close")
                self.close_sub()

    def close_sub(self):
        self.xing.unsubscribe('xing.FC0', self.inblock_subscription_FC0, self.sise_q)
        self.xing.unsubscribe('xing.FH0', self.inblock_subscription_FH0, self.hoga_q)
        if self.tosql:
            if not self.sql_flag.empty():
                print("Call sql break ")
                self.sql_flag.get()
                self.conn.close()
            print("Close Sub & Sql ")
        else:
            print("Close Sub ")


#Todo 그외 real 추가여부
#Todo thread handle 개선
#Todo 가격 datastream + price_tr 데이터결합 후 콜 되는 방식으로 데이터포인트

class Kopt_data_stream:

    def __init__(self, xing_inst, code, tosql=False, conn=None):
        self.code=code

        self.sise_q=queue.Queue()
        self.hoga_q=queue.Queue()
        self.sql_flag=queue.Queue()

        self.xing=xing_inst
        self.tosql=tosql
        self.conn=conn

        # KOSPI200옵션체결(C0)
        self.inblock_subscription_OC0 = {
            'InBlock': {
                # 단축코드
                'optcode': code
            }
        }
        # KOSPI200옵션호가(H0)
        self.inblock_subscription_OH0 = {
            'InBlock': {
                # 단축코드
                'optcode': code
            }
        }

    def q_tosql(self,conn,q,table_name,q_flag):
        print("Start sql stream")
        while not q_flag.empty():
            while not q.empty():
                temp = q.get()
                #########
                nw = datetime.datetime.now().strftime('%y%m%d%H%M%S.%f')[:-4]
                temp['OutBlock']['os_time'] = nw

                #########
                DBUtil.insert_for_outblock(conn.cursor(), table_name, temp['OutBlock'], place_flag=False)

                conn.commit()
                if q_flag.empty():
                    print('Break sql stream')
                    break

        print("Out from sql stream")

    def flush_queue(self,q):

        while q.qsize()>100:
            q.queue.clear()


    def start_sub(self):
        try:
            self.xing.subscribe('xing.OC0', self.inblock_subscription_OC0, self.sise_q)
            self.xing.subscribe('xing.OH0', self.inblock_subscription_OH0, self.hoga_q)

            if self.tosql:
                print("Sql put")
                self.table_name = 'DATA_che_' + self.code
                self.table_name_ho = 'DATA_ho_' + self.code

                self.sql_flag.put(1)

                DBUtil.create_table_for_outblock(self.conn.cursor(), self.table_name, 'OC0', 'OutBlock', None)
                DBUtil.create_table_for_outblock(self.conn.cursor(), self.table_name_ho, 'OH0', 'OutBlock', None)

                #TODO Sqlite concurreny문제로 thread 한 개에만 가능,
                t1 = threading.Thread(target=self.q_tosql, args=(self.conn, self.sise_q, self.table_name, self.sql_flag))
                t2 = threading.Thread(target=self.q_tosql, args=(self.conn, self.hoga_q, self.table_name_ho, self.sql_flag))

                t1.daemon = True
                t2.daemon = True
                t1.start()
                t2.start()

            #TODO Else empty queues
            else:
                t1 = threading.Thread(target=self.flush_queue, args=(self.sise_q,))
                t2 = threading.Thread(target=self.flush_queue, args=(self.hoga_q,))

                t1.daemon = True
                t2.daemon = True
                t1.start()
                t2.start()

        except:
            if self.tosql:
                print("Close Sub & Sql ")
                self.close_sub()
            else:
                print("Close")
                self.close_sub()

    def close_sub(self):
        self.xing.unsubscribe('xing.OC0', self.inblock_subscription_OC0, self.sise_q)
        self.xing.unsubscribe('xing.OH0', self.inblock_subscription_OH0, self.hoga_q)
        if self.tosql:
            if not self.sql_flag.empty():
                print("Call sql break ")
                self.sql_flag.get()
                self.conn.close()
            print("Close Sub & Sql ")
        else:
            print("Close Sub ")


class FFX_data_stream:

    def __init__(self, xing_inst, code, tosql=False, conn=None):
        self.code=code

        self.sise_q=queue.Queue()
        self.hoga_q=queue.Queue()
        self.sql_flag=queue.Queue()

        self.xing=xing_inst
        self.tosql=tosql
        self.conn = conn

        # 해선체결
        self.inblock_subscription_OVC = {
            'InBlock': {
                # 단축코드
                'symbol': code
            }
        }
        # 해선호가(OVH)
        self.inblock_subscription_OVH = {
            'InBlock': {
                # 단축코드
                'symbol': code
            }
        }

    def q_tosql(self,conn,q,table_name,q_flag):
        print("Start sql stream")
        #TODO q_empty 여야 method종료되도록 전환
        while not q_flag.empty():
            #print("outer_sql_loop")
            while not q.empty():
                try:
                    #print("inner sql loop")
                    temp = q.get()
                    #########
                    nw = datetime.datetime.now().strftime('%y%m%d%H%M%S.%f')[:-4]
                    temp['OutBlock']['os_time'] = nw

                    #########
                    #print("Sql data insert :", temp)
                    DBUtil.insert_for_outblock(conn.cursor(), table_name, temp['OutBlock'], place_flag=False)

                    conn.commit()
                    if q_flag.empty():
                        print('Break sql stream')
                        break
                except Exception as e:
                    print(e)

        print("Out from sql stream")

    def flush_queue(self,q):

        while q.qsize()>100:
            q.queue.clear()

    def start_sub(self):
        try:
            self.xing.subscribe('xing.OVC', self.inblock_subscription_OVC, self.sise_q)
            self.xing.subscribe('xing.OVH', self.inblock_subscription_OVH, self.hoga_q)

            if self.tosql:
                print("Sql put")
                self.table_name = 'DATA_che_' + self.code
                self.table_name_ho = 'DATA_ho_' + self.code

                self.sql_flag.put(1)
                #self.conn_che = sqlite3.connect("stream_FFX_{0}_che.db".format(self.code))
                #self.conn_ho = sqlite3.connect("stream_FFX_{0}_ho.db".format(self.code))
                #self.conn = sqlite3.connect("stream_FFX_{0}.db".format(self.code),check_same_thread=False)

                DBUtil.create_table_for_outblock(self.conn.cursor(), self.table_name, 'OVC', 'OutBlock', None, None, {'os_time':'double'})
                DBUtil.create_table_for_outblock(self.conn.cursor(), self.table_name_ho, 'OVH', 'OutBlock', None, None, {'os_time':'double'})

                #TODO Sqlite concurreny문제로 thread 한 개에만 가능,
                t1 = threading.Thread(target=self.q_tosql, args=(self.conn, self.sise_q, self.table_name, self.sql_flag))
                t2 = threading.Thread(target=self.q_tosql, args=(self.conn, self.hoga_q, self.table_name_ho, self.sql_flag))

                t1.daemon = True
                t2.daemon = True
                t1.start()
                t2.start()

            #TElse empty queues
            #TODO Else empty queues
            else:
                t1 = threading.Thread(target=self.flush_queue, args=(self.sise_q,))
                t2 = threading.Thread(target=self.flush_queue, args=(self.hoga_q,))

                t1.daemon = True
                t2.daemon = True
                t1.start()
                t2.start()


        except Exception as e:
            if self.tosql:
                print(e,"Close Sub & Sql ")
                self.close_sub()
            else:
                print(e,"Close")
                self.close_sub()

    def close_sub(self):
        self.xing.unsubscribe('xing.OVC', self.inblock_subscription_OVC, self.sise_q)
        self.xing.unsubscribe('xing.OVH', self.inblock_subscription_OVH, self.hoga_q)
        if self.tosql:
            if not self.sql_flag.empty():
                print("Call sql break ")
                self.sql_flag.get()
                self.conn.close()
            print("Close Sub & Sql ")
        else:
            print("Close Sub ")


