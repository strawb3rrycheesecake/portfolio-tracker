#create a porfolio tracker that is able to calculate and plot out time weighted earnings and calculate simple stuff like sharpe-ratios
#for simplicity's sake, i will exclude things like stock splits and dividends first
#first i need to create a df of my current holdings, the current holdings, likely from excel or csv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core.indexes.base import Index
import pandas_datareader.data as web
import datetime as dt
#setting today's date
tdy = dt.date.today().strftime('%Y-%m-%d')
print(tdy)

#importing transactions from excel or csv file
pf = pd.read_excel("test_portfolio.xlsx")

#changing date, bought date, and sold date to datetime format
pf['Bought date'] = pd.to_datetime(pf['Bought date'])
pf['Sold date'] = pd.to_datetime(pf['Sold date'])
pf['End date'] = pd.to_datetime(pf['End date'])
#calculating cost price for each transaction
#I did this in python instead of in the excel sheet as it will mess up the formating when i try to read the file
pf['Cost price'] = pf['Units'] * pf['Bought price']

#i want to be able to iterate through the transaction list and print a plot showing the time-weighted return of a particular stock
#determining end date
def end_date(param):#the param in this case has to be a dataframe consisting of the transactions
    for i in range(len(param.index)):
        if pd.isnull(param['Sold date'][i]) is True:
            param['End date'][i] = tdy
        else:
            param['End date'][i] = param['Sold date'][i]

end_date(pf)
print(pf)

def hold_period(param):
    title = ['Date']
    tick = pf['Ticker'].values.tolist()
    for i in tick:
        title.append(i)

hold_period(pf)

print(pf['Ticker'][0])

swrd = web.DataReader(pf['Ticker'][0], 'yahoo', pf['Bought date'][0], pf['End date'][0])['Adj Close']
swrd = swrd.values.tolist()
print(swrd)