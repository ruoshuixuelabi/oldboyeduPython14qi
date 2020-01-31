# f 表示这个文件
f = open("马化腾", mode="r", encoding="utf-8")
for line in f:  # 每次循环执行一次readline()
    print(line)
