f = open("小护士模特",mode="wb") # 读取的内容直接就是字节
f.write("你不好".encode("utf-8"))
f.close()

# w, r, a ===  wb, rb, ab   b: 处理的是非文本
