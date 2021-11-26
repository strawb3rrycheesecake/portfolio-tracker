#create a porfolio tracker that is able to calculate and plot out time weighted earnings and calculate simple stuff like sharpe-ratios
#for simplicity's sake, i will exclude things like stock splits and dividends first
#first i need to create a df of my current holdings, the current holdings, likely from excel or csv

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime as dt

#importing portfolio from excel or csv file
pf = pd.read_excel("test portfolio.xlsx")

#changing date, bought date, and sold date to datetime format
pf['Date'] = pd.to_datetime(pf['Date'])
pf['Bought date'] = pd.to_datetime(pf['Bought date'])
pf['Sold date'] = pd.to_datetime(pf['Sold date'])

print(pf)
df = web.DataReader('ISRG', 'yahoo', pf['Bought date'][1], pf['Date'][1])
df.index() = pd.to_datetime(df.index())
print(type(df.index()))