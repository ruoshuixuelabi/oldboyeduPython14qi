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

sql = "select * from userinfo where name = %(name1)s and pwd =%(pwd1)s "
print(sql)

# 执行sql语句
# 防止sql注入
# resCount = cur.execute(sql,(username,pwd))
# resCount = cur.execute(sql,[username,pwd])

resCount = cur.execute(sql,{"name1":username,"pwd1":pwd})


print(resCount)

if resCount:
    print('登录成功')
else:
    print('登录失败')

# 关闭
cur.close()
conn.close()
