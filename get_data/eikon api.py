import numpy as np
import pandas as pd
import eikon as ek
import cufflinks as cf
import configparser as cp

# API key로 eikon API접속
ek.set_app_key('030b4f0bb2264404800fcf6743715940204d53a2')

# RIC: reuters instrument code, Data item browser에서 검색하여 찾는다.
rics = [
    'GE',  # general electronic stock
    'AAPL.O',  # apple stock
    '.SPX',  # S&P 500 index
    '.VIX',  # VIX volatility
    'EUR=',  # EUR/USD exchange rate
    'XAU='  # Gold
    'DE10YT=RR'  # 10yr Germany Bond
]

# get time series data
ts = ek.get_timeseries('AAPL.O', start_date='2019-01-01')

# get news headline, date_to를 기준으로 하루치만 가능
nh = ek.get_news_headlines('R:AAPL.O', date_from='2018-01-01', date_to='2018-01-31')

# convert RICs into ISINs(international securities identification numbers) and ticker
isins_tickers = ek.get_symbology(rics, from_symbol_type='RIC', to_symbol_type=['ISIN', 'ticker'])

# other symbol types(ex. SEDOL: stock exchange daily official list) can also be converted to RICs or ISINs
sedols = ['B1YW440', '0673123', 'B02J639', 'B1XZS82', '0045614', '0053673', '0989529', '0216238', '0969703', '0263494']
transed_rics = ek.get_symbology(sedols, from_symbol_type='SEDOL', to_symbol_type=['RIC', 'ISIN'])

# historical data will be retrieved for the following stocks
symbols = ['US0378331005', 'US0231351067', 'US30303M1027', 'US4581401001']
rics = ek.get_symbology(symbols, from_symbol_type='ISIN', to_symbol_type='RIC')
rics = list(rics.RIC.values)
data = ek.get_timeseries(rics,  # the RICs
                         fields='CLOSE',  # close field
                         start_date='2017-10-01',  # start date
                         end_date='2018-01-31')  # end date
# retrieve news headlines for these RICs.
ek.get_news_headlines('R:{}'.format(','.join(rics)),  # the RICs
                      date_from='2018-02-02T20:00:00',  # the starting time
                      date_to='2018-02-02T22:00:00',  # the end time
                      count=20)  # number of headlines

# using ek.get_data() different fields of data shall be retrieved
# get_data(instruments, fields, parameters=None, field_name=False, raw_output=False, debug=False)
# Returns a pandas.DataFrame with fields in columns and instruments as row index
df, err = ek.get_data(rics, ['TR.PriceClose', 'TR.Volume', 'TR.PriceLow', 'TR.TotalReturnYTD', 'TR.TotalReturn52WK'])

# provide access to groups of RICs that have a common association
# for example, the constituent members of the FTSE 100 index or a list of options for a particular underlying contract.
# 0#.FTSE gives you a list of FTSE 100 constituents
# 0#GDAX*.EX gives you a list of all options for all maturities for the DAX index
# 0#GDAXM8*.EX gives you a list of all options for June 2018 maturity for the DAX index
dax = ek.get_data('0#.FTSE', fields=['TR.CommonName', 'TR.PriceClose', 'TR.Volume', 'TR.TotalReturnYTD'])[0]
kospi = ek.get_data('0#.KS11', fields=['TR.Stock Name', 'TR.Last'])
sp = ek.get_data('0#.SPX', fields=['TR.CommonName', 'TR.PriceClose', 'TR.Volume', 'TR.TotalReturnYTD'])[0]

# The eikon package provides the following basic functions to interact with the Eikon Data API and to retrieve data of different types:
# ek.get_symbology(): converting symbology types
# ek.get_data(): retrieve historical data
# ek.get_timeseries(): retrieve historical time series data
# ek.get_news_headlines(): retrieve news headlines
# ek.get_news_story(): retrieve full news texts



# ETF data
etf = ek.get_timeseries('143850.KS', start_date='2019-01-01')
etf.to_csv('Mirea Asset tiger S&P500 futures ETF.csv')
underlying = ek.get_timeseries('ESH9', start_date='2019-01-01')
underlying.to_csv('underlying.csv')
