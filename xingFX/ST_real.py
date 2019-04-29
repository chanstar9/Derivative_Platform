import sqlite3
from pystock_xingAPI import Xing, DBUtil

import datetime
import threading

import queue

#Todo 그외 real TR 추가여부
#Todo thread handle 개선

class KS_data_stream:

    def __init__(self, xing_inst, code, tosql=False, conn=None):
        self.code=code

        self.sise_q=queue.Queue()
        self.hoga_q=queue.Queue()
        self.sql_flag=queue.Queue()

        self.xing=xing_inst
        self.tosql=tosql
        self.conn=conn

        # KOSPI체결(S3)
        self.inblock_subscription_S3_ = {
            'InBlock': {
                # 단축코드
                'shcode': code
            }
        }

        # KOSPI호가잔량(H1)
        self.inblock_subscription_H1_ = {
            'InBlock': {
                # 단축코드
                'shcode': code
            }
        }

    def q_tosql(self,conn,q,table_name,q_flag):
        print("Start sql stream")
        while not q_flag.empty():
            while not q.empty():
                temp = q.get()
                #TODO 비교용 os time 추가
                nw = datetime.datetime.now().strftime('%y%m%d%H%M%S.%f')[:-4]
                temp['OutBlock']['os_time']=nw

                DBUtil.insert_for_outblock(conn.cursor(), table_name, temp['OutBlock'], place_flag=False)
                conn.commit()
                if q_flag.empty():
                    print('Break sql stream')
                    break
        print("Out from sql stream")

    def flush_queue(self,q):

        while q.qsize()>100:
            q.clear()

    def start_sub(self):
        try:
            self.xing.subscribe('xing.S3_', self.inblock_subscription_S3_, self.sise_q)
            self.xing.subscribe('xing.H1_', self.inblock_subscription_H1_, self.hoga_q)

            if self.tosql:
                self.table_name = 'DATA_che_' + self.code
                self.table_name_ho = 'DATA_ho_' + self.code

                self.sql_flag.put(1)

                DBUtil.create_table_for_outblock(self.conn.cursor(), self.table_name, 'S3_', 'OutBlock', None, None, {'os_time': 'double'})
                DBUtil.create_table_for_outblock(self.conn.cursor(), self.table_name_ho, 'H1_', 'OutBlock', None, None, {'os_time':'double'})

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



        except Exception as e:
            print(e)
            if self.tosql:
                print("Close Sub & Sql ")
                self.close_sub()
            else:
                print("Close")
                self.close_sub()

    def close_sub(self):
        self.xing.unsubscribe('xing.S3_', self.inblock_subscription_S3_, self.sise_q)
        self.xing.unsubscribe('xing.H1_', self.inblock_subscription_H1_, self.hoga_q)
        if self.tosql:
            if not self.sql_flag.empty():
                print("Call sql break ")
                self.sql_flag.get()
                self.conn.close()
            print("Close Sub & Sql ")
        else:
            print("Close Sub ")

class KQ_data_strem:

    def __init__(self, xing_inst, code, tosql=False):
        self.code=code

        self.sise_q=queue.Queue()
        self.hoga_q=queue.Queue()
        self.sql_flag=queue.Queue()

        self.xing=xing_inst
        self.tosql=tosql

        # KOSDAQ체결(K3)
        self.inblock_subscription_K3_ = {
            'InBlock': {
                # 단축코드
                'shcode': code
            }
        }

        # KOSDAQ호가잔량(HA)
        self.inblock_subscription_HA_ = {
            'InBlock': {
                # 단축코드
                'shcode': code
            }
        }

    def q_tosql(self,conn,q,table_name,q_flag):
        print("Start sql stream")
        while not q_flag.empty():
            while not q.empty():
                temp = q.get()
                #TODO 비교용 os time 추가
                nw = datetime.datetime.now().strftime('%y%m%d%H%M%S.%f')[:-4]
                temp['OutBlock']['os_time']=nw

                DBUtil.insert_for_outblock(conn.cursor(), table_name, temp['OutBlock'], place_flag=False)
                conn.commit()
                if q_flag.empty():
                    print('Break sql stream')
                    break
        print("Out from sql stream")

    def flush_queue(self,q):

        while q.qsize()>100:
            q.clear()

    def start_sub(self):
        try:
            self.xing.subscribe('xing.K3_', self.inblock_subscription_S3_, self.sise_q)
            self.xing.subscribe('xing.HA_', self.inblock_subscription_H1_, self.hoga_q)

            if self.tosql:
                self.table_name = 'DATA_che_' + self.code
                self.table_name_ho = 'DATA_ho_' + self.code

                self.sql_flag.put(1)

                DBUtil.create_table_for_outblock(self.conn.cursor(), self.table_name, 'S3_', 'OutBlock', None, None, {'os_time': 'double'})
                DBUtil.create_table_for_outblock(self.conn.cursor(), self.table_name_ho, 'H1_', 'OutBlock', None, None, {'os_time':'double'})

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



        except Exception as e:
            print(e)
            if self.tosql:
                print("Close Sub & Sql ")
                self.close_sub()
            else:
                print("Close")
                self.close_sub()


    def close_sub(self):
        self.xing.unsubscribe('xing.K3_', self.inblock_subscription_S3_, self.sise_q)
        self.xing.unsubscribe('xing.HA_', self.inblock_subscription_H1_, self.hoga_q)
        if self.tosql:
            if not self.sql_flag.empty():
                print("Call sql break ")
                self.sql_flag.get()
                self.conn.close()
            print("Close Sub & Sql ")
        else:
            print("Close Sub ")




