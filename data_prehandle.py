#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:data_prehandle.py
@TIME:2019/10/8 14:44
@DES:
'''
from data import *


import  numpy as np
import  math
def get_len(train_name):
    return len(train_name["mAP"])

def percent_gradually_5_k15():
    Nu = 1494.0
    k = 15
    x = np.linspace(1,gradually_5_k15["length"],gradually_5_k15["length"])
    def fun(x):
        num =  min(math.ceil(-(Nu/2) * np.cos((k/100) * (x-1))+(Nu/2)),Nu)
        return round(num)
    xx = list(map(fun,x))
    print("percent_gradually_5_k15",xx)
    return xx
def percent_gradually_5_10():
    Nu = 1494.0
    q = 1.0
    ef = 5
    x = np.linspace(1,gradually_5_10["length"],gradually_5_10["length"])
    def fun(x):
        num =  min(math.ceil(Nu * math.pow(x-1,q)*(ef/100)),Nu)
        return round(num)
    xx = list(map(fun,x))
    print("percent_gradually_5_10",xx)
    return xx
def percent_gradually_5_13():
    Nu = 1494.0
    q = 1.3
    ef = 5
    x = np.linspace(1,gradually_5_13["length"],gradually_5_13["length"])
    def fun(x):
        num =  min(math.ceil(Nu * math.pow(x-1,q)*(ef/100)),Nu)
        return round(num)
    xx = list(map(fun,x))
    print("percent_gradually_5_13",xx)
    return xx
def percent_gradually_5_15():
    Nu = 1494.0
    q = 1.5
    ef = 5
    x = np.linspace(1,gradually_5_15["length"],gradually_5_15["length"])
    def fun(x):
        num =  min(math.ceil(Nu * math.pow(x-1,q)*(ef/100)),Nu)
        return round(num)
    xx = list(map(fun,x))
    print("percent_gradually_5_15",xx)
    return xx
def percent_gradually_11_15():
    Nu = 1494.0
    q = 1.5
    ef = 1.1
    x = np.linspace(1,gradually_11_15["length"],gradually_11_15["length"])
    def fun(x):
        num =  min(math.ceil(Nu * math.pow(x-1,q)*(ef/100)),Nu)
        return round(num)
    xx = list(map(fun,x))
    print("percent_gradually_11_15",xx)
    return xx
def percent_gradually_55_25():
    Nu = 1494.0
    q = 2.5
    ef = 0.055
    x = np.linspace(1,gradually_11_15["length"],gradually_11_15["length"])
    def fun(x):
        num =  min(math.ceil(Nu * math.pow(x-1,q)*(ef/100)),Nu)
        return round(num)
    xx = list(map(fun,x))
    print("percent_gradually_55_25",xx)
    return xx
def percent_gradually_223_05():
    Nu = 1494.0
    q = 0.5
    ef = 22.3
    x = np.linspace(1,gradually_223_05["length"],gradually_223_05["length"])
    def fun(x):
        num =  min(math.ceil(Nu * math.pow(x-1,q)*(ef/100)),Nu)
        return round(num*100/Nu,2)
    xx = list(map(fun,x))
    print("percent_gradually_55_25",xx)
    return xx
def percent_gradually_30_04():
    Nu = 1494.0
    q = 0.4
    ef = 30
    x = np.linspace(1,gradually_30_04["length"],gradually_30_04["length"])
    def fun(x):
        num =  min(math.ceil(Nu * math.pow(x-1,q)*(ef/100)),Nu)
        return round(num*100/Nu,2)
        # return round(num)
    xx = list(map(fun,x))
    print("percent_gradually_30_04",xx)
    return xx

def get_train_pre(train_name):
    Ln=702
    select_pre = train_name["select_pre"]
    select_num = train_name["select_num"]
    def fun(pre,num):
        return round((math.floor(pre*num/100)+Ln)*100/(num+Ln),2)
    train_pre = list(map(fun,select_pre,select_num))
    print(train_name["title"],train_pre)

def get_train_pre_all():
    train_list = [EFnorm_50_10]
    for train_name in train_list:
        get_train_pre(train_name)






if __name__=="__main__":
    # print(get_len(gradually_5_15))
    # percent_gradually_5_k15()
    # get_train_pre(gradually_223_05)
    # percent_gradually_30_04()
    get_train_pre_all()