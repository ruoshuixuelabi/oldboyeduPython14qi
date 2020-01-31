import requests
from settings import LT_URL
from settings import MONGO_DB
from uuid import uuid4
import time,hashlib


def create_qr(num:int):
    qr_list = []
    for i in range(num):
        QR_str = hashlib.md5(f"{uuid4()}{time.time()}{uuid4()}".encode("utf8")).hexdigest()
        res = requests.get(LT_URL%(QR_str))
        with open(f"{QR_str}.jpg","wb") as f:
            f.write(res.content)
        
        qr_list.append({"device_key":QR_str})
        
        time.sleep(0.5)

    MONGO_DB.devices.insert_many(qr_list)

create_qr(20)
