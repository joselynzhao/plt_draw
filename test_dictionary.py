#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:test_dictionary.py
@TIME:2019/10/2 21:54
@DES:
'''


id_num = {"00":1,"b":234,"aas":32}
for item in id_num:
    id_num[item] = id_num[item] +1

print(id_num)