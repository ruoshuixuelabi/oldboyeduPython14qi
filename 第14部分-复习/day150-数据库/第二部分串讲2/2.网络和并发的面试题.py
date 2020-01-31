# -*- coding: utf-8 -*-
# __author__ = "maple"


# 30 iptables
# iptables -t filter  -A INPUT -s 192.168.1.5 -m UDP -dport 53 -j DROP
# iptables -t filter -A INPUT -s 10.1.1.0/24 -m UDP -m multiport --dports 8888,9999 -j ACCEPT


# 41 死锁
# 多个线程 多把锁 交替acquire
# a.acquire       # b.acquire
# b.acquire       # a.acquire

# mysql备份表
# shell> mysqldump -hmysql的ip地址
# shell> mysqldump -h 127.0.0.1 -uroot -p123 库名 表名 > 路径/文件名.sql
# mysql > source 路径/文件名.sql 恢复文件


# 锁
# 行锁 : 行共享 行排他
# 表锁




















