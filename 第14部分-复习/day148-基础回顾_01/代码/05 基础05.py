"""
dict {}
key:value存储数据
key: 必须是可哈希的. 哈希:一种算法. 尽可能的不重复. 解决哈希冲突

    1. dic[新key] = value
    2. dic.setdefault(key,value) 最终都会通过key把value查询出来
    3. dic.pop(key)
    4. dic[老key] = value
    5. dic.get(key)
    6. dic[key]
    
    for k in dic:
    
    for k,v in dic.items():
    
    
    keys()
    values()
    items()

    set集合
    {key}
    特点: 去重复
    
    数据库去重复
    1 jay 18
    2 jay 18
    3 rose 25
    
    delete from biao where ???? group by    having count(xxx) > 1

"""