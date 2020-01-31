f = open("小护士模特",mode="rb") # 读取的内容直接就是字节
bs = f.read()
print(bs.decode("utf-8"))   # 需要解码
f.close()
