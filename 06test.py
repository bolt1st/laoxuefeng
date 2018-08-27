from function06 import my_abs
from def_move import move
from def_quadratic import quadratic
from def_para import product
import math


# a = my_abs(-9)
# print(a)

# r = move(100, 100, 60, math.pi / 6)
# print(r)
# Python的函数返回多值其实就是返回一个tuple

# print(quadratic(2, 3, 1))
#print(product(2, 3, 4))

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')