from pymongo import MongoClient
import requests
import json



res= requests.get("http://110.164.203.137:9919/anime")


datas = res.json()
cout =0
for anime in datas :
   print(anime.get("title"))



