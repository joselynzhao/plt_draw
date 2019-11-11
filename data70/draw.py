#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:draw.py
@TIME:2019/11/6 17:51
@DES:
'''
'''同监督等饱和度实验 epoch 为 70'''

from main import  summary_gradually_compare
from data import *





if __name__ == "__main__":
    compare_list = [data21_50,data21_100,data21_200,data21_300,EF70_50_10]
    compare_item = ["mAP", "top1", "label_pre", "select_pre","select_percent"]
    compare_item2 = ["mAP", "top1"]
    summary_gradually_compare(compare_list,compare_item,"result70")