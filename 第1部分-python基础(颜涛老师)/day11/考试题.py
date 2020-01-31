# l1=[1,2,3,4,5,6,7,8,9,0]
# l1[1:4] = "abcd"
# print(l1)

# lis = [['k',['qwe',{'k1':['tt',3,'1']},89],'ab']]
# lis[0][1][1]['k1'][1] = str(lis[0][1][1]['k1'][1]+97)
# print(lis)

# for i in range(0, 101, 1):
#     print(100-i)


# 实现一个整数加法计算器：（5分）
# 如：content = input('请输入内容:')  # 如用户输入：5+8+7....(最少	输入两个数相加)，将最后的计算结果添加到此字典中(替换None)：
# dic={'最终计算结果':None}
# content = input('请输入内容:').strip()   # 5+8+7
# lst = content.split("+")
# sum = 0
# for el in lst:
#     sum = sum + int(el.strip())
# dic['最终计算结果'] = sum
# print(dic)

# def main(file_path, *args):
#     s = "_".join(args)
#     f = open(file_path, mode="a", encoding="utf-8")
#     f.write(s)
#     f.flush()
#     f.close()


# def func(lst):
#     new_lst = []
#     for i in range(len(lst)):
#         new_lst.append(lst[i] + str(i))
#     return new_lst

# 有文件t1.txt里面的内容为：（6分）
#   1,alex,22,13651054608,IT
# 	2,wusir,23,13304320533,Tearcher
# 	3,taibai,18,1333235322,IT
# 利用文件操作，将其构造成如下数据类型。
# [{'id':'1','name':'alex','age':'22','phone':'13651054608','	 		'job':'IT'},......]
# result = []
# with open("t1.txt", encoding="UTF-8") as f:
#     # 读取每一行数据
#     for line in f:
#         dic = {}
#         lst = line.split(",")
#         dic["id"] = lst[0].strip()
#         dic['name'] = lst[1].strip()
#         dic['age'] = lst[2].strip()
#         dic['phone'] = lst[3].strip()
#         dic['job'] = lst[4].strip()
#         result.append(dic)
# print(result)

#
# li = [11,22,33,44,55,77,88,99,90]
# result = {}
# for row in li:
#     if row < 66:
#         l = result.get("k1")    # 上来就拿k1
#         if l == None:   # k1不存在. 没有这个列表
#             result["k1"] = [row]    # 创建一个列表扔进去
#         else:   # k1如果存在
#             result['k1'].append(row)    # 追加内容
#     else:
#         l = result.get("k2")  # 上来就拿k1
#         if l == None:  # k1不存在. 没有这个列表
#             result["k2"] = [row]  # 创建一个列表扔进去
#         else:  # k1如果存在
#             result['k2'].append(row)  # 追加内容
# print(result)
