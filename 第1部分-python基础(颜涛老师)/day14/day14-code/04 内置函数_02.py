# s = "我叫王尼玛"
# print(format(s, "^20"))
# print(format(s, "<20"))
# print(format(s, ">20"))

# print(format(3, 'b' ))   # ⼆进制
# print(format(97, 'c' ))   # 转换成unicode字符
# print(format(11, 'd' ))   # ⼗进制 %d
# print(format(11, 'o' ))   # ⼋进制  8
# print(format(11, 'x' ))   # ⼗六进制(⼩写字⺟)
# print(format(11, 'X' ))   # ⼗六进制(⼤写字⺟)
# print(format(11, 'n' ))   # 和d⼀样
# print(format(11))   # 和d⼀样

# print(format(123456789, 'e' ))   # 科学计数法. 默认保留6位小数
# print(format(123456789, '0.2e' ))   # 科学计数法. 保留2位小数(小写)
# print(format(123456789, '0.2E' ))   # 科学计数法. 保留2位小数(大写)
# print(format(1.23456789, 'f' ))   # 小数点计数法. 保留6位小数
# print(format(1.23456789, '0.2f' ))   # 小数点计数法. 保留2位小数
# print(format(1.23456789, '0.10f'))   # 小数点计数法. 保留10位小数
# print(format(1.23456789e+3, 'F'))   # 小数点计数法. 很大的时候输出 INF

# lst = ["蛋1", "蛋2", "蛋3", "蛋4"]
# for i in range(len(lst)):
#     print(i)
#     print(lst[i])

# for index, el in enumerate(lst, 100):    # 把索引和元素一起获取,索引默认从0开始. 可以更改
#     print(index)
#     print(el)


# print(any([0, "哈哈", "馒头", True]))


lst1 = ["施瓦辛格", "泰达米尔", "阿米尔汗", "威震天"]
lst2 = ["终结者", "英雄联盟", "我的个神啊", "变形金刚"]
lst3 = [10000000, 3, 10, 55,66]
for el in zip(lst1, lst2, lst3):
    print(el)

