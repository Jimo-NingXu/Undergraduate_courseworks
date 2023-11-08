"""
stocktrader -- A Python module for virtual stock trading
TODO: Add a description of the module...
Also fill out the personal fields below.
Full name: Ning Xu
StudentId: 10726153
Email: ning.xu-8@student.manchester.ac.uk
"""
class TransactionError(Exception):
    pass

class DateError(Exception):
    pass

stocks = {}
portfolio = {}
transactions = []

import re
def normaliseDate(s):
  """
  Return a date in format Y(length of 4)-M(2)-D(2), if the given date is in three accepted date formats('d.m.y''y-m-d''y/m/d' with d and m have 1 or 2 integers)
  or raise DateError if the date format entered does not match.
  """
  try:
       if "/" or "-" or "." in s:
        t=re.split('[./-]',s,maxsplit=2)#Split the input date,make sure it only has 2 symbols.
        pattern1=t[0]+'/'+t[1]+'/'+t[2] #pattern 1.2.3 are accpted patterns.
        pattern2=t[0]+'-'+t[1]+'-'+t[2]
        pattern3=t[0]+'.'+t[1]+'.'+t[2]
        x=int(t[0])#Store the first/ second/ third element.
        y=int(t[1])
        z=int(t[2])
        if len(t[0])==4 and len(t[1])<=2 and len(t[2])<=2:#In pattern 1 and 2 the format is 4-2-2
           if s == pattern1:
        #The following pattern is learned from https://zhuanlan.zhihu.com/p/33030631
              r = format('%04d-%02d-%02d' %(x, y, z))
           elif s == pattern2:
              r = format('%04d-%02d-%02d' %(x, y, z))
        elif len(t[2])==4 and len(t[1])<=2 and len(t[0])<=2:#In pattern 3, the format is 2-2-4
             if s == pattern3:
                 r = format('%04d-%02d-%02d' %(z, y, x))
        return r
  except:
        raise DateError
        
import pandas as pd
import os
def loadStock(symbol):
    """
    Return=None
    Load individual stock data named fname into stocks, after extracting them from csv file ,(if the fname.csv is not find filenotfounderror will be raised )
    as well as normalising their date(if the test failed DateError will be raised) and ensuring that they only containing floating number(or Valueerror will be raised).
    """
    fname=symbol+'.csv'
    try:
       os.path.exists(fname)==True #Check whether the file is existing.
    except:
         raise FileNotFoundError
    data=pd.read_csv(fname, usecols=[1,2,3,4])#read the date in columes open,high,low,close.
    data1=pd.read_csv(fname,usecols=[0])#read all dates.
    value=data.values.tolist()# Turn them into a list.
    Date=data1['Date'].tolist()
    for i in value:
         for ii in i:
           if isinstance(ii, float)==False:#Make sure the date in columes open,high,low,close is float.
              raise ValueError
    try:
         for i in range(len(Date)):
           t=normaliseDate(Date[i])#Normalise date
           Date[i]=t
    except:
         raise ValueError
    diction=dict(zip(Date,value)) #Use keys and values to make an dictionary.
    stocks[symbol]=diction
    return

import csv
#https://blog.csdn.net/u014535666/article/details/107162141
def loadPortfolio(fname='portfolio.csv'):
 """
 Return=None
 Make a dictionary named portfolio which has data from a csv file(fname=file your want, the default is 'portfolio.csv'), or 
 reporting FileNotFoundError when the file cannot be found and 
 raising valueError when some of the value's format in portfolio is incorrect.
 """
 portfolio.clear() #Make sure portfolio is empty.
 transactions.clear()
 k=["date","cash"]
 t=[]
 try:
       os.path.exists(fname)==True #Try to find the file.
 except:
         raise FileNotFoundError
 with open(fname,'r') as file:
    require=list(csv.reader(file))
    try:
       require[0][0]=normaliseDate(require[0][0])# change the date's format and output as y-m-d
       t.append(require[0][0])
       if float(require[1][0])>=0:#Make sure cash is float number and >0.
           t.append(float(require[1][0]))
       for i in range(2,len(require)): #link individual stock and its volume.
        k.append((require[i][0]))
        loadStock(require[i][0])
        if float(require[i][1]) % 1== 0:#Make sure volume is a integer.
            t.append(int(require[i][1]))
       for i in range(0,len(k)):
        portfolio[k[i]]=t[i] #Put keys and values into dictionary.
    except:
        raise ValueError #If the data in portfolio fail to fit the format above, raise error.

from tabulate import tabulate
def valuatePortfolio(date=None, verbose=False):
    """
    Return the total value of portfolio at a given date(use the date of portfolio if the date is not given)after reading the lowest price from stocks and calculating the total value 
    print the portfolio as a table if verbose=true, otherwise, display the total value of the portfolio.
    """
    #the list(portfolio.values())[1] follow a similar code on
    #https://www.delftstack.com/zh/howto/python/get-first-key-in-dictionary-python/
    t=[]
    v=[]
    ha=["Cash"]
    cash=float(portfolio['cash'])
    total=0
    c=[cash]
    if date is None:
        date=list(portfolio.values())[0]
    else:
        date=normaliseDate(date)
    if date>=normaliseDate(portfolio['date']):
            for i in range(2,len(portfolio)):
             h=list(portfolio.keys())[i] #load stock in portfolio
             ha.append(h)
             loadStock(h)
             if date in stocks[h].keys():
              t.append(stocks[h][date][2]) #read the lowest price 
              v.append(portfolio[h]) #read volume of capital in portfolio
             else:
                 raise DateError
            for i in range(0,len(t)):
             f=float(t[i])*float(v[i])
             total=total+f
            total='{:.2f}'.format(float(total+cash))#let total value be in 2 decimal places.
            if verbose==False:
             print("The total value of our portfolio is £"+ str(total))#Print total value.
            elif verbose==True:
              t.insert(0, cash)
              v.insert(0,1)
              for i in range(1,len(t)):
               c.append(float(t[i])*float(v[i])) 
              ha.append("Total value")
              c.append(total)
              print("Your portfolio on " +date +":")
              print("[* share values based on the lowest price on " + str(date)+"]")
              print(tabulate({'Capital type':ha,'Volume':v,'Val/Unit*':t,'Value in £*':c},headers="keys",floatfmt=(".i", ".2f",".2f",".2f"),tablefmt='rst'))
              return float(total)
    if date<normaliseDate(list(portfolio.values())[0]):
              raise DateError

def addTransaction(trans, verbose=False):
    """
    Print all changes in portfolio if verbose is True and update portfolio information use data in trans like date, value for cash, the number of shares(delete the stock when share=0)
    after each trade has taken place, as well as record every trade and store them into dict(transactions).
    """
    try:
        date=normaliseDate(trans['date'])
    except:
        raise DateError
    if date<portfolio['date']:
        raise DateError
    else:
        if 'symbol' not in trans.keys():
           raise ValueError
        portfolio['date']=trans['date']
        if int(trans['volume'])<0:
            i=2
        elif int(trans['volume'])>0:
            i=1
        change='{:.2f}'.format(float(abs(trans['volume'])*float(stocks[trans['symbol']][trans['date']][i])))
        portfolio['cash']='{:.2f}'.format(float(portfolio['cash'])+float(trans['volume'])*float(stocks[trans['symbol']][trans['date']][i])*(-1))
        transactions.append(trans)
        try: 
            portfolio[trans['symbol']]=int(portfolio[trans['symbol']])+int(trans['volume'])
        except:
            portfolio[trans['symbol']]=int(trans['volume'])
        if portfolio[trans['symbol']]==0:
            del portfolio[trans['symbol']]
        if float(portfolio['cash'])<0:
            raise TransactionError
        else:
            if verbose==False:
                return
            elif verbose==True:
                if int(trans['volume'])>0:
                    print(str(portfolio['date']) + ":" +"Bought " + str(trans['volume'])+" shares of "+ str(trans['symbol']) + " for a total of £"+ str(change),'\n'"Available cash: £"+str(portfolio['cash']) ) 
                elif int(trans['volume'])<0:
                    print(str(portfolio['date']) +":" +"Sold " + str(-1*trans['volume'])+" shares of "+ str(trans['symbol']) + " for a total of £"+ str(change),'\n'"Remaining cash: £"+str(portfolio['cash']) )   
                    
def savePortfolio(fname='portfolio.csv'):
    """
    Save current portfolio into fname.csv(fname is the name of file),which in the same path of stocktrader.py.
    If fname is not given, default it as portfolio.csv.
    """
    with open(fname, 'w', newline="") as csv_file:  
        writer = csv.writer(csv_file)
        for key, value in portfolio.items():
            writer.writerow([key, value])
    return

def sellAll(date=None, verbose=False):
    """
    return=None
    Print all trades when verbose is True(verbose's default is false) after selling all stocks in portfolio at the given date(use the date in portfolio if date is not given . 
    """
    trans={}
    if date is None:
        date=portfolio['date']
    else:
        date=normaliseDate(date)
    trans['date']=date
    while len(portfolio)>2:
        trans['symbol']=list(portfolio.keys())[2]
        trans['volume']=int(list(portfolio.values())[2])*(-1)
        if verbose==True:
            addTransaction(trans,verbose=True) #Print trades.
        elif verbose==False:
            addTransaction(trans,verbose=False)
            return
        
def loadAllStocks():
    """
    Return=None
    Load all stocks in the same path of 'stocktrader.py', skip files if they containg values other than floating number.
    """
    path=os.path.abspath('stocktrader.py')
    path1 = os.path.dirname(path)
    files=os.listdir(path1)
    for file in files:
    #The following code is similar from https://blog.csdn.net/weixin_39616339/article/details/110911428
     file=os.path.splitext(file)[0]
     if file.isupper() == True:
         try:
             loadStock(file)
         except:
             pass
    return

TD=[]
def H(s,j):
    """
    Return the highest price of stock s at given date index j.
    """
    date=TD[j]
    return stocks[s][date][1]
def L(s,k):
    """
    Return the lowest price of stock s at given date index k.
    """
    date=TD[k]
    return stocks[s][date][2]
def Q_buy(s,j):
    """
    Output the ratio,with input company name and a date index number. 
    """
    total=0
    for i in range(0,10):
        total=total+H(s,j-i)
    Q_buy=10*H(s,j)/total
    return (Q_buy)
def Q_sell(s,k,j):
    """
    Output the ratio after calculate the slope of Lowest price of stock and Highest price at the given date index. 
    """
    Q_sell=L(s,k)/ H(s,j)
    return(Q_sell)

def tradeStrategy1(verbose=False):
    """
    Print all transactions when verbose is True. 
    The first purchase start at or after the 10th trading day, use Q_Buy to calculate all stocks' ratio, buy the one with highest ratio, 
    and the next purchase occurs after selling(when Q_sell < 0.7 or Q_sell >1.3).
    """
    s_list=list(stocks.keys()) #All stocks we are interested in.
    #The following code regarding dictionary is similar from https://selflearningsuccess.com/python-dictionary/
    for i in list(stocks.keys()):
       TD.extend(stocks[i].keys()) #Get all trading date store in list.
       break
    try:
       if TD[9]>=portfolio['date']: #Check whether the portfolio date is later than 10th trading day.
           j=9
       else:
            j=TD.index(portfolio['date']) 
    except:
        pass
    while j<= len(TD)-1: #Make sure trade date is in trading date list.
        hl=[]
        trans={}
        for i in range(0,len(s_list)):
            s=s_list[i]
            hl.append(Q_buy(s,j)) #Store all stocks' Q_buy rate.
        comp=s_list[hl.index(max(hl))] #select the stock with the highest rate, when two stocks have same rate, choose the one comes first in stocks.
        trans={'date':TD[j],'symbol':comp,'volume':int(float(portfolio['cash'])//stocks[comp][TD[j]][1])}
        if trans['volume']!=0:
            addTransaction(trans, verbose=True)   
        elif trans['volume']==0: #Donot trade with insufficient amount of money.
            pass 
        for k in range(j+1,len(TD)): #Test through the trade date list to find out the nearest trade day.
            if Q_sell(comp,k,j) < 0.7 or Q_sell(comp,k,j) >1.3:
                trans={"date":TD[k],'symbol':comp,'volume':(-1)*trans['volume']}
                addTransaction(trans, verbose=True) 
                break
        j=k+1 #Allow next round purchase.
    pass
    

# TODO: All other functions from the tasks go here

def main():
    # Test your functions here
    
    return

# the following allows your module to be run as a program
if __name__ == '__main__' or __name__ == 'builtins':
    main()