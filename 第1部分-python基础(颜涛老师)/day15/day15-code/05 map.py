# lst = [1,2,3,4,5,6,7,8,9,0,23,23,4,52,35,234,234,234,234,234,23,4]
# it = map(lambda i: i * i, lst) # 把可迭代对象中的每一个元素传递给前面的函数进行处理. 处理的结果会返回成迭代器
# print(list(it))


# lst1 = [ 1, 2, 3, 4, 5]
# lst2 = [ 2, 4, 6, 8]
# print(list(map(lambda x, y:x+y, lst1, lst2))) # 如果函数中有多个参数. 后面对应的列表要一一对应
