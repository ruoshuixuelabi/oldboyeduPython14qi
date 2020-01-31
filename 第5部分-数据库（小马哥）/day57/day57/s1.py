# 1.导入模块
import pymysql

username = input('请输入用户名:')
pwd = input('请输入密码:')

# 创建连接
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    database='db7',
    port=3306,
    charset='utf8'
)

# 创建游标
cur = conn.cursor()

sql = "select * from userinfo where name = '%s' and pwd = '%s' " %(username,pwd)
print(sql)

# 执行sql语句
resCount = cur.execute(sql)

print(resCount)

if resCount:
    print('登录成功')
else:
    print('登录失败')

# 关闭
cur.close()
conn.close()
