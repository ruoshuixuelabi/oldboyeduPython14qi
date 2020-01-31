from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = '15217111'
API_KEY = 'jE38mGiHGGe8LnmK2YdbGGoX'
SECRET_KEY = 'KaoFdHZoaUWQsmpRgIEgxIGhdkDbW2V4'

nlp_client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

text1 = "你叫什么名字"

text2 = "您怎么称呼"


res = nlp_client.simnet(text1, text2)

print(res.get("score"))