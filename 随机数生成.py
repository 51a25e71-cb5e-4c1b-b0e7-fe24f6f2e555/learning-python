# -*- coding: UTF-8 -*-

#生成0~9之间的随机数
#导入random模块
import random
import time

#print(random.randint(0,9))
sum = 0
i = 0
n = 1000
while i<n:
    sum = sum + random.randint(0,9)
    i = i + 1

print(sum/n)