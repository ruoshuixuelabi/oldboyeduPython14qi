# -*- coding: utf-8 -*-
# __author__ = "maple"

# tornado yield 协程
# yield from

# def func():
#     yield 1
#     yield 2
#
# def func2():
#     yield from [1,2]
#
# def func3():
#     yield from range(1,3)


# def func():    # 子生成器
#     n = yield 1
#     print(n)
#     yield 2
#
# def func2():   # 委托生成器
#     yield from func()   # 建立起一个桥梁,可以帮助我们控制生成器的停止或者继续
#
# g = func2()
# ret1 = g.send(None)
# print(ret1)
# print(g.send('n'))
# import time
# from types import coroutine
#
# @coroutine
# def func():    # 子生成器
#     n = yield 1
#     print(n)
#     time.sleep(1)
#     yield 2
#
# @coroutine
# def func2():    # 子生成器
#     n = yield 1
#     print(n)
#     time.sleep(1)
#     yield 2
#
# async def func2():   # 委托生成器
#     await func()   # 建立起一个桥梁,可以帮助我们控制生成器的停止或者继续


# 如何去规避这个阻塞事件的呢?
# 协程 + 事件循环

# import asyncio
# async def func():
#     print('start')
#     await asyncio.sleep(1)   # time.sleep 异步的接口 对象 必须实现__await__
#     print('end')
#
# loop = asyncio.get_event_loop()
# task1 = loop.create_task(func())
# task2 = loop.create_task(func())
# loop.run_until_complete(asyncio.wait([task1,task2]))

# asyncio是一个底层模块
# 他完成了几个任务的轮流检测io,并且在遇到io的时候能够及时在任务之间进行切换
# 然后达到使用单线程实现异步的方式

# aiohttp
# 完全使用asyncio作为底层模块完成的


# loop 你的循环
# 你的协程任务就是 被async语法约束的 函数
# 你的协程任务遇到io才能切出去,如何标识你的任务遇到io了呢? await 对象

# async 语法 帮助我们创建协程任务
# asyncio模块 : 异步io模块 对协程任务的循环管理 内置了很多异步的接口帮助我们 异步的socketserver,采用异步的形式去访问socket server