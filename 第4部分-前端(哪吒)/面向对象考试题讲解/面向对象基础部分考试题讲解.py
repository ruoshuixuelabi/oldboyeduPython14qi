
# 一、斐波那契数列
# 1、斐波那契数列：1, 2, 3, 5, 8, 13, 21.....根据这样的规律，编程求出400万以内最大的斐波那契数，并求出他是第几个斐波那契数。
#                         n1 = 3
#                         n2 = 5
#                         num = n1 + n2
#                         n1 = n2
#                         n2 = n1 + n2
#1、我首先要有前两个数
#第一种：递归
def fib(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    return fib(num - 1) + fib(num - 2)

# print(fib(32))

# flag = 0
# i = 1
# while not flag:
#     if fib(i) > 4000000:
#         flag = 1
#     else:
#         i += 1
#
# print(i,fib(i))
import time
def fib2(num):
    n1 = 1
    n2 = 2
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        for i in range(3,num + 1):#range(3,3)
            n1 , n2 = n2 , n1 + n2
        return n2
front_time = time.time()
fib2(33)
last_time  = time.time()
print('fib2>>>',last_time - front_time)

print('----------------------==============')
front_time = time.time()
fib(33)
last_time  = time.time()
print('fib....',last_time - front_time)







