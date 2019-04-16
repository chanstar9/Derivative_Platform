import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import eikon as ek
import datetime as dt
from dateutil import relativedelta as rd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
app_key = pd.read_csv('get_data/app_key.csv')
ek.set_app_key(app_key['app_key'][0])

# get US 10Y Note yield
start_date = '1980-01-01'
US10YNoteYTM = ek.get_timeseries('US10YT=RR', start_date=start_date, interval='monthly')['CLOSE']
US2YNoteYTM = ek.get_timeseries('US2YT=RR', start_date=start_date, interval='monthly')['CLOSE']
US3MBillYTM = ek.get_timeseries('US3MT=RR', start_date=start_date, interval='monthly')['CLOSE']

# plot US Treasury 10Y, 3M YTM
fig, ax = plt.subplots()
ax.plot(US10YNoteYTM, label='10Y')
ax.plot(US2YNoteYTM, label='2Y')
ax.plot(US3MBillYTM, label='3M')
ax.set_title("US Treasury Yield")
ax.legend()
plt.show()

# plot US Treasury 10Y, 3M Spread
fig, ax = plt.subplots()
spread_10Y3M = US10YNoteYTM - US3MBillYTM
ax.plot(spread_10Y3M, label='10Y3M Spread')
ax.set_title("Yield spread between 10year, 3month US Treasury")
ax.legend()
plt.show()

# plot yield spread
def get_long_timeseries(ticker, start_date, end_date, interval):
    if type(start_date) == str: start_date = dt.datetime.strptime(start_date, "%Y-%m-%d")
    if type(end_date) == str: end_date = dt.datetime.strptime(end_date, "%Y-%m-%d")
    dates = [start_date] \
            + [start_date + rd.relativedelta(years=10*(x+1)) for x in range((end_date.year - start_date.year)//10)] \
            + [end_date]
    ret = pd.DataFrame()
    for i in range(len(dates)-2):
            ret = ret.append(ek.get_timeseries(ticker, start_date=dates[i],
                                               end_date=dates[i+1]-rd.relativedelta(days=1), interval=interval))
    ret = ret.append(ek.get_timeseries(ticker, start_date=dates[-2], end_date=dates[-1], interval=interval))
    return ret

def df_spread(ticker1, ticker2, start_date, end_date, interval):
    if type(start_date) == str: start_date = dt.datetime.strptime(start_date, "%Y-%m-%d")
    if type(end_date) == str: end_date = dt.datetime.strptime(end_date, "%Y-%m-%d")
    data1 = get_long_timeseries(ticker1, start_date, end_date, interval)['CLOSE']
    data2 = get_long_timeseries(ticker2, start_date, end_date, interval)['CLOSE']
    spread = (data1 - data2).fillna(method='ffill')
    return spread

def plot_spread(ticker1, ticker2, start_date, end_date, interval):
    if type(start_date) == str: start_date = dt.datetime.strptime(start_date, "%Y-%m-%d")
    if type(end_date) == str: end_date = dt.datetime.strptime(end_date, "%Y-%m-%d")
    spread = df_spread(ticker1, ticker2, start_date, end_date, interval)
    fig, ax = plt.subplots(figsize=(16, 6))
    ax.plot(spread, '-', linewidth=0.8)
    ax.plot(spread * 0, 'r-')
    xticks = pd.date_range(str(start_date.year - 1), str(end_date.year), freq='1y').map(lambda x: (x + rd.relativedelta(days=1)))
    xticklabels = xticks.map(lambda x: x.year)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xticklabels)
    delta = rd.relativedelta(months=1)
    ax.set_xlim(start_date - delta, end_date + delta)
    ax.fill_between(spread.index, spread, where=spread < 0, color='r')
    plt.show()

start_date, end_date, interval = "2000-01-01", "2019-04-08", 'daily'
plot_spread('US10YT=RR', 'US3MT=RR', start_date, end_date, interval)
plot_spread('US10YT=RR', 'US2YT=RR', start_date, end_date, interval)
plot_spread('US30YT=RR', 'US10YT=RR', start_date, end_date, interval)

# 10Y-3M, 10Y-2Y, 30Y-1Y 한 번에 그리기
start_date, end_date, interval = "1980-01-01", "2019-04-08", 'daily'
start_date = dt.datetime.strptime(start_date, "%Y-%m-%d")
end_date = dt.datetime.strptime(end_date, "%Y-%m-%d")
spread = pd.DataFrame()
spread['10Y-3M'] = df_spread('US10YT=RR', 'US3MT=RR', start_date, end_date, interval)
spread['10Y-2Y'] = df_spread('US10YT=RR', 'US2YT=RR', start_date, end_date, interval)
spread['30Y-10Y'] = df_spread('US30YT=RR', 'US10YT=RR', start_date, end_date, interval)

fig, axes = plt.subplots(3, figsize=(22, 12))
delta = rd.relativedelta(months=1)
cols = list(spread.keys())
for i in range(3):
    axes[i].plot(spread[cols[i]], linewidth=0.8, label=cols[i])
    axes[i].set_title("US Treasury Yield Spread")
    axes[i].set_ylabel("(%)", rotation=0)
    axes[i].legend(loc='upper center', fontsize=14)
    axes[i].plot(spread[cols[i]]*0, 'r-')
    xticks = pd.date_range(str(start_date.year - 1), str(end_date.year), freq='1y').map(lambda x: (x + rd.relativedelta(days=1)))
    xticklabels = xticks.map(lambda x: x.year)
    axes[i].set_xticks(xticks)
    axes[i].set_xticklabels(xticklabels)
    axes[i].set_xlim(start_date - delta, end_date + delta)
    axes[i].fill_between(spread[cols[i]].index, spread[cols[i]], where=spread[cols[i]] < 0, color='r')
plt.show()

# 비농업취업자수
ticker, start_date, end_date, interval = "USNFAR=ECI", "1980-01-01", "2019-04-08", "monthly"
nonfarm = get_long_timeseries(ticker, start_date, end_date, interval)

fig, ax = plt.subplots()
ax.plot(nonfarm)
plt.show()