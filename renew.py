import requests
import pandas
from requests.api import get
import pymongo



res1 = requests.get('https://alphabet.researchandranking.com/assignment/stockData?entry=old')
res2 = requests.get('https://alphabet.researchandranking.com/assignment/stockData?entry=new')
  
r1 = res1.content
r2 = res2.json()

print(r2[0]['volume'])
# print(r2)
