# 2.
# def func(*args):
#     # sum = 0
#     # for el in args:
#     #     sum += el
#     # return sum
#     return sum(args)    # sum() 求和
#
# print(func(1,2,3))

# 3.
# a=10
# b=20
# def test5(a, b):
#         print(a,b)
# c = test5(b,a)
# print(c)


# def wrapper():
#     a = 1
#     def inner():
#         nonlocal  a
#         a += 1
#         print(a)
#     inner()
# wrapper()

# 接收n个参数. 返回最大值和最小值(字典)
# def func(*args):
#     m = args[0] # 假设第0项就是最大值
#     mi = args[0]
#     for el in args:
#         if el > m:
#             m = el # 当前这个元素比假设的那个大. 记录当前这个比较大的数
#         if el < mi:
#             mi = el
#     return {"最大值":m, "最小值":mi}

# print(func(5,7,12,1,46,87,3))

# 12
# def func():
#     yanse = ["红心", "草花","方块","黑桃"]
#     dianshu = ["2","3","4","5","6","A"]
#     result = []
#     for dian in dianshu:
#         for el in yanse:
#             result.append((el, dian))
#     return result


# def wrapper():
#     def inner():
#         print(666)
#     return inner
# wrapper()()

# 如果默认值参数是一个可变的数据类型, 如果有人调用的时候改变了他. 其他位置看到的也跟着改变了
# def extendList(val, list=[]):
#     list.append(val)
#     return list
# list1 = extendList(10)
# print('list1=%s' % list1)   # list = [10]
#
# list2 = extendList(123, [])
# print('list2=%s' % list2)   #
#
# list3 = extendList('a') # list = [10, 'a']
# print('list3=%s' % list3)

# 9*9
a = 1
while a <=9:

    b = 1
    while b <= a:
        print("%dx%d=%d\t" % (a, b, a*b), end="")
        b = b + 1
    print() # 换行
    a = a + 1



# *
# **
# ***
# ****
# *****

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
