# li = ["alex", "WuSir", "ritian", "barry", "wenzhou"]
# # li.reverse()
# # # print(li) # 翻转
# s = "qwert"
# li.extend(s)    # 迭代添加
# print(li)



# lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]

# lis[3][2][1][0] = lis[3][2][1][0].upper()
# lis[3][2][1][0] = lis[3][2][1][0].replace("t", "T")
# lis[3][2][1][0] = "TT"

# lis[3][2][1][1] = "100"
# print(lis)
# lis[3][2][1][1] = str(lis[3][2][1][1] + 97)

# int("1l")


# li = ["alex", "eric", "rain"]
# s = ""
# for el in li:
#     s = s + el + "_"
# print(s[:-1])

# li = ["alex", "WuSir", "ritian", "barry", "wenzhou", ""]
#
# for i in range(len(li)):
#     print(i)

# lst = []
# for i in range(1, 101):
#     if i % 2 == 0:
#         lst.append(i)
# print(lst)

# lst = []
# for i in range(50):
#     if i % 3 == 0:
#         lst.append(i)
# print(lst)

# for i in range(100, 0, -1):
#     print(i)

# count = 100
# while count > 0:
#     print(count)
#     count  =  count  - 1

# lst = []
# for i in range(100, 9, -1):
#     if i % 2 == 0:
#         lst.append(i)
#
# new_lst = []
# for el in lst:
#     if el % 4 == 0:
#         new_lst.append(el)
# print(new_lst)

# lst = []
# for i in range(1, 31):
#     lst.append(i)
#
# new_lst = []
# for el in lst:  # index(),
#     if el % 3 == 0:
#         el = "*"
#     new_lst.append(el)
# print(new_lst)

# li = ["TaiBai ", "ale  xC", "AbC   ", "egon", " ri  TiAn", "WuSir", "  aqc"]
# lst = []
# for el in li:
#     el = el.replace(" ", "")
#     if (el.startswith("A") or el.startswith("a")) and el.endswith("c"):
#         lst.append(el)
#

# lst = []
# li = ["苍老师", "东京热", "武藤兰", "波多野结衣"]
# content = input("请输入你的评论:")
# for el in li:
#     if el in content:
#         content = content.replace(el, "*" * len(el))
# lst.append(content)
# print(lst)

# li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
#
# for e in li:
#     if type(e) == list: # 判断e的数据类型
#         for ee in e:
#             if type(ee) == str:
#                 print(ee.lower())
#             else:
#                 print(ee)
#     else:
#         if type(e) == str:
#             print(e.lower())
#         else:
#             print(e)
'''
把班级学生数学考试成绩录入到一个列表中:  并求平均值.  要求:  录入的时候
要带着学生姓名和成绩,  例如:  张三_44
'''
# lst = []
# while 1:
#     stu = input("请输入学生的姓名和成绩(姓名_成绩), 输入Q退出录入:")
#     if stu.upper() == "Q":
#         break
#     lst.append(stu)
#
# # 求平均值
# sum = 0
# for el in lst:
#     li = el.split("_")
#     sum += int(li[1])
#
# print(sum / len(lst))
