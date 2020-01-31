# 1.1.
# f = open("a1.txt", mode="r", encoding="utf-8")
# s = f.read()
# print(s)
# f.close()
#
# # 1.2
# f = open("a1.txt", mode="a", encoding="utf-8")
# f.write("\n信不信由你.反正我信了")
# f.flush()
# f.close()

# #1.3
# f = open("a1.txt", mode="r+", encoding="utf-8")
# f.read()
# f.write("\n信不信由你.反正我信了")
# f.flush()
# f.close()

#1.4
# f = open("a1.txt", mode="w+", encoding="utf-8")
# f.write('''每天坚持一点，
# 每天努力一点，
# 每天多思考一点，
# 慢慢你会发现，
# 你的进步越来越大。
# ''')
# f.flush()
# f.close()

# 1.5
# import  os
# with open("a1.txt", mode="r", encoding="utf-8") as f1,\
#     open("a1_new.txt", mode="w", encoding="utf-8") as f2:
#     s = f1.read()
#     ss = s.replace("我说的都是真的。哈哈", "你们就信吧~\n我说的都是真的。哈哈")
#     f2.write(ss)
# os.remove("a1.txt")
# os.rename("a1_new.txt", "a1.txt")

# 6.
# f = open("a6.txt", mode="r", encoding="utf-8")
# line = f.readline()
# lst = line.split()  # 第一行切割完成 key就准备完了
#
# result = []
# # 接着向后读取
# for lin in f:
#     ll = lin.split()    # 每一行都进行切割
#     dic = {}
#     for i in range(len(ll)):    # i 表示ll的索引\
#         # lst[i]    # key
#         # ll[i]        # value
#         dic[lst[i]] = ll[i]
#     result.append(dic)
# print(result)



