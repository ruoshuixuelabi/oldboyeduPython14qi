"""
encode() 编码 -> bytes
decode() 解码 -> str

int, bool, str
int : -5~256
str : py文件中, 大部分直接声明的字符串都会驻留
bool: 很早就被驻留了

目的:快速创建对象, 节省内存

s = "alex"
ss = "alex"

String interning

py:
    is和==的区别
    is: 比较内存地址
    ==: 值

JS:
    ===:  值和类型

JAVA:
    equals() 一般比较的是值
    == 比较的内存地址

"""
