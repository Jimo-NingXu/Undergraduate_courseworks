#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 15:06:27 2021

@author: harperning
"""

import pandas as pd
import numpy as np
def loadStock(symbol):
    fname=symbol+'.csv'
    symbol={}
    #https://blog.csdn.net/weixin_40446557/article/details/103372497
    data=pd.read_csv(fname, usecols=[1,2,3,4,5,6])
    data1=pd.read_csv(fname,usecols=[0])
    value=data.value.tolist()
    return(value1)