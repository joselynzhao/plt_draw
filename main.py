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
    p = 0.05
    q = 1.5
    y1 = Nu * x * p

    # for q in np.linspace(1,2,0.2):
    plt.figure(figsize=(12, 6))
    for i in [1,1.1,1.2,1.3,1.4,1.5,1.6,1.7]:
        q = i
        y2 = Nu * pow(x, q) * p
        plt.plot(x,y2,label=i)

    y3 = -(Nu/2) * np.cos(0.15 *x) + Nu/2
    plt.plot(x,y3,label="cos")


    # plt.plot(x,y1,'b')
    # plt.plot(x,y2,'g')
    plt.axhline(y=Nu,ls="-.",c="r",label="max_Nu")
    # plt.axhspan(x=6,ls="",c="r")

    # plt.xticks(np.arange(0, 144, 12), year)

    plt.xlabel("steps")
    plt.ylabel("select_num")
    plt.xlim(0, 50)
    plt.ylim(0, 1600)
    plt.xticks(range(0,51,1))
    plt.legend(loc='lower right')
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
    plt.xticks(range(0, train_name["length"]+1, 1))
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
        plt.annotate(str(train_name[compare_item][max_point]), xy=(max_point + 2, train_name[compare_item][max_point]))
        x = np.linspace(1, train_name["length"] , train_name["length"])
        # print(x)
        plt.plot(x,train_name[compare_item],label=train_name["title"],marker='o')
    plt.xticks(range(0, max_len+1, 1))
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


def draw_gradually_compare2(compare_list,compare_item):   #这个函数实现起来确实有难度啊
    plt.figure(figsize=(12, 6))
    max_len = 0
    nu  = 1494.0
    for train_name in compare_list:
        train_len = train_name["length"]
        if(max_len<train_len):
            max_len = train_len
        def change(x):
            return int(nu * math.pow(x,train_name["p"]/10) * 0.05 ) / (nu/100)
        max_point = int(change(np.argmax(train_name[compare_item])))
        min_point = int(change(np.argmin(train_name[compare_item])))
        print( max_point, min_point)
        if compare_item!="select_pre":
            plt.annotate(str(train_name[compare_item][max_point]),
                         xy=(max_point + 2, train_name[compare_item][max_point]))
        else:
            plt.annotate(str(train_name[compare_item][min_point]),
                         xy=(min_point + 2, train_name[compare_item][min_point]))
        x = np.linspace(0, train_name["length"]-1 , train_name["length"])
        num = [0]
        # print(x)
        for i in x[1:]:
            number = change(i)
            num.append(number)
        # print(num)
        plt.plot(num,train_name[compare_item],label=train_name["title"],marker='o')
    plt.xticks(range(0, 100, 15))
    plt.xlabel("select_num(%)")
    plt.ylabel("value(%)")
    plt.title(compare_item)
    plt.legend(loc="lower left")
    plt.savefig("compares_percent/{}".format(compare_item))
    plt.show()


if __name__ =="__main__":
    # draw_line()
    compare_list=[gradually_5_10,gradually_5_13,gradually_5_15]
    draw_gradually_compare(compare_list,"select_pre")
    # draw_lines_for_one_train(gradually_5_15)