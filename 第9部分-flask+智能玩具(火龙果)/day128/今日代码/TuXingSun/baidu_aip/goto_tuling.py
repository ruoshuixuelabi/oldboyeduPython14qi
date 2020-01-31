import requests
from settings import TL_URL as url
from settings import TL_DATA as data_dict

def tl(text, uid):
    print(text,"我是图灵我处理")
    data_dict["perception"]["inputText"]["text"] = text
    data_dict["userInfo"]["userId"] = uid
    
    res = requests.post(url, json=data_dict)
    res_json = res.json()
    
    return res_json.get("results")[0]["values"]["text"]