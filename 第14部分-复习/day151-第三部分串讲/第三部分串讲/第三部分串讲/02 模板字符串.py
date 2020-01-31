# -*- coding: utf-8 -*-
# __author__ = "maple"

# 3.6+有模板字符串
# 字典默认会记录添加顺序(多去了解下)
# 类型注解

# asyncio 异步协程  *****


name = 'Alex'
print(f'{name} dsb.')


def foo(n1: int, n2: int)->int:
    return n1 + n2


if __name__ == '__main__':
    # foo('alex', 'dsb')
    foo(123, 321)
