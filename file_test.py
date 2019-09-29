
#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@AUTHOR:Joselyn Zhao
@CONTACT:zhaojing17@foxmail.com
@HOME_PAGE:joselynzhao.top
@SOFTWERE:PyCharm
@FILE:file_test.py
@TIME:2019/9/28 20:55
@DES:
'''



if __name__=="__main__":
    file = open("output.txt",'a')
    # file.write("hello")
    #     # file.write(" zhaojing")
    k = 3.43217952749
    print("{:4.1}".format(k))
    file.close()
