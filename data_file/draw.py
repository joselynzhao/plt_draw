#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:draw.py
@TIME:2019/11/6 17:11
@DES:
'''
'''同监督等饱和度实验 epoch 为 20'''

from main import  summary_gradually_compare
from data import *

if __name__ == "__main__":
    compare_list = [baohe_100,baohe_200,baohe_300,baohe_400,supervise20,gradually_5_10]
    compare_item = ["mAP", "top1", "label_pre", "select_pre","select_percent","nums_selected"]
    compare_item2 = ["mAP", "top1"]
    summary_gradually_compare(compare_list,compare_item2,"result_compare_with_supervise")


