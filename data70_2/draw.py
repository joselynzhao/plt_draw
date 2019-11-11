#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:draw.py
@TIME:2019/11/10 11:48
@DES:
'''
'''同监督等饱和度实验 epoch 为 70 計算公式進行了矯正
yita为20'''

from main import  summary_gradually_compare
from data import *
if __name__ == "__main__":
    compare_list = [data20_50,data20_100,data20_200,data20_300,data20_1]
    compare_item = ["mAP", "top1", "label_pre", "select_pre","select_percent"]
    compare_item2 = ["mAP", "top1"]
    summary_gradually_compare(compare_list,compare_item,"result70_2")