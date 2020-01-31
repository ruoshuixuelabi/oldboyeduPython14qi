f = open("亵渎", mode="w+", encoding="utf-8")  # w 操作.会清空原来的内容.  w+是不用的.
f.write("今天天气")
f.seek(0)
s = f.read()
print(s)
f.flush()
f.close()