#  1. 列表的增加
# lst = ["周杰伦", "王力宏", "周润发"]
# lst.append("伍佰")    # 向列表中添加一个元素, 元素放在末尾. 把一个元素追加到列表的末尾
# print(lst)
# lst.append("周星星")
# print(lst)]
# lst.insert(1, "马化腾")    # 把元素插入到指定位置. 元素的移动
# print(lst)
# lst.extend(["马云", "王健林", "李嘉诚"])    # 迭代添加
# print(lst)

# lst = []
# while 1:
#     name = input("请输入学生的名字")
#     if name.upper() == "Q":
#         break
#     else:
#         lst.append(name)    # 把名字添加到列表
#
# print(lst)

# 删除
# lst = ["盖伦", "大白梨", "提莫", "大白梨"]

# 1. pop()
# e = lst.pop()   # 返回删除的元素, 删除最后一个
# print(e)
# print(lst)
# e = lst.pop(1)  # 根据给出的索引进行删除
# print(e)
# print(lst)

# 2. remove(元素)
# lst.remove("大白梨")
# lst.remove("大白梨")
# print(lst)

# 3. del 删除 切片删除     delete
# del lst[1:]
# print(lst)

# 4. clear 清空
# lst.clear()
# print(lst)

# 修改
# 索引修改
# lst = ["太白", "五色", "银王", "日天"]
# lst[0] = "太黑"
# print(lst)
# lst[2] = "银角大王"
# print(lst)

# 切片修改
# lst[1:3] = "马化腾"    # 迭代修改
# print(lst)
# lst[1:3] = ["周杰伦", "他媳妇", "王力宏媳妇"]
# print(lst)

# 查询
# lst = ["舒克贝塔", "黑猫警长", "熊大熊二", "葫芦娃", "吴佩琪"]
# for el in lst:  #  element
#     print(el)

# 常用操作
# lst = ["王尼玛", "我记着你", "伟哥", "放学天台见","王尼玛", "王尼玛"]
# print(len(lst))
# print(lst.count("王尼玛"))

lst = [1, 9, 18, 2 , 34, 88, 7, 9]
# lst = ["2王尼玛", "马化腾", "1马云", "马云云", "阿里巴巴", "1王尼玛"]
lst.sort()  # 升序
lst.sort(reverse=True)  # 倒序
print(lst)
list







