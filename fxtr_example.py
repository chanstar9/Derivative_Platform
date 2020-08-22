from pystock_xingAPI import Xing, DBUtil

import logging.handlers
import pandas as pd

from xingFX.FX_tr import FX_tr
import matplotlib.pyplot as plt

def kfx_min(code='101P6000', min=30):
    min_ohlc = fx_tr.KFX_min(code,min)
    return min_ohlc

def get_ivs(maturity='201905'):

    fx,call,put=fx_tr.option_board(maturity)


    fx_atm = float(fx['gmprice'])
    call=call.apply(pd.to_numeric,errors='ignore')
    put=put.apply(pd.to_numeric,errors='ignore')


    plt.figure()

    ax1= plt.subplot(2,2,1)
    ax1.set_title('Call '+maturity+' IV')
    ax1.plot(call.actprice,call.iv, color='red')
    ax1.axvline(fx_atm,0,0.75)

    ax12= plt.subplot(2,2,2)
    ax12.set_title('Call '+maturity+' Price')
    ax12.plot(call.actprice, call.price, color='red')
    ax12.plot(call.actprice, call.theoryprice, color='black')
    ax12.axvline(fx_atm,0,0.75)


    ax2= plt.subplot(2,2,3, sharex=ax1)
    ax2.set_title('Put ' + maturity + ' IV')
    ax2.plot(put.actprice,put.iv, color='blue')
    ax2.axvline(fx_atm,0,0.75)

    ax22= plt.subplot(2,2,4)
    ax22.set_title('Put '+maturity+' Price')
    ax22.plot(put.actprice, put.price, color='blue')
    ax22.plot(put.actprice, put.theoryprice, color='black')
    ax22.axvline(fx_atm,0,0.75)


    plt.show()

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


    #xing 객체(접속) 객체 생성
    xing = Xing("demo.ebestsec.co.kr", 20001, 1, 0, "id", "pwd", "", logger=logging.getLogger('mylogger'))
    #로그인
    xing.open_manual()

    #tr 조회용 객체 생성
    fx_tr = FX_tr(xing)
    #tr 객체에서 KFX 코드 불러오는 메소드 실행, 변수에 저장
    kfx_codes = fx_tr.get_kfx_codes()

    get_ivs()

    #(연결프로그램)로그인 종료
    xing.close()
