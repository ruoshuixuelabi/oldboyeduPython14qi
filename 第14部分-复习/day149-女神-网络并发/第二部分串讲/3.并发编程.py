# 基础概念
# 并行和并发
    # 并行 同一时刻,多个任务在多个cpu中被执行
    # 并发 同一时间段内,多个任务交替执行在cpu上
# 进程和程序 :运行中的程序是一个进程
# 进程的三状态 :就绪 运行 阻塞
# 异步和同步
    # 异步 : 两个任务(当前所在的代码,和另一个独立的任务)之间没有明确的先后关系
    #        一个任务的继续并不影响到另一个任务的执行
    # 同步 : 两个任务之间有明确的先后关系
    #        一个任务的继续必须依赖于上一个任务的结果
# 阻塞和非阻塞
    # 阻塞 :等待io操作结束
    # 非阻塞 :不等待io操作结束
# 进程和线程和协程
    # 进程 操作系统中资源分配的最小单位,资源独立;能利用多核;有数据安全问题;占用操作系统资源开销大
    # 线程 操作系统中cpu调度的最小单位,资源共享;能利用多核;有数据安全问题;占用的操作系统资源相对少
    # 协程 操作系统不可见,资源共享,不能利用多核,本质是一条线程,没有数据安全问题;
        # 占用的操作系统资源相当于一条线程
# 进程
    # 资源独立
# 线程
    # 同时处理多个任务
    
# Cpython解释器 :
# GIL锁 CPython解释器中管理线程的机制
    # 保证了CPython解释器中 多个线程 只有一个线程在同一时间点能访问cpu
    # CPython解释器导致了我们不能充分利用多线程来访问多个CPU
# 多进程 : 帮助我们在Cpython解释器下利用多核
# 多线程 : 当我们不确定io操作或者python语言没有给这个io操作设置协程识别的语法的时候就需要使用线程了
# 协程 : 在单线程中,有n个任务,这n个任务如果同步执行,那么所有的io时间是累加在一起的
#        如果这n个任务能够共享所有的io时间
# 完成一个任务,遇到io之后,能够切换到另一个任务执行,所有的io操作的时间还能做其他任务的执行\
# 这样就可以通过一条线程完成多个任务
# 协程 :切换也是有开销的,切换的开销就和函数调用的开销是一样的

# 数据安全:
# 多个进程操作同一个文件,会出现数据不安全
# 多个线程操作同一个全局变量,会出现数据不安全
    # 对于共享的数据的操作
    # 如果是 += *= /= -= 都存在数据不安全的问题 l[0] += 1\
    # 如果是 append extend pop remove不会存在数据不安全的问题
# 协程 永远不会数据不安全 因为协程是由程序员控制的,而程序员控制的只能是代码,而不是CPU指令

import dis
import threading
# a = 0
# def func2():
#     global a
#     g = func1()
#     next(g)
#     a +=1
#     next(g)
#
# def func1():
#     global a
#     yield
#     a += 1
#     yield

# a = []
# def funca():
#     a.append(1)
#
# b = 0
# def funcb():
#     global b
#     b += 1
#
# dis.dis(funca)
# dis.dis(funcb)
# 两个线程

# multiprocess
# from multiprocessing import Process
# def target_func(a1,a2,a3):
#     pass  # 计算密集型的代码
# p = Process(target=target_func,args=(1,2,3))
# p.daemon = True # 守护进程 守护到主进程代码结束
# p.start()
# p.join()
# 锁
# 事件
# 信号量
# 管道
# 队列
# 进程池

# 生产者消费者模型
    # 爬虫的时候
    # 在高并发的web程序server

# threading
# 守护线程,是等待主线程结束之后才结束
# 主线程会等待其他非守护线程的子线程结束才结束,然后才是守护线程结束
# 锁 Lock RLock
# 事件
# 信号量
# 条件
# timer
# 队列 :import queue (Queue,LifoQueue,PriorityQueue)
from queue import Queue,LifoQueue,PriorityQueue
# q = Queue(5)
# q.put(5)
# q.put(4)
# q.put(3)
# q.put(2)
# # q.put_nowait()
# print(q.get())
# # q.get_nowait()
#
# lifoq = LifoQueue(5)
# lifoq.put(5)
# lifoq.put(4)
# lifoq.put(3)
# lifoq.put(2)
# print(lifoq.get())

# q = PriorityQueue()
# q.put((1,'zaa'))
# q.put((3,'caa'))
# q.put((2,'bbb'))
# print(q.get())
# print(q.get())
# print(q.get())

# gevent/asyncio
# from gevent import monkey
# monkey.patch_all()
# import gevent
# import socket
# import requests
# from urllib import request
# def func(url):
#     ret = request.urlopen(url)
#
# url = 'http://www.sogou.com/'
# # for i in range(100):
# #     func(url)
# g_l = []
# for i in range(100):
#     g = gevent.spawn(func,url)
#     g_l.append(g)
# gevent.joinall(g_l)















# 具体的代码
# 使用了哪些模块
# 有哪些模型
# 数据安全的问题
# 同步机制
# 池

# p.start()
# p.terminate()
# p.isalive()  True