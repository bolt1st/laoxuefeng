#!/usr/bin/env python3
# -*- coding: utf-8 -*-

sum0 = 0
n = 1
while n < 101:
    sum0 = sum0 + n
    n = n + 1
print(sum0)

# 请利用循环依次对list中的每个名字打印出Hello, xxx!：
L = ['B', 'L', 'A']
k = 0
while k < 3:
    print('Hello,%s!' % L[k])
    k = k + 1

# 我们想只打印奇数，可以用continue语句跳过某些循环：
m = 0
while m < 10:
    m = m + 1
    if m % 2 == 0:
        continue
    print(m)

