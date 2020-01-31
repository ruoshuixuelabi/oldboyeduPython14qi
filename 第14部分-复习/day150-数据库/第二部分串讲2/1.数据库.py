# -*- coding: utf-8 -*-
# __author__ = "maple"


# 表操作
# 你的项目的数据库的情况
    # 是你自己搭的环境
    # 还是用的公司的平台环境
# 你公司数据库的版本
    # 公司的平台
        # 5.5
        # 5.6
        # 5.7
        # 5.8
        # 7.0
    # 自己搭的环境
        # 可以是任何一个版本
# 你的项目使用的什么存储引擎
    # innodb
    # myisam
# 你为什么要用这个存储引擎

# mysql存储引擎
    # innodb 行级锁 支持事务和外键 对于多删改的程序保持数据一致性有更好的性能
    # myisam 表级锁 查询和插入都非常快 不适合多删改 高并发 对事务一致性要求高的程序
    # memoory 内存级别的存储引擎  更多的用来做缓存
    # blackhole 用来做大量数据的分流的
# 数据类型

# 完整性约束 : not null,unique,primary key ,foreignkey

# 设计表结构 :
    # 几张表
    # 表与表之间的关系 : 一对一 一对多 多对多
    # 关联的键
    # 每张表中的主键和外键
    # 索引关系

# 单表查询的执行顺序
# select ... from table where condition group by col having filter_con order by  limit offset
# from where group by  having select distinct orderby limit
# limit 取n个 offset 偏移量

# 多表查询
# left join
# right join
# inner join
# union
# union all 没有 left join union right join
# 子查询

# 索引
# 聚集索引 只能有一个 就是主键
    # id name age
    # 1  alex  83
    # 2  wusir 74
    # 3  yuan  25

# 非聚集索引 辅助索引 可以有多个
    # 大概比聚集索引多一次IO操作

# 索引的种类:
    # 普通索引
    # 唯一索引
    # 主键索引
    # 联合索引(联合主键索引,联合唯一索引,联合普通索引)

# 使用索引的优缺点
    # 优点 加速了查询速度
    # 缺点 创建了索引会降低写速度,占更多的硬盘空间

# 合并索引


















