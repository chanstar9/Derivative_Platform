import sqlite3
from pystock_xingAPI import Xing, DBUtil
import logging
import logging.handlers
import pandas as pd
import datetime as dt
from xingFX.KFX_tosql import KFX_sql
from xingFX.FX_tr import FX_tr

if __name__ == '__main__':

    # 1. 로거 인스턴스를 만든다
    logger = logging.getLogger('mylogger')

    # 2. 스트림과 파일로 로그를 출력하는 핸들러를 각각 만든다.
    fileHandler = logging.FileHandler('./API_KFX.log')
    streamHandler = logging.StreamHandler()

    # 3. 1번에서 만든 로거 인스턴스에 스트림 핸들러와 파일핸들러를 붙인다.
    logger.addHandler(fileHandler)
    logger.addHandler(streamHandler)
    # 4. 로거 인스턴스로 로그를 찍는다.
    logger.setLevel(logging.DEBUG)

    xing = Xing("demo.ebestsec.co.kr", 20001, 1, 0, "", "", "", logger=logging.getLogger('mylogger'))

    xing.open_manual()

    kfx_tosql = KFX_sql(xing, 'xingDB')
    kfx_tr=FX_tr(xing)

    #코드 받아오기
    kfx_code = kfx_tr.get_kfx_codes()
    target_codes = kfx_code.shcode.iloc[:3]

    #데이터 베이스 저장 실행
    kfx_tosql.KFX_min_sql(30,target_codes,20190401)