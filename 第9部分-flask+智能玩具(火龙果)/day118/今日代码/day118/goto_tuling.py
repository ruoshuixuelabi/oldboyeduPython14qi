import requests

url = "http://openapi.tuling123.com/openapi/api/v2"

data_dict = {
	"reqType":0,
    "perception": {
        "inputText": {
            "text": "北京"
        },
    },
    "userInfo": {
        "apiKey": "c3a9ba0d958a43658a5acdcae50c13ae",
        "userId": "jinwangbas"
    }
}
def tl(text,uid):
    data_dict["perception"]["inputText"]["text"] = text
    data_dict["userInfo"]["userId"] = uid
    
    res = requests.post(url,json=data_dict)
    res_json = res.json()
    
    return res_json.get("results")[0]["values"]["text"]