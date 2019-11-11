#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:data_summary.py
@TIME:2019/11/6 10:53
@DES:
'''

GPU2080ti={
    "step": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "training": [336.60875, 406.35135, 472.78478, 539.06432, 613.80808, 684.03103, 748.72381, 822.56127, 885.45491,
                 952.49652, 1027.6314],
    "evaluate": [446.54249, 438.68298, 441.46347, 439.90956, 443.08302, 439.72151, 441.10421, 440.59277, 438.93963,
                 442.53716, 437.79857],
    "estimate": [386.68923, 381.22512, 383.0398, 383.44226, 384.61231, 383.50827, 384.01085, 382.6546, 381.98211,
                 381.11715, 381.3774],
    "onetime": [1169.841, 1226.2602, 1297.2888, 1362.417, 1441.5046, 1507.262, 1573.8403, 1645.8101, 1706.3783,
                1776.1525, 1846.8091],
    "alltime": 16553.5639,
    "name":"2080ti"
}
GPUtesla_1={
    "step":[0, 1, 2, 3, 4, 5, 6, 7, 8],
    "training":[301.70493, 339.19007, 406.89485, 464.52635, 534.60119, 593.34493, 647.12007, 704.04125, 761.53045],
    "evaluate":[501.08605, 498.51668, 495.10426, 499.13845, 498.46009, 494.63499, 495.0809, 495.08627, 502.04949],
    "estimate":[428.46669, 427.59908, 422.52134, 424.72719, 423.14119, 425.46325, 426.59451, 424.12448, 423.72771],
    "onetime":[1231.2589, 1265.3073, 1324.5224, 1388.3941, 1456.2048, 1513.4459, 1568.7983, 1623.2551, 1687.3111],
    "alltime":13058.497899999998,
    "name":"tesla_1"
}

GPUtesla_8={
    "step":[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "training":[14.01633, 40.688029, 763.54133, 726.9843, 728.3283, 726.73542, 731.84279, 733.56433, 732.56462, 797.77826, 819.01968],
    "evaluate":[512.33668, 526.91144, 528.20828, 521.55467, 518.15028, 524.64333, 520.22039, 518.55187, 521.96948, 524.68244, 522.89311],
    "estimate":[414.02187, 439.65949, 438.59297, 448.94876, 446.41907, 446.78058, 440.09465, 444.67333, 450.47948, 443.59297, 446.21146],
    "onetime":[940.37626, 1007.2606, 1730.3445, 1697.4896, 1692.9001, 1698.162, 1692.1606, 1696.7923, 1705.0166, 1766.057, 1788.1276],
    "alltime":17414.687159999998,
    "name":"tesla_8"
}

import matplotlib.pyplot as plt
import math
import codecs
import  numpy as np

'''将对比对象的各个指标拼到一张图上  x = step'''
def summary_gradually_compare(compare_list,compare_item): #compare_item 是一个item 的list
    len_list = len(compare_item) # 有多少的item 就有多少张子图
    raw  = math.floor(pow(len_list,0.5))
    col = math.ceil(len_list/raw)
    print("col:{} , raw:{}".format(col, raw))
    unit_size = 4.5
    plt.figure(figsize=(4 * unit_size, 2 * unit_size), dpi=100)
    plt.subplots_adjust(hspace=0.3)  # 调整子图间距
    for i in range(len_list): #遍历每一个item
        plt.subplot(raw, col, i + 1)
        item  = compare_item[i]
        max_len = 0
        for train_name in compare_list:
            train_len = train_name["step"][-1]+1
            if(max_len<train_len):
                max_len = train_len
            max_point = np.argmax(train_name[item])
            # if item in ["select_pre","train_pre"]:
            #     max_point = np.argmin(train_name[item])
            plt.annotate(str(train_name[item][max_point]), xy=(max_point, train_name[item][max_point]))
            x = train_name["step"]
            # x = np.linspace(1, train_name["length"] , train_name["length"])
            plt.plot(x,train_name[item],label=train_name["name"],marker='o')
        plt.xticks(range(1, max_len+1, round(max_len/10)))
        plt.xlabel("steps")
        plt.ylabel("time(seconds)")
        plt.title(item)
        if i == 0:
            # plt.legend(loc="best")
            plt.legend(loc='center', bbox_to_anchor=(0.2, 1.2), ncol=len(compare_list))  # 1
        # if compare_item in ["select_pre","train_pre"]:
        #     plt.legend(loc="upper right")
        # else: plt.legend(loc="lower right")
    plt.savefig("result_picture",bbox_inches="tight")
    plt.show()

if __name__ =="__main__":
    compare_list=[GPU2080ti,GPUtesla_1,GPUtesla_8]
    compare_item = ["training","evaluate","estimate","onetime"]
    summary_gradually_compare(compare_list,compare_item)
    pass