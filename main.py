#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:main.py
@TIME:2019/9/25 20:06
@DES:
'''

from data import  *
import  numpy as np
import matplotlib.pyplot as plt
import  codecs
import  math

def draw_line():
    Nu = 1494
    x = np.linspace(0,50,50)
    p = 0.011
    q = 1.5
    y1 = Nu * x * p

    # for q in np.linspace(1,2,0.2):
    plt.figure(figsize=(12, 6))
    plt.plot(x, Nu * pow(x,1) * 0.05,label="1")
    plt.plot(x,Nu * pow(x,1.5)*0.011,label ="1.5_0.011")
    plt.plot(x,Nu * pow(x,2)*0.0025,label ="2_0.0025")
    # for i in [1.5]:
    #     q = i
    #     y2 = Nu * pow(x, q) * p
    #     plt.plot(x,y2,label=i)

    y3 = -(Nu/2) * np.cos(0.15 *x) + Nu/2
    plt.plot(x,y3,label="cos")


    # plt.plot(x,y1,'b')
    # plt.plot(x,y2,'g')
    plt.axhline(y=Nu,ls="-.",c="r",label="max_Nu")
    # plt.axhspan(x=6,ls="",c="r")

    # plt.xticks(np.arange(0, 144, 12), year)

    plt.xlabel("steps")
    plt.ylabel("select_num")
    plt.xlim(0,22)
    plt.ylim(0, 1600)
    plt.xticks(range(0,22,1))
    plt.legend(loc='lower right')
    plt.savefig("lines_compare")
    plt.show()



def draw_lines_for_one_train(train_name):
    plt.figure(figsize=(12, 6))
    x = np.linspace(1, train_name["length"]+1, train_name["length"])
    plt.plot(x,train_name["mAP"],label="mAP",marker='o')
    mAP_max = np.argmax(train_name["mAP"])
    # plt.plot(mAP_max+2,train_name["mAP"][mAP_max], marker='s')
    plt.annotate(str(train_name["mAP"][mAP_max]), xy=(mAP_max+2, train_name["mAP"][mAP_max]))
    plt.plot(x,train_name["top1"],label="top1",marker='o')
    top1_max = np.argmax(train_name["top1"])
    plt.annotate(str(train_name["top1"][top1_max]), xy=(top1_max + 2, train_name["top1"][top1_max]))
    plt.plot(x,train_name["label_pre"],label="label_pre",marker='o')
    plt.plot(x,train_name["select_pre"],label="select_pre",marker='o')
    plt.xticks(range(1, train_name["length"]+1, 1))
    plt.xlabel("steps")
    plt.ylabel("value(%)")
    plt.title(train_name["title"])
    plt.legend(loc="lower right")
    plt.savefig("each_train/{}".format(train_name["title"]))
    plt.show()


def draw_gradually_compare(compare_list,compare_item):
    plt.figure(figsize=(12, 6))
    max_len = 0
    for train_name in compare_list:
        train_len = train_name["length"]
        if(max_len<train_len):
            max_len = train_len
        max_point = np.argmax(train_name[compare_item])
        if compare_item=="select_pre":
            max_point = np.argmin(train_name[compare_item])
        plt.annotate(str(train_name[compare_item][max_point]), xy=(max_point + 1, train_name[compare_item][max_point]))
        x = np.linspace(1, train_name["length"] , train_name["length"])
        # print(x)
        plt.plot(x,train_name[compare_item],label=train_name["title"],marker='o')
    plt.xticks(range(1, max_len+1, 1))
    plt.xlabel("steps")
    plt.ylabel("value(%)")
    plt.title(compare_item)
    if compare_item =="select_pre":
        plt.legend(loc="upper right")
    else: plt.legend(loc="lower right")
    plt.savefig("compares/{}".format(compare_item))
    plt.show()
    pass
    # draw_mAP


def draw_gradually_percent(compare_item):   #这个函数实现起来确实有难度啊
    plt.figure(figsize=(10, 6))
    x1 = percent_gradually_5_10()
    x2 = percent_gradually_5_13()
    x3 = percent_gradually_5_15()
    x4 = percent_gradually_5_k15()
    x = [x1,x2,x3,x4]
    compare_list = [gradually_5_10,gradually_5_13,gradually_5_15,gradually_5_k15]
    for i in range(len(compare_list)):
        train_name = compare_list[i]
        xx = x[i]
        yy =  train_name[compare_item]
        plt.plot(xx, yy, label=train_name["title"], marker='o')
        max_point = np.argmax(train_name[compare_item])
        if compare_item == "select_pre":
            max_point = np.argmin(train_name[compare_item])
        plt.annotate(str(train_name[compare_item][max_point]), xy=(xx[max_point], train_name[compare_item][max_point]))

    plt.xticks(range(0, 105, 10))
    plt.xlabel("select_num(%)")
    plt.ylabel("value(%)")
    plt.title(compare_item)
    if compare_item!="select_pre":
        plt.legend(loc="upper left")
    else: plt.legend(loc="lower left")
    plt.savefig("compares_percent/{}".format(compare_item))
    plt.show()



def draw_gradually_compare_all():
    compare_list=[gradually_5_10,gradually_5_13,gradually_5_15,gradually_5_k15]
    compare_items = ["mAP","top1","top5","top10","top20","label_pre","select_pre"]
    for item in compare_items:
        draw_gradually_compare(compare_list,item)


def draw_lines_for_all_train():
    train_list = [gradually_5_10, gradually_5_13, gradually_5_15, gradually_5_k15]
    for train_name in train_list:
        draw_lines_for_one_train(train_name)


def draw_gradually_all_percent():
    compare_items = ["mAP", "top1", "top5", "top10", "top20", "label_pre", "select_pre"]
    for items  in compare_items:
        draw_gradually_percent(items)


if __name__ =="__main__":
    pass
    # draw_lines_for_all_train()
    # draw_gradually_compare_all()
    # draw_gradually_all_percent()
    # draw_line()