# lst = ["我不是药神", "西游记", "西红柿首富", "天龙八部"]
#
# # lst.clear()
# # list在循环的时候不能删. 因为会改变索引
# del_lst = []
# for el in lst:
#     del_lst.append(el)  # 记录下来要删除的内容
#
# for el in del_lst:  # 循环记录的内容
#     lst.remove(el)  # 删除原来的内容
# print(lst)

# lst = ["周杰伦", "周润发", "周星星", "马化腾", "周树人"]
# 删除掉姓周的人的信息
# del_lst = []
# for el in lst:
#     if el.startswith("周"):
#         del_lst.append(el)
#
# for el in del_lst:
#     lst.remove(el)
# print(lst)

# 字典也不能在循环的时候更改大小
# dic = {"a":"123", "b":"456"}
# for k in dic:
#     dic.setdefault("c", "123")

# a = dict.fromkeys(["jj", 'jay', 'taibai'], "sb")  # 静态方法


# dic = {"a":"123"}
# s = dic.fromkeys("王健林", "思聪" ) # 返回给你一个新字典
# print(s)

