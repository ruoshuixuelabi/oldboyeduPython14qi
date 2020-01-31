# f = open("老师点名", mode="r+", encoding="utf-8") # r+模式, 默认情况下光标在文件的开头, 必须先读, 后写
# f.write("周润发")
# s = f.read()
# f.flush()
# f.close()
# print(s)


# f = open("精品", mode="r+", encoding="utf-8")
# s = f.read(3)
# # 不管你前面读了几个. 后面去写都是在末尾
# # f.write("哈哈")   # 1.在没有任何操作之前进行写. 在开头写  2. 如果读取了一些内容. 再写, 写入的是最后
#
# # print(ss)


f = open("精品", mode="r+", encoding="utf-8")
# f.read(3)
# f.seek(3)   # 移动到xx位置
# 移动到开头: f.seek(0)  开头
# 移动到末尾: f.seek(0, 2)   末尾 第二个参数有三个值. 0: 再开头,  1: 在当前, 2: 末尾

#超人的都是精品.abcdefg潘长江是精品巴拉巴拉小魔仙哈哈
# f.seek(6)   # 移动6个字节. 2个字
# s = f.read(3)   # 读取3个字
# print(s)
# f.seek(0)
# ss = f.read(3)
# print(ss)

# s = f.read()
# f.seek(0)
# ss= f.read()
# print(s)
# print(ss)



