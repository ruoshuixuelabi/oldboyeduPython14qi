# 1.导入模块
import pymysql

# 创建连接
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    database='db7',
    port=3306,
    charset='utf8'
)

# 创建游标
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

sql = "select * from userinfo"
print(sql)

resCount = cur.execute(sql)
print(resCount)

# row = cur.fetchone()
# print(row)
# row = cur.fetchone()
# print(row)
# row = cur.fetchone()
# print(row)

# rows = cur.fetchmany(10)
# print(rows)

# rows = cur.fetchall()
# print(rows)
row = cur.fetchone()
print(row)
row = cur.fetchone()
print(row)
row = cur.fetchone()
print(row)
# 相对于自己  如果第一个参数是正数  向下 移动
# cur.scroll(-1,mode='relative')
# row = cur.fetchone()
# print(row)


# absolute 相对于起始位置
cur.scroll(1,mode='absolute')
row = cur.fetchone()
print(row)



# 关闭
cur.close()
conn.close()
