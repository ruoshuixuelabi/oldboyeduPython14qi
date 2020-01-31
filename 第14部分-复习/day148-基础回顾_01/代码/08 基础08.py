"""
文件操作
open(文件, 模式, 编码)

文件路径:
    1. 绝对路径 : 磁盘根目录
    2. 相对路径 : 当前文件所在文件夹
    
模式:
    r, w, a, r+, w+, a+, wb, rb, ab
    
操作:
    read() 读
    readline()
    readlines()
    
for line in f:
    pass
    
seek(0)
seek(0,2)

with open() as f:
    pass
    
os.remove()
os.rename()


"""