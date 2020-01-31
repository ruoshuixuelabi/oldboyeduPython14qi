# def func(i):    # 判断奇数
#     return i % 2 == 1
lst = [1,2,3,4,5,6,7,8,9]

ll = filter(lambda i:i%2==1, lst)
#  第一个参数. 函数. 将第二个参数中的每一个元素传给函数. 函数如果返回True, 留下该元素.
# print("__iter__" in dir(ll))
# print("__next__" in dir(ll))
# print(list(ll))

# lst = [
#         {'id':1, 'name':'alex', 'age':18},
#         {'id':2, 'name':'taibai', 'age':58},
#         {'id':3, 'name':'wusir', 'age':38},
#         {'id':4, 'name':'ritian', 'age':48},
#         {'id':5, 'name':'女神', 'age':18}
#        ]
#
# print(list(filter(lambda dic: dic['age']>40, lst)))



