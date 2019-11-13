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

from data_prehandle import  *

def draw_line():
    Nu = 1494
    x = np.linspace(0,50,50)
    p = 0.011
    q = 1.5
    y1 = Nu * x * p

    # for q in np.linspace(1,2,0.2):
    plt.figure(figsize=(8, 6), dpi=300)
    plt.plot(x, Nu * pow(x, 0.5) * 0.05, label="0.5")
    plt.plot(x, Nu * pow(x, 0.8) * 0.05, label="0.8")
    plt.plot(x, Nu * pow(x,1) * 0.05,label="1")
    plt.plot(x, Nu * pow(x,1.3) * 0.05,label="1.3")
    plt.plot(x, Nu * pow(x,1.5) * 0.05,label="1.5")
    # plt.plot(x,Nu * pow(x,1.5)*0.011,label ="1.5_0.011")
    # plt.plot(x, Nu * pow(x, 2.5) * 0.00055, label="2.5_0.0025")
    # plt.plot(x, Nu * pow(x, 0.5) * 0.223, label="0.5_0.223")
    # plt.plot(x, Nu * pow(x, 0.4) * 0.3, label="0.4_0.3")
    # for i in [1.5]:
    #     q = i2
    #     y2 = Nu * pow(x, q) * p
    #     plt.plot(x,y2,label=i)

    y3 = -(Nu/2) * np.cos(0.15 *x) + Nu/2
    y4 = Nu * pow(x,1) * 0.05 -y3
    # plt.plot(x,y3,label="cos")
    # plt.plot(x,y4,label="-cos")


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
    plt.title("gradually")
    plt.legend(loc='lower right')
    plt.savefig("lines_compare/gradually—5",bbox_inches='tight')
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
    plt.plot(x,train_name["train_pre"],label="train_pre",marker ="o")
    plt.plot(x,train_name["select_percent"],label="select_percent",marker ="o")
    # plt.plot(x,train_name["select_num"],label="select_num",marker ="o")
    plt.xticks(range(1, train_name["length"]+1, 1))
    plt.xlabel("steps")
    plt.ylabel("value(%)")
    plt.title(train_name["title"])
    plt.legend(loc="lower right")
    plt.savefig("each_train/{}".format(train_name["title"]))
    plt.show()


def draw_lines_for_one_train2(train_name):
    plt.figure(figsize=(12, 6))
    x = train_name["select_percent"]
    plt.plot(x,train_name["mAP"],label="mAP",marker='o')
    mAP_max = np.argmax(train_name["mAP"])
    # plt.plot(mAP_max+2,train_name["mAP"][mAP_max], marker='s')
    plt.annotate(str(train_name["mAP"][mAP_max]), xy=(x[mAP_max], train_name["mAP"][mAP_max]))
    plt.plot(x,train_name["top1"],label="top1",marker='o')
    top1_max = np.argmax(train_name["top1"])
    plt.annotate(str(train_name["top1"][top1_max]), xy=(x[top1_max], train_name["top1"][top1_max]))
    plt.plot(x,train_name["label_pre"],label="label_pre",marker='o')
    plt.plot(x,train_name["select_pre"],label="select_pre",marker='o')
    plt.plot(x,train_name["train_pre"],label="train_pre",marker ="o")
    plt.xticks(range(0, 105, 10))
    plt.xlabel("select_percent(%)")
    plt.ylabel("value(%)")
    plt.title(train_name["title"])
    plt.legend(loc="lower right")
    plt.savefig("each_train_percent/{}".format(train_name["title"]))
    plt.show()


'''将所有的train的结果都汇合到一张图上面  x = select_num'''
def draw_trains_in_one_graph1():
    train_list = [gradually_5_10, gradually_5_13, gradually_5_15, gradually_5_k15,gradually_11_15,gradually_55_25,gradually_223_05,gradually_30_04,AP_bs_50,EF_5_q_1pro,EF_5_q_1pro2]
    train_list = [gradually_5_10, gradually_5_13, gradually_5_15]
    train_list = [gradually_5_10,AP_bs_50]
    train_list = [gradually_5_10,EF_5_q_1pro,EF_5_q_1pro2]
    train_list = [gradually_5_10, gradually_5_k15, gradually_11_15, gradually_55_25,gradually_223_05, gradually_30_04]
    len_list = len(train_list)
    raw = math.floor(pow(len_list,0.5))
    col = math.ceil(len_list/raw)
    print("col:{} , raw:{}".format(col,raw))
    unit_size = 4.5
    plt.figure(figsize=(4*unit_size, 2 * unit_size),dpi = 100)
    plt.subplots_adjust( hspace=0.5)  # 调整子图间距
    for i in range(len_list):
        train_name = train_list[i]
        # ax = fig.add_subplot()
        plt.subplot(raw,col,i+1)
        x = train_name["select_percent"]
        plt.plot(x, train_name["mAP"], label="mAP", marker='o')
        mAP_max = np.argmax(train_name["mAP"])
        # plt.plot(mAP_max+2,train_name["mAP"][mAP_max], marker='s')
        plt.annotate(str(train_name["mAP"][mAP_max]), xy=(x[mAP_max], train_name["mAP"][mAP_max]))
        plt.plot(x, train_name["top1"], label="top1", marker='o')
        top1_max = np.argmax(train_name["top1"])
        plt.annotate(str(train_name["top1"][top1_max]), xy=(x[top1_max], train_name["top1"][top1_max]))
        plt.plot(x, train_name["label_pre"], label="label_pre", marker='o')
        plt.plot(x, train_name["select_pre"], label="select_pre", marker='o')
        plt.plot(x, train_name["train_pre"], label="train_pre", marker="o")
        # plt.plot(x,train_name["select_num"],label="select_num",marker ="o")
        plt.xticks(range(0, 105, 10))
        plt.xlabel("select_percent(%)")
        plt.ylabel("value(%)")
        plt.title(train_name["title"])
        if i == 0:
            # plt.legend(loc='center', bbox_to_anchor=(1.6,1.3), ncol=6) #all
            plt.legend(loc='center', bbox_to_anchor=(1.6, 1.2), ncol=6)  # 1 CP
            # plt.legend(loc='center', bbox_to_anchor=(1.2, 1.2), ncol=6)  # AP
    # plt.suptitle("all_train", fontsize="20")
    plt.savefig("each_train_percent/summary_percent_ES",bbox_inches='tight')

'''将所有的train的结果都汇合到一张图上面   x = step'''
def draw_trains_in_one_graph2():
    train_list = [gradually_5_10, gradually_5_13, gradually_5_15, gradually_5_k15,gradually_11_15,gradually_55_25,gradually_223_05,gradually_30_04,AP_bs_50,EF_5_q_1pro,EF_5_q_1pro2]
    train_list = [gradually_5_10, gradually_5_13, gradually_5_15]
    train_list = [gradually_5_10, AP_bs_50]
    train_list = [gradually_5_10, EF_5_q_1pro, EF_5_q_1pro2]
    train_list = [gradually_5_10, gradually_5_k15, gradually_11_15, gradually_55_25, gradually_223_05, gradually_30_04]
    len_list = len(train_list)
    raw = math.floor(pow(len_list,0.5))
    col = math.ceil(len_list/raw)
    print("col:{} , raw:{}".format(col,raw))
    unit_size = 4.5
    plt.figure(figsize=(4*unit_size,2 * unit_size),dpi = 100)
    plt.subplots_adjust( hspace=0.5)  # 调整子图间距
    for i in range(len_list):
        train_name = train_list[i]
        # ax = fig.add_subplot()
        plt.subplot(raw,col,i+1)
        x = np.linspace(1, train_name["length"]+1, train_name["length"])
        plt.plot(x, train_name["mAP"], label="mAP", marker='o')
        mAP_max = np.argmax(train_name["mAP"])
        # plt.plot(mAP_max+2,train_name["mAP"][mAP_max], marker='s')
        plt.annotate(str(train_name["mAP"][mAP_max]), xy=(x[mAP_max], train_name["mAP"][mAP_max]))
        plt.plot(x, train_name["top1"], label="top1", marker='o')
        top1_max = np.argmax(train_name["top1"])
        plt.annotate(str(train_name["top1"][top1_max]), xy=(x[top1_max], train_name["top1"][top1_max]))
        plt.plot(x, train_name["label_pre"], label="label_pre", marker='o')
        plt.plot(x, train_name["select_pre"], label="select_pre", marker='o')
        plt.plot(x, train_name["train_pre"], label="train_pre", marker="o")
        plt.plot(x,train_name["select_percent"],label="select_percent",marker ="o")
        plt.xticks(range(1, train_name["length"]+1, round(train_name["length"]/10)))
        plt.xlabel("steps")
        plt.ylabel("value(%)")
        plt.title(train_name["title"])
        if i == 0:
            # plt.legend(loc='center', bbox_to_anchor=(1.6,1.3), ncol=6) #all
            plt.legend(loc='center', bbox_to_anchor=(1.6,1.2), ncol=6) #1
            # plt.legend(loc='center', bbox_to_anchor=(1.2,1.2), ncol=6) #AP
    # plt.suptitle("all_train", fontsize="20")
    plt.savefig("each_train_percent/summary_step_ES",bbox_inches='tight')


'''将对比对象的各个指标拼到一张图上  x = step'''
def summary_gradually_compare(compare_list,compare_item,save_path): #compare_item 是一个item 的list
    len_list = len(compare_item) # 有多少的item 就有多少张子图
    raw  = math.floor(pow(len_list,0.5))
    col = math.ceil(len_list/raw)
    print("col:{} , raw:{}".format(col, raw))
    unit_size = 5
    plt.figure(figsize=(4 * unit_size, 2 * unit_size), dpi=100)
    plt.subplots_adjust(hspace=0.3)  # 调整子图间距
    for i in range(len_list): #遍历每一个item
        plt.subplot(raw, col, i + 1)
        item  = compare_item[i]
        max_len = 0
        for train_name in compare_list:
            train_len = train_name["length"]
            if(max_len<train_len):
                max_len = train_len
            max_point = np.argmax(train_name[item])
            # if item in ["select_pre","train_pre"]:
            #     max_point = np.argmin(train_name[item])
            plt.annotate(str(train_name[item][max_point]), xy=(max_point + 1, train_name[item][max_point]))
            x = np.linspace(1, train_name["length"] , train_name["length"])
            plt.plot(x,train_name[item],label=train_name["title"],marker='o')
        plt.xticks(range(1, max_len+1, round(max_len/10)))
        plt.xlabel("steps")
        plt.ylabel("value(%)")
        plt.title(item)
        if i == 1:
            # plt.legend(loc="best")
            plt.legend(loc='center', bbox_to_anchor=(0.5, 1.2), ncol=len(compare_list))  # 1
        # if compare_item in ["select_pre","train_pre"]:
        #     plt.legend(loc="upper right")
        # else: plt.legend(loc="lower right")
    plt.savefig(save_path,bbox_inches="tight")
    plt.show()


def draw_gradually_compare(compare_list,compare_item):
    plt.figure(figsize=(12, 6))
    max_len = 0
    for train_name in compare_list:
        train_len = train_name["length"]
        if(max_len<train_len):
            max_len = train_len
        max_point = np.argmax(train_name[compare_item])
        if compare_item in ["select_pre","train_pre"]:
            max_point = np.argmin(train_name[compare_item])
        plt.annotate(str(train_name[compare_item][max_point]), xy=(max_point + 1, train_name[compare_item][max_point]))
        x = np.linspace(1, train_name["length"] , train_name["length"])
        # print(x)
        plt.plot(x,train_name[compare_item],label=train_name["title"],marker='o')
    plt.xticks(range(1, max_len+1, 1))
    plt.xlabel("steps")
    plt.ylabel("value(%)")
    plt.title(compare_item)
    if compare_item in ["select_pre","train_pre"]:
        plt.legend(loc="upper right")
    else: plt.legend(loc="lower right")
    plt.savefig("compares/equalstep-{}".format(compare_item))
    plt.show()

    # draw_mAP



'''将对比对象的各个指标拼到一张图上  x = select_percent'''
def summary_gradually_percent(compare_list,compare_item):
    len_list = len(compare_item)  # 有多少的item 就有多少张子图
    raw = math.floor(pow(len_list, 0.5))
    col = math.ceil(len_list / raw)
    print("col:{} , raw:{}".format(col, raw))
    unit_size = 4.5
    plt.figure(figsize=(4 * unit_size, 2 * unit_size), dpi=100)
    plt.subplots_adjust(hspace=0.3)  # 调整子图间距
    for i in range(len_list):
        plt.subplot(raw, col, i + 1)
        item = compare_item[i]
        for train_name in compare_list:
            xx = train_name["select_percent"]
            yy = train_name[item]
            plt.plot(xx, yy, label=train_name["title"], marker='o')
            max_point = np.argmax(train_name[item])
            if item in [ "select_pre","train_pre"] :
                max_point = np.argmin(train_name[item])
            plt.annotate(str(train_name[item][max_point]), xy=(xx[max_point], train_name[item][max_point]))
        plt.xticks(range(0, 105, 10))
        plt.xlabel("select_num(%)")
        plt.ylabel("value(%)")
        plt.title(item)
        if i ==1 :
            plt.legend(loc='center', bbox_to_anchor=(0.5, 1.2), ncol=len(compare_list))  # 1
    plt.savefig("compares_percent/summary_percent_ESnorm",bbox_inches="tight")
    plt.show()

def draw_gradually_percent2(compare_list,compare_item):   #这个函数实现起来确实有难度啊
    plt.figure(figsize=(10, 6))
    for train_name in compare_list:
        xx = train_name["select_percent"]
        yy = train_name[compare_item]
        plt.plot(xx, yy, label=train_name["title"], marker='o')
        max_point = np.argmax(train_name[compare_item])
        if compare_item in [ "select_pre","train_pre"] :
            max_point = np.argmin(train_name[compare_item])
        plt.annotate(str(train_name[compare_item][max_point]), xy=(xx[max_point], train_name[compare_item][max_point]))

    linex=np.linspace(0,100,101)
    liney=np.linspace(0,100,101)
    # plt.plot(linex,liney,ls='-.',label ="diagonal")
    plt.xticks(range(0, 105, 10))
    plt.xlabel("select_num(%)")
    plt.ylabel("value(%)")
    plt.title(compare_item)
    if compare_item not in ["select_pre","train_pre"]:
        plt.legend(loc="upper left")
    else: plt.legend(loc="lower left")
    plt.savefig("compares_percent/ef_5_q_10-{}".format(compare_item))
    plt.show()


def draw_gradually_compare_all():
    compare_list=[gradually_5_10,gradually_5_13,gradually_5_15,gradually_5_k15]
    compare_list2 = [gradually_5_10, gradually_5_k15, gradually_11_15, gradually_55_25, gradually_223_05,gradually_30_04]
    compare_items = ["mAP","top1","top5","top10","top20","label_pre","select_pre"]
    compare_items2 = ["mAP", "top1", "top5", "top10", "top20", "label_pre", "select_pre", "train_pre"]
    for item in compare_items2:
        draw_gradually_compare(compare_list2,item)


def draw_lines_for_all_train():
    train_list = [gradually_5_10, gradually_5_13, gradually_5_15, gradually_5_k15,gradually_11_15,gradually_55_25,gradually_223_05,gradually_30_04,AP_bs_50,EF_5_q_1pro,EF_5_q_1pro2]
    for train_name in train_list:
        draw_lines_for_one_train2(train_name)


# def draw_gradually_all_percent():
#     compare_items = ["mAP", "top1", "top5", "top10", "top20", "label_pre", "select_pre"]
#     for items  in compare_items:
#         draw_gradually_percent(items)

def draw_gradually_all_percent2():
    compare_items = ["mAP", "top1", "label_pre", "select_pre","train_pre"]
    compare_list1 = [gradually_5_10,gradually_5_13,gradually_5_15]
    compare_list2 = [gradually_5_10,gradually_5_k15,gradually_11_15,gradually_55_25,gradually_223_05,AP_bs_50]
    compare_list3 = [EF_5_q_1pro,EF_5_q_1pro2,gradually_5_10]
    for items  in compare_items:
        draw_gradually_percent2(compare_list3,items)


def select_pre_with_mAP(train_name):
    title = train_name["title"]
    xx = train_name["mAP"]
    yy = train_name["select_pre"]
    plt.figure(figsize=(10, 6))
    plt.plot(xx, yy, label="diagonal")
    plt.xticks(range(int(xx[0])-5, int(xx[-1])+5, 10))
    plt.xlabel("mAP(%)")
    plt.ylabel("select_pre(%)")
    plt.title(title)
    plt.savefig("select_pre_with_mAP/"+title)
    plt.show()

def select_pre_with_mAP_for_all():
    compare_list = [gradually_5_10, gradually_5_13, gradually_5_15, gradually_5_k15]
    plt.figure(figsize=(10, 6))
    for train_name in compare_list:
        xx = train_name["mAP"]
        yy = train_name["label_pre"]
        plt.plot(xx, yy, label=train_name["title"])
    # plt.xticks(range(20, 70, 10))
    plt.xlabel("mAP(%)")
    plt.ylabel("label_pre(%)")
    plt.title("label_pre with mAP")
    plt.savefig("label_pre_with_mAP")
    plt.show()


def select_pre_with_mAPtop1(train_name):
    title = train_name["title"]
    xx = train_name["mAP"]
    xxx = train_name["top1"]
    yy = train_name["select_pre"]
    plt.figure(figsize=(10, 6))
    plt.plot(xx, yy, label="with mAP")
    plt.plot(xxx, yy, label="with top1")
    plt.xticks(range(int(min(xx[0],xxx[0]))-5, int(max(xx[-1],xxx[-1]))+5, 10))
    plt.xlabel("mAP or top1(%)")
    plt.ylabel("select_pre(%)")
    plt.title(title)
    plt.savefig("select_pre_with_mAPtop1/"+title)
    plt.show()

import  codecs
def init_outf(file_name):
    f = codecs.open(file_name, 'r', 'utf-8')
    datas = f.readlines()
    steps = []
    mPAs = []
    top1s = []
    top5s = []
    top10s = []
    top20s = []
    label_pres = []
    select_pres = []
    for line in datas:
        line = line.strip()
        ll = line.split(" ")
        step =int(ll[0].split('/')[0] )
        steps.append(step)

        mPA = round(float(ll[2][:-1]),1)
        top1 = round(float(ll[10][:-1]),1)
        top5 = round(float(ll[18][:-1]),1)
        top10 = round(float(ll[26][:-1]),1)
        top20 = round(float(ll[34][:-1]),1)
        label_pre = round(float(ll[37])*100,1)
        select_pre = round(float(ll[40])*100,2)

        mPAs.append(mPA)
        top1s.append(top1)
        top5s.append(top5)
        top10s.append(top10)
        top20s.append(top20)
        label_pres.append(label_pre)
        select_pres.append(select_pre)
    print(steps)
    print(mPAs)
    print(top1s)
    print(top5s)
    print(top10s)
    print(top20s)
    print(label_pres)
    print(select_pres)


def init_outf2(file_name):
    f = codecs.open(file_name, 'r', 'utf-8')
    datas = f.readlines()
    step = []
    mAP = []
    top1 = []
    nums_selected = []
    select_percent = []
    label_pres = []
    select_pres = []
    for line in datas:
        line = line.strip()
        line = line.split(" ")
        for ll in line:
            data = ll.split(":")
            if(data[0]=="step"):
                step.append(int(data[1]))
            if(data[0]=="top1"):
                top1.append(round(float(data[1][:-1]),2))
            if(data[0]=="nums_selected"):
                nums_selected.append(int(data[1]))
            if(data[0]=="selected_percent"):
                select_percent.append(round(float(data[1][:-1]),2))
            if(data[0] =="mAP"):
                mAP.append(round(float(data[1][:-1]),2))
            if(data[0]=="label_pre"):
                label_pres.append(round(float(data[1][:-1]),2))
            if(data[0] =="select_pre"):
                select_pres.append(round(float(data[1][:-1]),2))

    print("\"step\":{},".format(step))
    print("\"top1\":{},".format(top1))
    print("\"mAP\":{},".format(mAP))
    print("\"nums_selected\":{},".format(nums_selected))
    print("\"select_percent\":{},".format(select_percent))
    print("\"label_pre\":{},".format(label_pres))
    print("\"select_pre\":{},".format(select_pres))
    print("\"length\":{},".format(step[-1]+1))
    print("\"title\":\"{}\"".format(file_name.split("/")[-1].split(".")[0]))


def summary_compare():
    train_list1 = [gradually_5_10, gradually_5_13, gradually_5_15]
    train_list2 = [gradually_5_10, AP_bs_50]
    train_list3 = [gradually_5_10, EF_5_q_1pro, EF_5_q_1pro2]
    train_list4 = [gradually_5_10, gradually_5_k15, gradually_11_15, gradually_55_25, gradually_223_05, gradually_30_04]
    train_list5 = [EF70_11_15,EF70_50_10,EF70_223_05]
    train_list6 = [gradually_5_10,EFnorm_50_10]
    compare_items = ["mAP", "top1", "label_pre", "select_pre","train_pre"]
    summary_gradually_compare(train_list6,compare_items)
    summary_gradually_percent(train_list6,compare_items)

if __name__ =="__main__":
    # pass
    # draw_lines_for_all_train()
    # draw_gradually_compare_all()
    # draw_trains_in_one_graph1()
    # draw_trains_in_one_graph2()
    # draw_gradually_compare_all()
    # draw_gradually_all_percent2
    init_outf2("supervise_step/data_step2-ef3.txt")


    # draw_gradually_compare_all()
    # draw_line()
    # select_pre_with_mAP_for_all()
    # draw_lines_for_one_train(EF_10_q_1pro)

    # summary_compare()

