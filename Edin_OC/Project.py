#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pandas-datareader


# In[2]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm


# In[3]:


pip install yfinance --upgrade --no-cache-dir


# In[4]:


import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import yfinance as yf
import time
from yahoofinancials import YahooFinancials


# In[5]:


pip install yahoofinancials


# In[6]:


def calculate_returns(s):
    for i in s:
        data = yf.download(s, start="2002-1-30", end="2021-1-30")
        returns=(data['Close']/data['Close'].shift(1))-1
        re=returns.resample('M').mean()
        re.dropna(axis=0,how="any")
        return(re)
portfolio=["^GSPC","^IXIC","^GDAXI"]
calculate_returns(portfolio)


# In[7]:


def calculate_risks(s):
    for i in s:
        data = yf.download(s, start="2002-1-30", end="2021-1-30")
        returns=(data['Close']/data['Close'].shift(1))-1
        re=returns.resample('M').std().dropna(axis=0,how="any")
        return(re)
portfolio=["^GSPC","^IXIC","^GDAXI","ZF=F"]
calculate_risks(portfolio)


# In[8]:


def calculate_EXCEED_returns(s):
    tr=calculate_returns(s)
    rf=calculate_returns("^TNX")
    risk_pri=tr-rf
    return(risk_pri)
portfolio=["^GSPC","^IXIC","^GDAXI","ZF=F"]
calculate_EXCEED_returns("AAPL")


# In[9]:


BETA={}
def Beta_regression(portfolio,verbose=None):
    X=calculate_EXCEED_returns("^GSPC") #计算 Excess！！
    xbar = sum(X)/len(X)
    n = len(X)
    for i in portfolio:
        Y=calculate_EXCEED_returns(i)
        ybar = sum(Y)/len(Y)
        numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
        denum = sum([xi**2 for xi in X]) - n * xbar**2
        beta = numer / denum
        alpha = ybar - beta * xbar
        yfit = [alpha + beta * xi for xi in X]
        BETA[i]=beta
    if verbose==True:
            plt.plot(X, yfit,'-r',label=portfolio)
            plt.scatter(X,Y)
            plt.axis([-0.03,0.04,-0.03,0.04])
            plt.xlabel("S&P_500_Excess_Return")
            plt.ylabel("Portfolio_Excess_Return")
            plt.legend()
            print('best fit line:\ y = {:.2f} + {:.2f}x'.format(alpha, beta))
    return
portfolio=["AAPL","MRK"]
Beta_regression(portfolio)
BETA


# In[10]:


Expected_re={}
def Expected_returns(portfolio):
    rf=float(calculate_returns("^TNX").mean())
    mkt_pre=float(calculate_EXCEED_returns("^GSPC").mean())
    Beta_regression(portfolio,verbose=None)
    for i in portfolio:
        beta=float(BETA[i])
        er=rf+beta*mkt_pre
        Expected_re[i]=er
    return
portfolio=["^GSPC"]
Expected_returns(portfolio)
Expected_re


# In[11]:


def CML(portfolio):
    return


# In[12]:


def SML(portfolio):
    port=["^GSPC","^TNX"]
    Expected_returns(port)
    MKT=Expected_re["^GSPC"]
    RF=Expected_re["^TNX"]
    Expected_re.clear
    plt.plot([0,1],[RF,MKT],c='blue',ls='-')
    plt.scatter(0,RF,label="Risk_free")
    plt.scatter(1,MKT,label="Market")
    plt.legend()
    Beta_regression(portfolio,verbose=None)
    Expected_returns(portfolio)
    for i in portfolio:
        X=BETA[i]
        Y=Expected_re[i]
        plt.scatter(X,Y,label=i)
        plt.ylabel("Expected_Return")
        plt.xlabel("Beta")
    plt.legend()
    return
portfolio=["AAPL","MRK"]
SML(portfolio)


# In[13]:


def get_balance_sheet(s):
    stock = yf.Ticker(s)
    return stock.balance_sheet
get_balance_sheet('AAPL')


# In[14]:


def get_cashflow(s):
    stock = yf.Ticker(s)
    return stock.cashflow
get_cashflow('AAPL')


# In[15]:


failed_list=[]
def convert2csv(stk_list):
    for i in stk_list:
        try:
            print('processing: ' + i)
            stock = yf.Ticker(i)
            stock.financials.to_csv('profit_loss_account_'+i+'.csv')
            stock.balance_sheet.to_csv('balance_sheet_'+i+'.csv')
            stock.cashflow.to_csv('cash_flow_'+i+'.csv')
            time.sleep(1)
        except :
            failed_list.append(i)
            continue
    return
convert2csv(["AAPL","MRK"])


# In[16]:


tech_stocks = ['AAPL', 'MSFT', 'INTC']
yahoo_financials_tech = YahooFinancials(tech_stocks)
tech_cash_flow_data_an = yahoo_financials_tech.get_financial_stmts('monthly', 'income')


# In[17]:


tech_cash_flow_data_an


# In[18]:


def RF():
    N_DAYS = 90
    df_rf = yf.download('^IRX', start="2019-1-30", end="2021-1-30")
    rf = df_rf.resample('M').last().Close / 100
    rf = (1 / (1 - rf * N_DAYS / 360)) ** (1 / N_DAYS)
    rf = (rf ** 30) - 1
    rf.plot(title='Risk-free rate (13 Week Treasury Bill)')
    return plt.show()


# In[19]:


from yahoofinancials import YahooFinancials
ticker = 'AAPL'
yahoo_financials = YahooFinancials(ticker)
income_statement_data_qt = yahoo_financials.get_financial_stmts('monthly', 'balance')
income_statement_data_qt


# In[84]:


import random
def score_stocks(stock_list):
    #评分系统
    terms=list(stock_list.keys())
    new_index=[]
    index=[]
    i=0
    for i in range(0,len(terms[0])):
        index.append(0)
        new_index.append(0)
        i=i+1
    for elements in terms:
        a=stock_list[elements]
        sorted_id=sorted(range(len(a)),key=lambda k: a[k],reverse=True)
        t=len(sorted_id)
        for g in range(0,len(sorted_id)):
            c=sorted_id[g]
            index[c]=t
            t=t-1
        new_index=[new_index[i]+index[i] for i in range(0,len(index))]
        sorted_id.clear()
    index = [x/len(terms) for x in new_index]
    return(index)


# In[37]:


stock_list={}
def calculate_ROE(s):
    ticker = s
    yahoo_financials = YahooFinancials(ticker)
    income_statement_data_m = yahoo_financials.get_financial_stmts('m', 'balance')
    tA = []
    tL = []
    for i in ticker:
        lst1 = income_statement_data_m['balanceSheetHistoryQuarterly'][i]
        total_assets = []
        total_liability = []
        for j in lst1:
            for k in j.keys():
                k = str(k)
                total_assets.append(j[k]['totalAssets'])
                total_liability.append(j[k]['totalLiab'])
        tA.append(np.mean(total_assets))
        tL.append(np.mean(total_liability))
        income = yahoo_financials.get_net_income()
        nI = []
        ROE = []
        for i in income.keys():
            i = str(i)
            nI.append(income[i])
        for i in range(len(tA)):
            ROE.append(nI[i] / (tA[i] - tL[i]))
    stock_list['ROE']=ROE
    return ROE
calculate_ROE(['AAPL','PG','AMZN'])


# In[38]:


def EPS(ticker):
    EPS=[]
    for i in ticker:
        yahoo_financials = YahooFinancials(i)
        t= yahoo_financials.get_earnings_per_share()
        EPS.append(t)
    stock_list['EPS']=EPS
    return EPS
EPS(['AAPL','PG','AMZN'])
stock_list


# In[85]:


score_stocks(stock_list)


# In[50]:


def calculate_forward_EPS(tickers):
    forward_EPS = []
    for i in tickers:
        yf = YahooFinancials(i)
        forward_EPS.append(yf.get_key_statistics_data()[i]['forwardEps'])
    return forward_EPS


# In[ ]:




