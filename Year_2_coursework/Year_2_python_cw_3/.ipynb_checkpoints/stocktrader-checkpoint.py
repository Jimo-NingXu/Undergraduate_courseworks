"""
stocktrader -- A Python module for virtual stock trading
TODO: Add a description of the module...
Also fill out the personal fields below.

Full name: Peter Pan
StudentId: 123456
Email: peter.pan.123@student.manchester.ac.uk
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
    #https://zhuanlan.zhihu.com/p/33030631
  try:
      if "/" or "-" or "." in s:
        t=re.split('[./-]',s,maxsplit=2)
        x=int(t[0])
        y=int(t[1])
        z=int(t[2])
        pattern1=format('%d-%d-%d' %(x, y, z))
        pattern2=format('%d/%d/%d' %(x, y, z))
        pattern3=format('%d.%d.%d' %(x, y, z))
        if len(t[0])==4 and len(t[1])<=2 and len(t[2])<=2:
           if s == pattern1:
              r = format('%04d-%02d-%02d' %(x, y, z))
           elif s == pattern2:
              r = format('%04d-%02d-%02d' %(x, y, z))
        elif len(t[2])==4 and len(t[1])<=2 and len(t[0])<=2:
             if s == pattern3:
                 r = format('%04d-%02d-%02d' %(z, y, x))
        return(r)
  except:
        raise DateError
import csv
def loadStock(symbol):
 try:
    fname=symbol+'.csv'
    with open(fname, newline='') as csvfile:
         symbol={}
         reader = csv.DictReader(csvfile)
         for row in reader:
                 item = symbol.get(row['Date'], dict())
                 item = {k: row[k] for k in ('Open','High','Low','Close','Adj Close','Volume')}
                 symbol[row['Date']] = item
    return symbol
 except:
     raise FileNotFoundError

def loadPortfolio(fname='portfolio.csv'):
    
    return
# TODO: All other functions from the tasks go here

def main():
    # Test your functions here
    return

# the following allows your module to be run as a program
if __name__ == '__main__' or __name__ == 'builtins':
    main()