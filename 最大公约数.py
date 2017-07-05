# -*- coding: UTF-8 -*-

#正序
def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        print(i,end=" ")
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
#倒序
def gcd(a, b):
    if b > a:
        a, b = b, a   # b为最小值
    if a % b == 0:
        return b      # 判断b是否为最大公约数
    for i in range(b//2+1, 1, -1):
        print(i,end=" ")    # 倒序求最大公约数更合理
        if b % i == 0 and a % i == 0:
            return i
    return 0

while(True):
    a = int(input("input 'a':"))
    b = int(input("input 'b':"))

    print(gcd(a,b))