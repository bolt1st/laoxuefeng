# -*- coding: utf-8 -*-

# 允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积


def product(x, *y):
    sum = x
    for n in y:
        sum = sum * n
    return sum

