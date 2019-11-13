#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:draw.py
@TIME:2019/11/11 10:21
@DES:
'''
'''测试在标签准确率为100%下的 渐进效果， 一次渐进， epoch = 20
step1 ：每次随机选 num_to_select个
step2 ：每次新增 75个，u_data 集越来越少'''

from main import  summary_gradually_compare
from data import *
if __name__ == "__main__":
    compare_list = [supervise_step1,supervise_step2,supervise_step2_ef3, supervise_step2_ef2, supervise20]
    # compare_item = ["mAP", "top1", "label_pre", "select_pre","select_percent"]
    compare_item2 = ["mAP", "top1"]
    summary_gradually_compare(compare_list,compare_item2,"result_supervise_step")