#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:manage_data.py
@TIME:2019/11/6 11:00
@DES:
'''

import codecs

def init_outf2(file_name):
    f = codecs.open(file_name, 'r', 'utf-8')
    datas = f.readlines()
    step = []
    training = []
    evaluate = []
    estimate = []
    onetime = []
    for line in datas:
        line = line.strip()
        line = line.split(" ")
        for ll in line:
            data = ll.split(":")
            if(data[0]=="step"):
                step.append(int(data[1]))
            if(data[0]=="traning"):
                training.append(float(data[1]))
            if(data[0]=="evaluate"):
                evaluate.append(float(data[1]))
            if(data[0]=="estimate"):
                estimate.append(float(data[1]))
            if(data[0] =="onetime"):
                onetime.append(float(data[1]))
    print("\"step\":{},".format(step))
    print("\"training\":{},".format(training))
    print("\"evaluate\":{},".format(evaluate))
    print("\"estimate\":{},".format(estimate))
    print("\"onetime\":{},".format(onetime))
    alltime = 0.0
    for one in onetime:
        alltime = alltime+one
    print("\"alltime\":{},".format(alltime))
    print("\"name\":\"{}\"".format(file_name.split(".")[0]))

if __name__ =="__main__":
    init_outf2("tesla_8.txt")