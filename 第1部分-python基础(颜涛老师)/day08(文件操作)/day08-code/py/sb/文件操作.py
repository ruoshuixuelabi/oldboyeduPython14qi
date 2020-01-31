f = open("../../file/wuse", mode='r', encoding="utf-8") # ../表示上一层文件夹
s = f.read()
print(s)
f.close()