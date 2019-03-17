import eikon as ek
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.api import VAR, DynamicVAR
import matplotlib.pyplot as plt

app_key = pd.read_csv('get_data/app_key.csv')
ek.set_app_key(app_key['app_key'][0])

# get data
start = '1960-01-01'
end = '2200-12-31'
df_chgdp = ek.get_timeseries(['aCNGDP'], start_date=start, end_date=end, interval='quarterly')
df_chequity = ek.get_timeseries(['.SSEC'], start_date=start, end_date=end, interval='monthly')
df_usgdp = ek.get_timeseries(['aUSGDP/A'], start_date=start, end_date=end, interval='quarterly')
df_usequity = ek.get_timeseries(['.NYA'], start_date=start, end_date=end, interval='monthly')
df_krgdp = ek.get_timeseries(['aKRCGDPA'], start_date=start, end_date=end, interval='quarterly')
df_krequity = ek.get_timeseries(['.KS11'], start_date=start, end_date=end, interval='monthly')

# GDP data preprocessing
gdp_rolling_sum_window = 4 * 5

df_chgdp['gdp'] = df_chgdp.rolling(gdp_rolling_sum_window).sum()
df_usgdp['gdp'] = df_usgdp.rolling(gdp_rolling_sum_window).sum()
df_krgdp['gdp'] = df_krgdp.rolling(gdp_rolling_sum_window).sum()

from pandas.tseries.offsets import MonthEnd as pd_MonthEnd

df_chgdp['date'] = df_chgdp.index - pd.DateOffset(months=1) + pd_MonthEnd(0)
df_usgdp['date'] = df_usgdp.index - pd.DateOffset(months=1) + pd_MonthEnd(0)
df_krgdp['date'] = df_krgdp.index - pd.DateOffset(months=1) + pd_MonthEnd(0)

# equity market data preprocessing
df_usequity = df_usequity[['CLOSE']]
df_usequity.index.name = 'date'

df_chequity = df_chequity[['CLOSE']]
df_chequity.index.name = 'date'

df_krequity = df_krequity[['CLOSE']]
df_krequity.index.name = 'date'

# merge GDP and equity
us = pd.merge_asof(df_usequity, df_usgdp, on='date', tolerance=pd.Timedelta(12, unit='M'), direction='nearest')
ch = pd.merge_asof(df_chequity, df_chgdp, on='date', tolerance=pd.Timedelta(12, unit='M'), direction='nearest')
kr = pd.merge_asof(df_krequity, df_krgdp, on='date', tolerance=pd.Timedelta(12, unit='M'), direction='nearest')

us = us.dropna()
ch = ch.dropna()
kr = kr.dropna()

# equity/GDP ratio
us['raw_ratio'] = us['CLOSE'] / us['gdp']
us['mean_ratio'] = us['raw_ratio'].rolling(60).mean()
us['ratio'] = us['raw_ratio'] / us['mean_ratio']

ch['raw_ratio'] = ch['CLOSE'] / ch['gdp']
ch['mean_ratio'] = ch['raw_ratio'].rolling(60).mean()
ch['ratio'] = ch['raw_ratio'] / ch['mean_ratio']

kr['raw_ratio'] = kr['CLOSE'] / kr['gdp']
kr['mean_ratio'] = kr['raw_ratio'].rolling(60).mean()
kr['ratio'] = kr['raw_ratio'] / kr['mean_ratio']

us2 = us[['date', 'ratio']].set_index('date')
ch2 = ch[['date', 'ratio']].set_index('date')
kr2 = kr[['date', 'ratio']].set_index('date')

compare = pd.concat([us2, ch2, kr2],axis=1)
compare.columns = ['us', 'ch', 'kr']
compare = compare.dropna()
compare.plot()
plt.show()