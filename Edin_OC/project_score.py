pip install pandas-datareader
pip install yfinance --upgrade --no-cache-dir
pip install yahoofinancials
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
import yfinance as yf
import time
from yahoofinancials import YahooFinancials
import csv
stock_list={}

def QEG_calculate(tickers):
    #Quarterly Earnings Growth
    #QEG_calculate(['AAPL','PG','AMZN'])
    QEG = []
    failed_list=[]
    for i in tickers:
            yf = YahooFinancials(i)
            QEG.append(yf.get_key_statistics_data()[i]['earningsQuarterlyGrowth'])
    stock_list['QEG']=QEG
    return QEG

def ticker_reader(s):
    ticker = []
    with open(s)as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            ticker.append(row[0])
    return ticker
ticker_reader('name.csv')

def selection(s,verbose=True):
    stocks=[]
    failed_list=[]
    if verbose==True:
        c=ticker_reader(s)
    else:
        c=s
    for a in c:
        try:
            b = QEG_calculate([a])
            b[0]==float
            if b[0]>= 0.25:
                stocks.append(a)
        except:
            failed_list.append(a)
            print(failed_list)
    return stocks

selection('name.csv',True)





