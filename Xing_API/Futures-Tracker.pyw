import sys, os
import datetime, time
import win32com.client
import pythoncom
import inspect
import glob

import pickle
import uuid
import base64
import json
import re

import PyQt5
from PyQt5 import QtCore, QtGui, uic
from PyQt5 import QAxContainer
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow, QDialog, QMessageBox, QProgressBar)
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *

import numpy as np
from numpy import NaN, Inf, arange, isscalar, asarray, array

import pandas as pd
import pandas.io.sql as pdsql
from pandas import DataFrame, Series

import talib as ta
from talib import MA_Type

import logging
import logging.handlers

from XASessions import *
from XAQuaries import *
from XAReals import *

from Utils import *


주문지연 = 3000

UI_DIR = "UI\\"


class CPortStock(object):
    def __init__(self, 매수일, 종목코드, 종목명, 매수가, 수량, STATUS=''):
        self.매수일 = 매수일
        self.종목코드 = 종목코드
        self.종목명 = 종목명
        self.매수가 = 매수가
        self.수량 = 수량
        self.STATUS = STATUS

        self.매수후고가 = 매수가


Ui_MainWindow, QtBaseClass_MainWindow = uic.loadUiType(UI_DIR+"Futures-Tracker.ui")
class MainWindow(QDialog, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Tracker - http://www.thinkalgo.co.kr")
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.connection = XASession(parent=self)

        # ------------------------------------------------------------------------
        self.매도 = 1
        self.매수 = 2
        self.지정가 = '00'
        self.시장가 = '1'
        self.조건없음 = '0'
        self.조건IOC = '1'
        self.조건FOK = '2'

        self.신용거래코드 = '000'

        self.거래시점 = '봉' # '틱' or '봉'

        self.틱주기 = 120

        self.ONETICK = 0.01
        self.TICKADJUST = 0
        self.myformat = "%0.2f"
        self.signedformat = self.myformat.replace("%", "%+")
        self.precision = '0.01000'
        
        self.매수후최고가 = 0.0
        self.TRAILSTOP = 11
        self.PROFITSTOP = 5
        self.SHORT = '10'
        self.SHORTSTR = 'EMA010'
        self.DIFFSTR = 'DIFF010'
        self.매수도방법 = '2'
        self.futureamt = '1'
        self.indexcode = 'UROM18'
        self.futurecode = 'UROM18'
        self.수동자동거래 = '수동' # 수동, 상승매수, 하락매도
        self.LOSSCUT_METHOD = '손절' # 손절, 트레일스탑

        self.현재가 = 0.0
        self.주문번호리스트 = []
        self.Lock = False

        self.portfolio = dict()

        self.QueryInit()

        self.clock = None
        self.running = False
        self.계좌정보 = None
        self.prevstatus = "▬"
        # ------------------------------------------------------------------------
        self.상태그림 = ['▼','▬','▲']
        self.상태문자 = ['매도', '대기', '매수']
        self.trend_indicator = "▬"*30
        self.trend_indicator_len = 30

    def QueryInit(self):
        self.XQ_t0167 = t0167(parent=self)
        self.ovc = None
        self.ovh = None
        self.o3137 = None
        self.o3137data = None
        self.signal = None

        self.XR_TC1 = None
        self.XR_TC2 = None
        self.XR_TC3 = None
        self.QA_CIDBT00100 = None
        self.QA_CIDBT01000 = None

        self.버퍼_가격 = []
        self.버퍼_거래량 = []

    def AdjustedPrice(self):
        return self.ONETICK * self.TICKADJUST

    def keyPressEvent(self, event):
        key = event.key()

        if key == QtCore.Qt.Key_Space:
            self.Lock = False
            for i in range(0,len(self.주문번호리스트)):
                self.CancelOrder()
            self.주문번호리스트 = []

        if key == QtCore.Qt.Key_Q:
            self.ShowAutoManual("상승매수")
            self.수동자동거래 = '상승매수'
        if key == QtCore.Qt.Key_E:
            self.ShowAutoManual("하락매도")
            self.수동자동거래 = '하락매도'
        if key == QtCore.Qt.Key_W:
            self.ShowAutoManual("수동")
            self.수동자동거래 = '수동'
        if key == QtCore.Qt.Key_X:
            self.ShowAutoManual("수동")
            self.수동자동거래 = '수동'
            self.Lock = False

            for i in range(0,len(self.주문번호리스트)):
                self.CancelOrder()

            self.주문번호리스트 = []
            self.매수후최고가 = 0.0
            self.portfolio['P'] = CPortStock(종목코드=self.futurecode, 종목명=self.futurecode, 매수가=0.0, 수량=0, 매수일=datetime.datetime.now())
            self.ShowLossCutPrice(self.myformat % self.매수후최고가)
            self.lineEdit_portfolio.setText(str(0))

        # 매수
        if key == QtCore.Qt.Key_A:
            self.ShowAutoManual("수동")
            self.수동자동거래 = '수동'
            self.매수후최고가 = self.현재가
            self.ShowLossCutPrice(self.myformat % (self.매수후최고가 - float(self.precision) * self.TRAILSTOP))
            주문가 = self.LongOrder(현재가=self.현재가, 주문수량=self.futureamt)
            self.ShowLog("수동매수 : %s (%s)" % (self.myformat % self.현재가, self.myformat % 주문가))
            logger.info("수동매수 : %s (%s)" % (self.myformat % self.현재가, self.myformat % 주문가))

        # 매도
        if key == QtCore.Qt.Key_D:
            self.ShowAutoManual("수동")
            self.수동자동거래 = '수동'
            self.매수후최고가 = self.현재가
            self.ShowLossCutPrice(self.myformat % (self.매수후최고가 + float(self.precision) * self.TRAILSTOP))
            주문가 = self.ShortOrder(현재가=self.현재가, 주문수량=self.futureamt)
            self.ShowLog("수동매도 : %s (%s)" % (self.myformat % self.현재가, self.myformat % 주문가))
            logger.info("수동매도 : %s (%s)" % (self.myformat % self.현재가, self.myformat % 주문가))

    def OnQApplicationStarted(self):
        self.clock = QtCore.QTimer()
        self.clock.timeout.connect(self.OnClockTick)
        self.clock.start(1000)

        self.iteminfo = dict()
        with open("ITEMS.txt", mode='r', encoding='utf-8') as itemfile:
            lines = itemfile.read()
            self.iteminfo = json.loads(lines)

        #TODO:자동로그인
        self.MyLogin()

        self.setFocus()

    def OnClockTick(self):
        current = datetime.datetime.now()
        current_str = current.strftime('%H:%M:%S')

        if current.second == 0:  # 매 0초
            self.XQ_t0167.Query()


    def OnLogin(self, code, msg):
        if code == '0000':
            self.ShowLog("로그인 되었습니다.")
        else:
            self.ShowLog("%s %s" % (code, msg))

    def Account(self, 구분):
        if self.계좌정보 is None:
            self.계좌정보 = pd.read_csv("secret/passwords.csv", converters={'계좌번호': str, '거래비밀번호': str})
        주식계좌정보 = self.계좌정보.query("구분 == '%s'" % 구분)
        계좌번호 = ''
        거래비밀번호 = ''
        if len(주식계좌정보) > 0:
            계좌번호 = 주식계좌정보['계좌번호'].values[0].strip()
            거래비밀번호 = 주식계좌정보['거래비밀번호'].values[0].strip()

        return (계좌번호, 거래비밀번호)

    def MyLogin(self):
        계좌정보 = pd.read_csv("secret/passwords.csv", converters={'계좌번호': str, '거래비밀번호': str})
        주식계좌정보 = 계좌정보.query("구분 == '해외선옵'")
        if len(주식계좌정보) > 0:
            if self.connection is None:
                self.connection = XASession(parent=self)

            self.계좌번호 = 주식계좌정보['계좌번호'].values[0].strip()
            self.id = 주식계좌정보['사용자ID'].values[0].strip()
            self.pwd = 주식계좌정보['비밀번호'].values[0].strip()
            self.cert = 주식계좌정보['공인인증비밀번호'].values[0].strip()
            self.거래비밀번호 = 주식계좌정보['거래비밀번호'].values[0].strip()
            self.url = 주식계좌정보['url'].values[0].strip()
            self.connection.login(url=self.url, id=self.id, pwd=self.pwd, cert=self.cert)
        else:
            self.ShowLog("secret디렉토리의 passwords.csv 파일에서 거래 계좌를 지정해 주세요")

    def OnReceiveMessage(self, systemError, messageCode, message):
        일자 = "{:%Y-%m-%d %H:%M:%S.%f}".format(datetime.datetime.now())
        if message.strip() != '조회완료':
            logger.info("%s %s %s" % (systemError, messageCode, message))
        self.ShowLog("[%s] %s %s %s" % (일자, systemError, messageCode, message))

    def make_signal(self):
        df = self.o3137data.copy()
        df['중간'] = (df['고가'] + df['저가']) / 2
        for i in [self.SHORT]:
            df['EMA%03d' % i] = ta.EMA(np.array(df['중간'].astype(float)), timeperiod=i)
            df['BUP'], df['BBAND'], df['BDOWN'] = ta.BBANDS(real=np.array(df['중간'].astype(float)),
                                                            timeperiod=i, nbdevup=2.0, nbdevdn=2.0,matype=MA_Type.EMA)
            df['DIFF%03d' % i] = df[['BUP','BBAND','BDOWN']].apply(lambda x: min(x[0]-x[1], x[1]-x[2]), axis=1)

        self.signal = df

    def make_signal_temp(self, _temp):
        df = self.o3137data.copy()
        df = df.append(_temp, ignore_index=True)

        df['중간'] = (df['고가'] + df['저가']) / 2
        for i in [self.SHORT]:
            df['EMA%03d' % i] = ta.EMA(np.array(df['중간'].astype(float)), timeperiod=i)
            df['BUP'], df['BBAND'], df['BDOWN'] = ta.BBANDS(real=np.array(df['중간'].astype(float)),
                                                            timeperiod=i, nbdevup=2.0, nbdevdn=2.0, matype=MA_Type.EMA)
            df['DIFF%03d' % i] = df[['BUP', 'BBAND', 'BDOWN']].apply(lambda x: min(x[0] - x[1], x[1] - x[2]), axis=1)

        return df

    def DelayedQuery(self):
        self.o3137.Query(시장구분='F', 단축코드=self.futurecode, 단위=str(self.틱주기), 건수='100', 연속시간=self.연속시간, 연속당일구분=self.연속당일구분, 연속조회=True)

    def OnReceiveData(self, szTrCode, result):
        if szTrCode == 't0167':
            # logger.info("Server Time : {} {}".format(result[0], result[1]))
            pass

        if szTrCode == 'o3137':
            단축코드, 레코드카운트, self.연속시간, self.연속당일구분, df = result
            if type(self.o3137data) == type(None):
                self.o3137data = df
            else:
                self.o3137data = pd.concat([self.o3137data, df])

            if len(self.o3137data) < 360:
                if len(df) < 80:
                    QTimer.singleShot(1 * 1000, self.DelayedQuery)
                else:
                    self.DelayedQuery()
            else:
                self.o3137data.reset_index(inplace=True)
                self.o3137data['index'] = 1
                self.o3137data['index'] = self.o3137data['index'].cumsum()
                self.o3137data = self.o3137data.sort_values(by='index', ascending=False)
                self.o3137data['index'] = 1
                self.o3137data['index'] = self.o3137data['index'].cumsum()
                self.o3137data.set_index('index', inplace=True)

                self.make_signal()

        if szTrCode == 'CIDBT00100':
            df, df1 = result
            if len(df1) > 0:
                주문번호 = df1['해외선물주문번호'].values[0]

                if 주문번호 != '0':
                    try:
                        self.주문번호리스트.append(int(주문번호))
                    except Exception as e:
                        self.주문번호리스트.append(주문번호)

        if szTrCode == 'CIDBT01000':
            df, df1 = result
            logger.info('----------------------------------------------------------')
            logger.info(df)
            logger.info(df1)
            logger.info('----------------------------------------------------------')

    def ShowPortfolio(self):
        _포트수량 = 0
        for p, v in self.portfolio.items():
            _포트수량 = v.수량
        self.lineEdit_portfolio.setText(str(_포트수량))

        self.lineEdit_profit.setText(self.signedformat % ((self.현재가 - self.portfolio['P'].매수가)*_포트수량))

        return _포트수량

    def ShowTrend(self, direction):
        self.trend_indicator = self.trend_indicator + self.상태그림[direction+1]
        self.trend_indicator = self.trend_indicator[-self.trend_indicator_len:]
        self.label_trend.setText(self.trend_indicator)

    def ShowAutoManual(self, txt):
        self.lineEdit_status.setText(txt)

    def ShowLog(self, txt):
        self.label_log.setText(txt)

    def ShowLossCutPrice(self, txt):
        self.lineEdit_losscut.setText(txt)

    def ShowLossCut(self, 현재가):
        if self.portfolio['P'].수량 > 0:
            if self.LOSSCUT_METHOD == "트레일스탑":
                if 현재가 > self.매수후최고가:
                    self.매수후최고가 = 현재가
                self.lineEdit_losscut.setText(self.myformat % (self.매수후최고가 - float(self.precision) * self.TRAILSTOP))
            if self.LOSSCUT_METHOD == '손절':
                self.lineEdit_losscut.setText(self.myformat % (self.매수후최고가 - float(self.precision) * self.TRAILSTOP))

        if self.portfolio['P'].수량 < 0:
            if self.LOSSCUT_METHOD == "트레일스탑":
                if 현재가 < self.매수후최고가:
                    self.매수후최고가 = 현재가
                self.lineEdit_losscut.setText(self.myformat % (self.매수후최고가 + float(self.precision) * self.TRAILSTOP))
            if self.LOSSCUT_METHOD == '손절':
                self.lineEdit_losscut.setText(self.myformat % (self.매수후최고가 + float(self.precision) * self.TRAILSTOP))

    def LongOrder(self, 현재가, 주문수량, 가격종류='지정가'):
        self.Lock = True
        result = 현재가
        if 가격종류=='시장가':
            주문가격 = 현재가
            result = 현재가
            self.QA_CIDBT00100.Query(계좌번호=self.계좌번호, 비밀번호=self.비밀번호, 종목코드값=self.futurecode, 선물주문구분코드='1', 매매구분코드='2', 해외선물주문유형코드=self.시장가, 해외파생주문가격='', 주문수량=주문수량)
        if 가격종류=='현재가':
            주문가격 = '' if self.매수도방법 == '1' else self.myformat % (현재가)
            result = 현재가 if self.매수도방법 == '1' else 현재가 + self.AdjustedPrice()
            self.QA_CIDBT00100.Query(계좌번호=self.계좌번호, 비밀번호=self.비밀번호, 종목코드값=self.futurecode, 선물주문구분코드='1', 매매구분코드='2', 해외선물주문유형코드=self.매수도방법, 해외파생주문가격=주문가격, 주문수량=주문수량)
        if 가격종류=='지정가':
            주문가격 = '' if self.매수도방법 == '1' else self.myformat % (현재가 + self.AdjustedPrice())
            result = 현재가 if self.매수도방법 == '1' else 현재가 + self.AdjustedPrice()
            self.QA_CIDBT00100.Query(계좌번호=self.계좌번호, 비밀번호=self.비밀번호, 종목코드값=self.futurecode, 선물주문구분코드='1', 매매구분코드='2', 해외선물주문유형코드=self.매수도방법, 해외파생주문가격=주문가격, 주문수량=주문수량)
        return result

    def ShortOrder(self, 현재가, 주문수량, 가격종류='지정가'):
        self.Lock = True
        if 가격종류 == '시장가':
            주문가격 = 현재가
            result = 현재가
            self.QA_CIDBT00100.Query(계좌번호=self.계좌번호, 비밀번호=self.비밀번호, 종목코드값=self.futurecode, 선물주문구분코드='1', 매매구분코드='1', 해외선물주문유형코드=self.시장가, 해외파생주문가격='', 주문수량=주문수량)
        if 가격종류 == '현재가':
            주문가격 = '' if self.매수도방법 == '1' else self.myformat % (현재가)
            result = 현재가 if self.매수도방법 == '1' else 현재가 + self.AdjustedPrice()
            self.QA_CIDBT00100.Query(계좌번호=self.계좌번호, 비밀번호=self.비밀번호, 종목코드값=self.futurecode, 선물주문구분코드='1', 매매구분코드='1', 해외선물주문유형코드=self.매수도방법, 해외파생주문가격=주문가격, 주문수량=주문수량)
        if 가격종류 == '지정가':
            주문가격 = '' if self.매수도방법 == '1' else self.myformat % (현재가 - self.AdjustedPrice())
            result = 현재가 if self.매수도방법 == '1' else 현재가 + self.AdjustedPrice()
            self.QA_CIDBT00100.Query(계좌번호=self.계좌번호, 비밀번호=self.비밀번호, 종목코드값=self.futurecode, 선물주문구분코드='1', 매매구분코드='1', 해외선물주문유형코드=self.매수도방법, 해외파생주문가격=주문가격, 주문수량=주문수량)
        return result

    def CancelOrder(self):
        if len(self.주문번호리스트)>0:
            _주문번호 = '{:0>10}'.format(self.주문번호리스트[-1])
            _날짜 = datetime.datetime.now().strftime("%Y%m%d")
            # _날짜 = self.체결일자
            # print(_날짜, _주문번호)
            self.QA_CIDBT01000.Query(주문일자=_날짜, 계좌번호=self.계좌번호, 비밀번호=self.비밀번호, 종목코드값=self.futurecode, 해외선물원주문번호=_주문번호, 선물주문구분코드='3')

    # -------------------------------------------------------------------------------------------------

    def Signal_BreakOutMA(self,현재가,SHORT):
        result = 0
        if 현재가 > SHORT:
            result = 1
        if 현재가 < SHORT:
            result = -1

        return result

    # -------------------------------------------------------------------------------------------------

    def OnReceiveRealData(self, szTrCode, result):
        if szTrCode == 'TC3':
            매도매수유형 = result['매도매수유형']
            주문번호 = result['주문번호']
            체결수량 = result['체결수량']
            체결가격 = result['체결가격']
            종목코드 = result['종목코드']

            if 종목코드 == self.futurecode:
                logger.info('----------------------------------------------------------')
                logger.info(result)
                logger.info('----------------------------------------------------------')

            if 주문번호 in self.주문번호리스트:
                self.Lock = False
                P = self.portfolio['P']
                P.종목코드 = result['종목코드']
                P.종목명 = result['종목코드']
                P.매수가 = 체결가격
                self.매수후최고가 = 체결가격
                if 매도매수유형 == '1' or 매도매수유형 == 1:  # 매도
                    P.수량 = P.수량 - 체결수량

                if 매도매수유형 == '2' or 매도매수유형 == 2:  # 매수
                    P.수량 = P.수량 + 체결수량

                if P.수량 == 0:
                    self.매수후최고가 = 0.0

                    self.ShowAutoManual("수동")
                self.수동자동거래 = '수동'

            else:
                if 종목코드 == self.futurecode:
                    P = self.portfolio['P']
                    P.매수가 = 체결가격
                    이전수량 = P.수량
                    if 매도매수유형 == '1' or 매도매수유형 == 1:  # 매도
                        P.수량 = P.수량 - 체결수량

                    if 매도매수유형 == '2' or 매도매수유형 == 2:  # 매수
                        P.수량 = P.수량 + 체결수량

                    if 이전수량 == 0:
                        self.매수후최고가 = 체결가격

                    if P.수량 == 0:
                        self.매수후최고가 = 0.0

                        self.ShowAutoManual("수동")
                    self.수동자동거래 = '수동'

            _포트수량 = self.ShowPortfolio()
            if _포트수량 == 0:
                self.portfolio['P'].매수가 = 0.0
                self.lineEdit_losscut.setText(self.myformat % 0.0)

        if szTrCode in ['OVC']:
            if type(self.signal) is type(None) or len(self.signal) < 10:
                return

            if len(self.portfolio) == 0:
                self.portfolio['P'] = CPortStock(종목코드=self.futurecode, 종목명=self.futurecode, 매수가=0.0, 수량=0, 매수일=datetime.datetime.now())

            self.버퍼_가격.append(result['체결가격'])
            self.버퍼_거래량.append(result['건별체결수량'])
            현재가 = result['체결가격']
            self.현재가 = 현재가

            self.ShowLossCut(현재가=현재가)

            # 틱 수가 차면 봉을 만듦
            if len(self.버퍼_가격) >= self.틱주기:
                _price = self.버퍼_가격[:self.틱주기]
                _vol = self.버퍼_거래량[:self.틱주기]
                self.버퍼_가격 = self.버퍼_가격[self.틱주기:]
                self.버퍼_거래량 = self.버퍼_거래량[self.틱주기:]

                _시가 = _price[0]
                _고가 = max(_price)
                _저가 = min(_price)
                _종가 = _price[-1]
                _거래량 = sum(_vol)

                lst = [[result['체결일자_현지'], result['체결시간_현지'], _시가, _고가, _저가, _종가, _거래량]]
                _temp = DataFrame(data=lst, columns=self.o3137data.columns)
                self.o3137data = self.o3137data.append(_temp, ignore_index=True)

                if len(self.o3137data) > 300:
                    self.o3137data = self.o3137data.iloc[-260:]

                self.make_signal()

            # 틱 거래이면 미완성 봉으로
            # 봉 거래이면 완성된 봉으로.
            if self.거래시점 == '틱' and len(self.버퍼_가격) > 0:
                _시가 = self.버퍼_가격[0]
                _고가 = max(self.버퍼_가격)
                _저가 = min(self.버퍼_가격)
                _종가 = self.버퍼_가격[-1]
                _거래량 = sum(self.버퍼_거래량)

                lst = [[result['체결일자_현지'], result['체결시간_현지'], _시가, _고가, _저가, _종가, _거래량]]
                _temp = DataFrame(data=lst, columns=self.o3137data.columns)

                signal = self.make_signal_temp(_temp)
            else:
                signal = self.signal

            현재시각 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            SHORT = signal[self.SHORTSTR].values[-1]
            DIFF = signal[self.DIFFSTR].values[-1]

            y = self.Signal_BreakOutMA(현재가,SHORT)
            self.ShowTrend(y)

            _f = "%s [%s-%s]" % (self.myformat,self.myformat, self.myformat)
            self.lineEdit_price.setText(_f % (현재가, SHORT, DIFF))

            currentstatus = "{}".format(self.상태그림[y+1])
            if self.prevstatus != currentstatus:
                _format = "%s " + self.myformat
                self.lineEdit_position.setText(_format % (self.상태그림[y+1], 현재가))
                self.prevstatus = currentstatus

            _text = "[%s] lookback:%s Lock:%s" % (현재시각, len(self.o3137data), self.Lock)
            self.ShowLog(_text)

            _포트수량 = self.ShowPortfolio()

            # 수익처리
            if self.Lock == False:
                if self.portfolio['P'].수량 > 0 and self.portfolio['P'].매수가 != 0.0:
                    if 현재가 >= self.portfolio['P'].매수가 + self.ONETICK * self.PROFITSTOP:
                        주문가 = self.ShortOrder(현재가=현재가, 주문수량=str(abs(self.portfolio['P'].수량)), 가격종류='시장가')
                        self.수동자동거래 = '수동'
                        self.ShowAutoManual("수동")
                        self.ShowLossCutPrice(self.myformat % 0.0)
                        self.ShowLog("수익매도 : %s (%s)" % (현재가, 주문가))
                        logger.info("수익매도 : %s (%s)" % (현재가, 주문가))

                if self.portfolio['P'].수량 < 0 and self.portfolio['P'].매수가 != 0.0:
                    if 현재가 <= self.portfolio['P'].매수가 - self.ONETICK * self.PROFITSTOP:
                        주문가 = self.LongOrder(현재가=현재가, 주문수량=str(abs(self.portfolio['P'].수량)), 가격종류='시장가')
                        self.수동자동거래 = '수동'
                        self.ShowAutoManual("수동")
                        self.ShowLossCutPrice(self.myformat % 0.0)
                        self.ShowLog("수익매수 : %s (%s)" % (현재가, 주문가))
                        logger.info("수익매수 : %s (%s)" % (현재가, 주문가))

            # 로스컷 처리
            losscut_price = float(self.lineEdit_losscut.text().strip())
            if losscut_price > 0.0:
                if self.Lock == False:
                    if self.portfolio['P'].수량 > 0:
                        if 현재가 <= losscut_price:
                            주문가 = self.ShortOrder(현재가=현재가, 주문수량=str(abs(self.portfolio['P'].수량)), 가격종류='시장가')
                            self.수동자동거래 = '수동'
                            self.ShowAutoManual("수동")
                            self.ShowLossCutPrice(self.myformat % 0.0)
                            self.ShowLog("손절매도 : %s (%s)" % (현재가, self.myformat % (주문가)))
                            logger.info("손절매도 : %s (%s)" % (현재가, self.myformat % (주문가)))

                    if self.portfolio['P'].수량 < 0:
                        if 현재가 >= losscut_price:
                            주문가 = self.LongOrder(현재가=현재가, 주문수량=str(abs(self.portfolio['P'].수량)), 가격종류='시장가')
                            self.수동자동거래 = '수동'
                            self.ShowAutoManual("수동")
                            self.ShowLossCutPrice(self.myformat % 0.0)
                            self.ShowLog("손절매수 : %s (%s)" % (현재가, self.myformat % (주문가)))
                            logger.info("손절매수 : %s (%s)" % (현재가, self.myformat % (주문가)))

            # 자동거래의 경우 - 보유 수량이 없을 경우 자동거래 가능
            if self.Lock == False:
                x = self.Signal_BreakOutMA(현재가,SHORT)
                if x == 1 and self.수동자동거래 == "상승매수":
                    if self.portfolio['P'].수량 <= 0:
                        self.매수후최고가 = self.현재가
                        주문가 = self.LongOrder(현재가=현재가, 주문수량=str(abs(self.portfolio['P'].수량)+int(self.futureamt)))
                        self.ShowLossCutPrice(self.myformat % (self.매수후최고가 - float(self.precision) * self.TRAILSTOP))
                        self.ShowLog("매수 : %s (%s)" % (현재가, self.myformat % (주문가)))
                        logger.info("매수 : %s (%s)" % (현재가, self.myformat % (주문가)))

                if x == -1 and self.수동자동거래 == "하락매도":
                    if self.portfolio['P'].수량 >= 0:
                        self.매수후최고가 = self.현재가
                        주문가 = self.ShortOrder(현재가=현재가, 주문수량=str(abs(self.portfolio['P'].수량)+int(self.futureamt)))
                        self.ShowLossCutPrice(self.myformat % (self.매수후최고가 + float(self.precision) * self.TRAILSTOP))
                        self.ShowLog("매도 : %s (%s)" % (현재가, self.myformat % (주문가)))
                        logger.info("매도 : %s (%s)" % (현재가, self.myformat % (주문가)))

    def Run(self, flag=True):
        if self.running == flag:
            return

        self.running = flag
        ret = 0
        if flag == True:
            self.clock = QtCore.QTimer()
            self.clock.timeout.connect(self.OnClockTick)
            self.clock.start(1000)

            self.QueryInit()
            
            self.주문번호리스트 = []
            self.Lock = False

            self.계좌번호, self.비밀번호 = self.Account(구분='해외선옵')
            self.ShowLog("%s-%s" %(self.계좌번호, self.비밀번호))

            if len(self.portfolio) == 0:
                self.portfolio['P'] = CPortStock(종목코드=self.futurecode, 종목명=self.futurecode, 매수가=0.0, 수량=0, 매수일=datetime.datetime.now())

            self.o3137 = o3137(parent=self)
            self.o3137.Query(시장구분='F',단축코드=self.futurecode,단위=str(self.틱주기),건수='100',연속시간='',연속당일구분='',연속조회=False)

            self.ovc = OVC(parent=self)
            self.ovc.AdviseRealData(종목코드=self.futurecode)

            self.QA_CIDBT00100 = CIDBT00100(parent=self)
            self.QA_CIDBT01000 = CIDBT01000(parent=self)

            self.XR_TC1 = TC1(parent=self)
            self.XR_TC2 = TC2(parent=self)
            self.XR_TC3 = TC3(parent=self)

            self.XR_TC1.AdviseRealData()
            self.XR_TC2.AdviseRealData()
            self.XR_TC3.AdviseRealData()

        else:
            if self.clock is not None:
                try:
                    self.clock.stop()
                except Exception as e:
                    pass
                finally:
                    self.clock = None

            try:
                if self.o3137 != None:
                    self.o3137 = None
            except Exception as e:
                pass
            finally:
                self.o3137 = None

            try:
                if self.ovc != None:
                    self.ovc.UnadviseRealData()
            except Exception as e:
                pass
            finally:
                self.ovc = None

            try:
                if self.XR_TC1 != None:
                    self.XR_TC1.UnadviseRealData()
            except Exception as e:
                pass
            finally:
                self.XR_TC1 = None

            try:
                if self.XR_TC2 != None:
                    self.XR_TC2.UnadviseRealData()
            except Exception as e:
                pass
            finally:
                self.XR_TC2 = None

            try:
                if self.XR_TC3 != None:
                    self.XR_TC3.UnadviseRealData()
            except Exception as e:
                pass
            finally:
                self.XR_TC3 = None

    def ValuesChanged(self):
        self.GetValues()
        self.setFocus()

    def GetValues(self):
        self.매수도방법 = self.comboBox_buysell_sHogaGb.currentText().strip()[0]
        if self.매수도방법 in ['1','2']: # 시장가, 현재가
            self.TICKADJUST = 0
        if self.매수도방법 in ['3','4','5','6','7','8','9']:
            self.TICKADJUST = int(self.매수도방법)-2
        if self.매수도방법 in ['A','B','C','D','E','F','G']:
            self.TICKADJUST = ord('A') - ord(self.매수도방법) -1
        if self.매수도방법 not in ['1','2']:
            self.매수도방법 = '2'
        self.TRAILSTOP = int(self.comboBox_trailstop.currentText().strip())
        self.PROFITSTOP = int(self.comboBox_profitstop.currentText().strip())
        self.틱주기 = int(self.comboBox_period.currentText().strip())
        self.SHORT = int(self.comboBox_short.currentText().strip())
        self.SHORTSTR = 'EMA%03d' % self.SHORT
        self.DIFFSTR = 'DIFF%03d' % self.SHORT
        self.futureamt = str(int(self.comboBox_amt.currentText().strip()))
        self.futurecode = self.lineEdit_futurecode.text().strip()
        self.수동자동거래 = self.lineEdit_status.text().strip()
        self.LOSSCUT_METHOD = self.comboBox_losscut_method.currentText().strip()
        self.myformat = "%0.5f"
        if self.precision == '0.00005':
            self.myformat = "%0.5f"
        if self.precision == '0.00010':
            self.myformat = "%0.4f"
        if self.precision == '0.01000':
            self.myformat = "%0.2f"
        if self.precision == '0.25000':
            self.myformat = "%0.2f"
        if self.precision == '0.10000':
            self.myformat = "%0.1f"
        if self.precision == '1.00000':
            self.myformat = "%0.0f"

        if len(self.portfolio) > 0:
            if self.portfolio['P'].수량 > 0:
                self.lineEdit_losscut.setText(self.myformat % (self.매수후최고가 - float(self.precision) * self.TRAILSTOP))

            if self.portfolio['P'].수량 < 0:
                self.lineEdit_losscut.setText(self.myformat % (self.매수후최고가 + float(self.precision) * self.TRAILSTOP))

            self.lineEdit_portfolio.setText(str(self.portfolio['P'].수량))

    def SELECTITEM(self, item):
        if item == 'EuroFX':
            indexcode, futurecode, period, precision, onetick, myformat = self.iteminfo['EuroFX']
        if item == 'EuroFX mini':
            indexcode, futurecode, period, precision, onetick, myformat = self.iteminfo['EuroFXmini']
        if item == 'EuroFX micro':
            indexcode, futurecode, period, precision, onetick, myformat = self.iteminfo['EuroFXmicro']
        if item == 'S&P 500 mini':
            indexcode, futurecode, period, precision, onetick, myformat = self.iteminfo['SP500mini']
        if item == 'NASDAQ mini':
            indexcode, futurecode, period, precision, onetick, myformat = self.iteminfo['NASDAQmini']
        if item == 'HangSeng mini':
            indexcode, futurecode, period, precision, onetick, myformat = self.iteminfo['HangSengmini']
        if item == 'Crude Oil':
            indexcode, futurecode, period, precision, onetick, myformat = self.iteminfo['CrudeOil']
        if item == 'Gold':
            indexcode, futurecode, period, precision, onetick, myformat = self.iteminfo['Gold']

        self.indexcode = indexcode
        self.futurecode = futurecode
        self.틱주기 = period
        self.precision = precision
        self.ONETICK = onetick
        self.myformat = myformat
        self.signedformat = self.myformat.replace("%", "%+")

        self.lineEdit_futurecode.setText(futurecode.strip())

        self.GetValues()
        self.setFocus()

    def FOCUS(self):
        self.GetValues()
        self.setFocus()

    def START(self):
        self.SELECTITEM(self.comboBox_item.currentText().strip())
        self.Run(flag=True)


if __name__ == "__main__":
    # 1.로그 인스턴스를 만든다.
    logger = logging.getLogger('Futures')
    # 2.formatter를 만든다.
    formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s]%(asctime)s>%(message)s')

    loggerLevel = logging.DEBUG
    filename = "LOG/Futures.log"

    # 스트림과 파일로 로그를 출력하는 핸들러를 각각 만든다.
    filehandler = logging.FileHandler(filename)
    streamhandler = logging.StreamHandler()

    # 각 핸들러에 formatter를 지정한다.
    filehandler.setFormatter(formatter)
    streamhandler.setFormatter(formatter)

    # 로그 인스턴스에 스트림 핸들러와 파일 핸들러를 붙인다.
    logger.addHandler(filehandler)
    logger.addHandler(streamhandler)
    logger.setLevel(loggerLevel)
    logger.debug("=============================================================================")
    logger.info("LOG START")

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)

    window = MainWindow()
    window.show()

    QTimer().singleShot(3, window.OnQApplicationStarted)

    sys.exit(app.exec_())

