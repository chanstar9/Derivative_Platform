import numpy as np
import pandas as pd
import eikon as ek
from data import RICs as ric


def eikon_init():
    app_key = pd.read_csv('get_data/app_key.csv')
    ek.set_app_key(app_key['app_key'][0])

eikon_init()





######################################################################
DJIA = '.DJI'  # 다우존스
SPX = '.SPX'  # S&P500
KOSPI = '.KS11'  # 코스피
KOSDAQ = '.KQ11'  # 코스닥
FTSE_100_INDEX = '.FTSE'  # financial times stock exchange (영국)
HANG_SENG = '.HSI'  # 항생지수
NEKKEI_225 = '.N225'    # 니케이

ek.get_timeseries(ric.SPX, start_date='2019-01-01')
ek.get_timeseries('SPXe171929100.U', start_date='2019-01-01')

ek.get_data('SPXe171929100.U', ['CF_NAME', ])
ek.get_data('0#AAPL*.U',['CF_LAST','CF_BID','CF_ASK'])
ek.get_data('0#SPX*.U', ['CF_NAME', 'CF_LAST'])
ek.get_timeseries('0#SPX*.U')


ts = ek.get_timeseries('AAPLD181918000.U', start_date='2019-01-01')
ek.get_timeseries('AAPL.O')

ek.get_data('AAPLD181918000.U', ['TR.IMPLIEDVOLATILITY'])
ek.get_data('AAPL.O', ['CNV_OPTION'])
# isins_tickers = ek.get_symbology(rics, from_symbol_type='RIC', to_symbol_type=['ISIN', 'ticker'])

data, err = ek.get_data('APPL.O', ['OPTION_XID'])

