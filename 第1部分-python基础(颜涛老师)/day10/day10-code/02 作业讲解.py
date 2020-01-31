# 2. 写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def func(lst):
#     ll = []
#     for i in range(len(lst)):
#         if i % 2 == 1:
#             ll.append(lst[i])
#     return ll
#
# a = [1, 5, 7, 9, 12]
# ret = func(a)
# print(ret)

# 3, 写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
# def func(a):
#     # if len(a) > 5:
#     #     return True
#     # else:
#     #     return False
#     return len(a) > 5

# 4.
# def func(lst):
#     if len(lst) > 2:
#         return lst[0], lst[1]


# 5.写函数，计算传入函数的字符串中, 数字、字母、空格 以及 其他内容的个数，并返回结果。
# def func(s=""): # function
#     shuzi = 0
#     zimu = 0
#     kongge = 0
#     qita = 0
#     for c in s: # 循环字符串.拿到每个字符
#         if c.isdigit(): # 数字
#             shuzi += 1
#         elif c.isalpha():
#             zimu+=1
#         elif c == ' ':
#             kongge += 1
#         else:
#             qita += 1
#     return shuzi, zimu, kongge, qita

# 6.写函数，接收两个数字参数，返回比较大的那个数字。
# def func(a, b):
#     # if a > b:
#     #     return a
#     # else:
#     #     return b
#     c = a if a > b else b
#     return c
# print(func(3, 5))

# 7. 写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
#
# 	dic = {"k1":"v1", "k2":[11,22]}
# 	PS:字典中的value只能是字符串或列表
#
# def func(dic):
#     new_dic = {}
#     for k, v in dic.items():
#         if len(v) > 2:
#             new_dic[k] = v[0:2]
#         else:
#             new_dic[k] = v
#     return new_dic
# dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# print(func(dic))

# 8.
# def func(lst):
#     dic = {}
#     for i in range(len(lst)):
#         dic[i] = lst[i]
#     return dic


# 9.
# def func(name, age,edu,sex ="男"):
#     f = open("student.msg", mode="a", encoding="utf-8")
#     f.write(name+"_"+str(age)+"_"+sex+"_"+edu+"\n")
#     f.flush()
#     f.close()
#
#
# while 1:
#     content = input("请问. 是否要录入学生信息, 输入q退出:")
#     if content.upper() == "Q":
#         break
#     n = input("请输入名字:")
#     a = input("请输入年龄:")
#     s = input("请输入性别:")
#     e = input("请输入学历:")
#     if s == "":
#         func(n,a,e)
#     else:
#         func(n,a,e,s)

# 10
# import os
# def func(filename, old, new):
#     with open(filename, mode="r", encoding="utf-8") as f1,\
#         open(filename+"_副本", mode="w", encoding="utf-8") as f2:
#
#         for line in f1:
#             s = line.replace(old, new)
#             f2.write(s)
#
#     os.remove(filename)
#     os.rename(filename+"_副本", filename)
#
# func("student.msg", "本", "学")



