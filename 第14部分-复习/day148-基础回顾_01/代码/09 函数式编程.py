"""

语法:
    def  函数名(形参):
        函数体-return
        
    函数名(实参)
    
    形参: 位置, *args, 默认值, **kwargs
    实参: 位置, 关键字参数, *, **
    
    *, **: 形参:聚合, 实参:打散
    
    
函数互相调用
函数嵌套
def func1():
    def func2():
        def func3():
        
    func2()

func1()

闭包:
    内层函数使用外层函数的变量
    作用:
        1. 保护变量.
        2. 常驻内存
        
作用域:
     全局作用域: 内置+全局
     局部作用域: 函数内部

global : 在局部使用全局
nonlocal  : 在局部!!!!! 在局部使用外层离它最近的那个局部变量

globals()  查看全局内容
locals()  查看当前作用域


函数名: 变量名(引用)

a = 10

变量 = 值
引用 = 对象
句柄 = document.getElementById()对象

装饰器
目的: 不改变原来代码的基础上. 给函数添加新功能
动态代理. 拦截器

通用装饰器的写法
def wrapper(fn):
    def inner(*args, **kwargs):
        '''之前'''
        ret = fn(*args, **kwargs)
        '''之后'''
        return ret
    return inner

@wrapper
def login():
    pass
   
带参数的装饰器
def wrapper_out(flag):
    def wrapper(fn):
        def inner(*args, **kwargs):
            if flag:
                print("问问金老板, 行情怎么样")
            else:
                print("自己去")
            ret = fn(*args, **kwargs)
            print("亲人两行泪")
            return ret
        return inner
    return wrapper

@wrapper_out(False)
def yue():
    print("约me?")

@wrapper_out(True)
def chi():
    print("吃饭去了")

yue()
chi()


同一个函数被多个装饰器装饰
@wrapper1
@wrapper2
@wrapper3
def yue():
    print("约me?")
    
# {[(yue)]}

wrapper1
wrapper2
wrapper3
yue
wrapper3
wrapper2
wrapper1


迭代器
    目的: 让不同的数据类型有相同的遍历方式
    __iter__() 获取迭代器
    __next__() 获取数据.
    
    for循环
    
    from collections import Iterator, Iterable
    
    isinstance(xx, Iterator)
    isinstance(xx, Iterable)
    
生成器
    写生成器的方式:
        1. 生成器函数   -> yield
        2. 生成器表达式 -> (结果 for循环 if)
        
    特点:
        1. 省内存
        2. 惰性机制(面试题)
        3. 只能向前. 不能反复
        
    本质是迭代器
        __iter__
        __next__
        send()
        
    推导式
        列表
        字典
        生成器表达式
        
        [结果 for if]
        
    lambda:
        lambda 参数:返回值
        
        和内置函数一起用
        sorted, map, filter
        
        sorted(迭代对象, key = func, reverse = xxx)
        map(func, iter)  映射
        filter(func, iter) 筛选
      
      
      递归
        def func():
            func()
        在不确定循环层数的时候.
        树形结构遍历
        
        最大递归深度:
            998
            1000
        
        二分查找
            特点: 掐头结尾取中间
            
            有序的海量数据
         
"""
