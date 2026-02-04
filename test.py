from pymongo import MongoClient
import requests
import json
import time


res= requests.get("http://110.164.203.137:9919/anime")


datas = res.json()
cout =0
for anime in datas :
    time.sleep(1)
    print(anime.get("title"))



