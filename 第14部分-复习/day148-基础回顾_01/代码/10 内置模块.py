"""
    random
    random.random()  # 0-1之间的小数
    random.uniform() # 小数 (m,n)
    
    random.randint()  随机整数 [m,n]
    
    random.choice()  从列表中随机选择一个
    random.sample() 从列表中随机选择n个
    
    random.shuffle() 打乱

    time模块
    时间戳
        time.time() 当前系统时间, 从1970-01-01 08:00:00
        
    格式化时间
        time.strftime("%y-%m-%d %H:%M:%S") 字符串格式化时间  f: format
        
    结构化时间
        time.localtime()  本质是一个元组. 用来做转化的
        
        
    时间戳转化成格式化时间
        # n = 180000000
        # # 转化成结构化时间
        # struct_time = time.localtime(n)
        # # 转化成格式化时间
        # str_time = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
        #
        # print(str_time)
        
        # # 把一个格式化时间转化成数字
        # date = input("请输入时间(yyyy-MM-dd HH:mm:ss):")
        # # 把字符串转化成结构化时间
        # struct_time = time.strptime(date, "%Y-%m-%d %H:%M:%S") # p: parse 转化
        # # 变成时间戳
        # n = time.mktime(struct_time)
        
    os和操作系统相关
        
        1 os.mkdir()  创建一个文件夹
        2 os.makedirs() 创建一个多级目录
        3 os.rmdir()
        4 os.removedirs()
        
        os.listdir() 列出目标文件夹内的所有文件
        
        os.path.isfile
        os.path.isdir
        os.path.exists
        
        os.path.join
        os.path.getsize() 文件大小
        
    sys 和python解释器相关
        sys.path 模块的搜索路径
        sys.argv 获取命令行参数
        
    
    collections
        namedtuple
        
            Point = namedtuple("Point", ["x", "y"]) # 创建了一个类
            p1 = Point(1,2)  # 创建一个对象
            
            print(p1)
            print(p1.x)
            print(p1.y)
        OrderedDict
            不用了
            
        Counter
            计数器
            c = Counter("哈哈哈哈哈哈")
            print(c)
            
        deque
            双向队列
            
            数据结构
                Stack 栈, 先进后出
                Queue 队列, 先进先出
                
                class StackFullError(Exception):
                    pass
                class StackEmptyError(Exception):
                    pass
                
                class Stack:
                    def __init__(self, size):
                        self.size = size
                        self.lst = []
                        self.top = 0 # 下一个元素准备装的位置
                
                    def push(self, el):
                        # self.lst[self.top] = el # 报错
                        if self.top == self.size:
                            raise StackFullError('满了')
                        self.lst.insert(self.top, el)
                        self.top += 1 # 栈顶指针. 向上移动
                        
                    def pop(self):
                        if self.top == 0:
                            raise StackEmptyError("空的")
                        self.top -= 1 # 先移动站定指针
                        data = self.lst[self.top]
                        del self.lst[self.top]
                        return data
                    
                    
                s = Stack(6)
                s.push("马卫华1")
                s.push("马卫华2")
                s.push("马卫华3")
                s.push("马卫华4")
                s.push("马卫华5")
                s.push("马卫华6")
                
                
                
                print(s.pop())
                print(s.pop())
                print(s.pop())
                print(s.pop())
                print(s.pop())
                print(s.pop())
                print(s.pop())
            
        
        hashlib模块
        
        pickle模块
            dumps  序列化成bytes字节
            loads  发序列化成对象
            
            dump   序列化之后的bytes写入文件
            load   从文件导出bytes. 反序列化成对象
        
        json模块
            dumps  数据转化成json
            loads  json转化回数据
            
            dump   序列化之后的bytes写入文件
            load   从文件导出bytes. 反序列化成对象
            
            python   json
            None     null
            True     true
            False    false
            dict     {}
            list     []
            
        re模块
            正则表达式
            
            普通字符 a b  ab
            元字符
                .   除了换行符以外的其他所有内容
                \w  数字, 字母, 下划线
                \d  数字
                \s  空白
                \b  单词的结尾
                \W  除了数字, 字母, 下划线
                \D  除了数字
                \n
                \t
                ^   开头
                $   结尾
                [abc]  字符组
                [^abc]
                () 分组  \1
                |
            量词:
                * 零次或多次
                + 1次或多次
                ? 0次或1次
                {n} n次
                {m,n} m次到n次
                {m,} m次到更多次
                
             贪婪匹配
                 *
                 +
                 ?
                 
            惰性匹配
                a*?m
        re模块
            search 全文检索
            match 从头开始   ^
    
            import re

            it = re.finditer(r"(?P<shuzi>\d+)", "你好啊, 我叫赛利亚123")
            print(it.__next__().group("shuzi"))
            
            re.search()
            re.match()
            re.sub()
            re.split()
            
        模块和包
            模块: 我们写的py文件
                import xxx
                from xxx import xxxxx
                
                __name__
                
            包: (留坑)
                sys.path
                启动文件必须在包外面
                
                相对导入
                    相对当前目录导入
                    . 当前
                    .. 上级目录
                绝对导入
                    从项目根目录导入
            
"""

import time
# print(time.localtime())

# n = 180000000
# # 转化成结构化时间
# struct_time = time.localtime(n)
# # 转化成格式化时间
# str_time = time.strftime("%Y-%m-%d %H:%M:%S", struct_time)
#
# print(str_time)

# # 把一个格式化时间转化成数字
# date = input("请输入时间(yyyy-MM-dd HH:mm:ss):")
# # 把字符串转化成结构化时间
# struct_time = time.strptime(date, "%Y-%m-%d %H:%M:%S") # p: parse 转化
# # 变成时间戳
# n = time.mktime(struct_time)
#
# print(n)
#
# time.gmtime() # 格林尼治时间
# time.localtime() # 本地化时间


# import os
# os.makedirs("胡一菲/曾小贤/小姨妈/吕子乔/雷佳音")
# os.path.getsize()
#
from collections import namedtuple, OrderedDict, deque, Counter

# c = Counter(["马卫华","马卫华", "周杰伦"])
# print(c)
#
# Point = namedtuple("Point", ["x", "y"]) # 创建了一个类
# p1 = Point(1,2)  # 创建一个对象
#
# print(p1)
# print(p1.x)
# print(p1.y)

# class Point:
#     def __init__(self,x, y):
#         self.x = x
#         self.y = y


# import queue
#
# q = queue.Queue()
# q.put("马卫华1")
# q.put("马卫华2")
# q.put("马卫华3")
# q.put("马卫华4")
# q.put("马卫华5")
#
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
# print(q.get())
#
# from collections import deque
# dq = deque()
# dq.append("今夜在浪漫剧场")
# dq.append("我想吃掉你的胰脏")
# dq.append("风来坊")
#
# dq.appendleft("流浪地球")
# dq.appendleft("新喜剧之王")
# dq.appendleft("飞驰人生")
#
# print(dq)
#
# print(dq.pop())
# print(dq.pop())
# print(dq.pop())
# print(dq.popleft())
# print(dq.popleft())
# print(dq.popleft())

# import hashlib
#
# md5 = hashlib.md5(b'flkja123sdlfjlasdkfjkladjflkdasjflkdasjfkldajfkla12312321dsjfkldasjfkldas123jfkladsjfkl')
#
# s = "alex"
# # f = open("", mode="rb")
# # for line in f:
# #     md5.update(line)
# md5.update(s.encode("utf-8"))
#
# psw = md5.hexdigest()
# print(psw)






