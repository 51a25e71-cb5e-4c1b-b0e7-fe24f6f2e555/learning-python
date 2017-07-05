# -*- coding: UTF-8 -*-

#通过if...elif...else语句判断数字是正数,负数或零
num = float(input("输入一个数字:"))
if num>0:
    print("正数")
elif num == 0:
    print("零")
else:
    print("负数")

#使用内嵌if语句来实现
if num>= 0:
    if num == 0:
        print("零")
    else:
        print("正数")
else:
    print("负数")