from django.test import TestCase

# Create your tests here
import requests
from .xuatfile import *

def Put(soduht ,username ,id_user, sl, loai):
    api = "http://127.0.0.1:8000/api/myuser/qcsama/"
    id = str(id_user)
    x = "/"
    c = str(api +id + x)

    soduht = int(soduht)
    sl = int(sl)
    kc = 0
    if loai == "1":
        kc = soduht-(5000*sl)
    if loai == "2":
        kc = soduht-(10000*sl)
    if loai == "3":
        kc = soduht-(12000*sl)
    if loai == "4":
        kc = soduht-(15000*sl)
    if loai == "5":
        kc = soduht-(20000*sl)
    if loai == "6":
        kc = soduht-(25000*sl)

    if kc >=0:
        response=requests.put(c, data={"username":username ,"sodu": kc})
        print(response.json())
        acc = DocFile(sl)
        return acc
    else:
        return "Số dư không đủ"


