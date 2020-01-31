import jieba
from settings import MONGO_DB

# jieba.add_word("挂了")
# jieba.add_word("太上皇打")
res = list(jieba.cut("来一首小毛驴"))
print(res)


# ck = []
#
content = MONGO_DB.content.find({})

for con in content:
    ck.append(list(jieba.cut(con.get("title"))))
#
# print(ck)

