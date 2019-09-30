#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:dynamic_draw.py
@TIME:2019/9/30 10:50
@DES:
'''

from data import  *
import  numpy as np
import matplotlib.pyplot as plt
import  codecs
import  math

# 动态图绘制器
class gif_drawer():
    def __init__(self):
        plt.ion()
        self.xs = [0, 0]
        self.ys = [0, 0]

    def draw(self, update_x, update_y):
        self.xs[0] = self.xs[1]
        self.ys[0] = self.ys[1]

        self.xs[1] = update_x
        self.ys[1] = update_y

        plt.title("Training Accuracy")
        plt.xlabel("iteration")
        plt.ylabel("accuracy")
        plt.plot(self.xs, self.ys, )
        plt.pause(0.1)

