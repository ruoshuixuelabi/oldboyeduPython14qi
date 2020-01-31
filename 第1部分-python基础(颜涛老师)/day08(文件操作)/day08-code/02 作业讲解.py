# 1. 水仙花
# n = input("请输入一个三位数:")  # 156
# s = int(n[0])**3 + int(n[1])**3 + int(n[2]) ** 3
# if int(n) == s:
#     print("是水仙花")
# else:
#     print("不是")

# 2. 冒泡排序
# a = 10
# b = 20
# a, b = b, a

# lst = [88,5,8,6,1,23]
# for a in range(len(lst)):   # 记录内部排序的次数
#     i = 0
#     while i < len(lst) - 1: # 把最大值移动到右端
#         if lst[i] > lst[i+1]:   # 比较,
#             lst[i], lst[i+1] = lst[i+1], lst[i] # 交换
#         i = i + 1
# print(lst)
# c的思想
# x = a
# a = b
# b = x
# print(a, b)

# 3. 36选7
# from random import randint # 我要用随机数. 必须导入这个鬼
# s = set()
# while len(s) < 7:   # 当s集合中的元素的个数小于7的时候. 就去添加
#     s.add(randint(1,36))
# print(s)

# 4.
salary = int(input("工资:"))
if salary <= 2000:
    pass
elif salary <= 4000:
    pass
elif salary <= 6000:
    pass
elif salary <= 10000:
    pass
elif salary > 10000:
    pass

