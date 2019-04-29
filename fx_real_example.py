from pystock_xingAPI import Xing, DBUtil
import logging
import logging.handlers

import pandas as pd
import datetime
import threading
import queue
import sqlite3
import time

from xingFX.FX_tr import FX_tr
from xingFX.FX_real import *

from operator import methodcaller

def start_subs(d):
    for a in map(methodcaller('start_sub'),d.values()):
        pass
        #print(a)

def close_subs(d):
    for a in map(methodcaller('close_sub'),d.values()):
        pass
        #print(a)

if __name__ == '__main__':

    # 1. 로거 인스턴스를 만든다
    logger = logging.getLogger('mylogger')

    # 2. 스트림과 파일로 로그를 출력하는 핸들러를 각각 만든다.
    fileHandler = logging.FileHandler('./module_test.log')
    streamHandler = logging.StreamHandler()

    # 3. 1번에서 만든 로거 인스턴스에 스트림 핸들러와 파일핸들러를 붙인다.
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)
    # 4. 로거 인스턴스로 로그를 찍는다.
    # logger.setLevel(logging.INFO)
    logger.setLevel(logging.DEBUG)

    # xing 객체생성
    xing = Xing("demo.ebestsec.co.kr", 20001, 1, 0, "", "", "", logger=logging.getLogger('mylogger'))

    # xing 객체연결, 연결시 로그인
    xing.open_manual()

    # TR 조회 객체 생성
    fx_tr = FX_tr(xing)

    # 해외선물 코드 받기
    ffx_codes = fx_tr.get_ffx_codes()
    #SNP_codes = [code for code in ffx_codes.Symbol if ('ES' in code) & (len(code) < 6)]

    # c_list=SNP_codes

    c_list = ['ESM19', 'ESU19', 'CLM19', 'CLU19', 'ADM19', 'EDM19', 'VXK19']
    #코드 데이터프레임에서 100종목
    c_list = ffx_codes.Symbol[:100]

    # TODO check_same_thread 주의/ sql concurrency & 지연 해결 ( mysql, mongdoDB 등, log, txt) log 이후 사후 데이터베이스화가 최적
    # ffx_conn = sqlite3.connect("stream_FFX.db", check_same_thread=False)

    #Real data stream 받아오는 클래스를 각 종목별로 생성, dict 에 저장

    d = {}
    for x in c_list:
        # d["FFX{0}".format(x)] = FFX_data_stream(xing, x, True, ffx_conn)
        d["FFX{0}".format(x)] = FFX_data_stream(xing, x, True,
                                                sqlite3.connect("\xingDB\stream_FFX_{0}.db".format(x), check_same_thread=False))

    # Log 에만 찍는 경우
    d = {}
    for x in c_list:
        # d["FFX{0}".format(x)] = FFX_data_stream(xing, x, True, ffx_conn)
        d["FFX{0}".format(x)] = FFX_data_stream(xing, x, False, None)

    #method caller & mapping 을 통해서 dict 안의 전체 구독 method들을 실행시킴
    print("Start multiple subs")
    time.sleep(2)
    start_subs(d)
    #TODO 일정시간(장조료)시 자동 구독종료
    time.sleep(120)
    close_subs(d)