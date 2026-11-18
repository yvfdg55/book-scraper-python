# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 04:25:19 2026

@author: hello
"""

import re
import requests
from bs4 import BeautifulSoup
import tabulate
import time
import json


url="https://books.toscrape.com/"
headers=headers={'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"}

res= requests.get(url,headers=headers)

soup=BeautifulSoup(res.text,"html.parser")
data=soup.find_all('li', class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

price=re.findall(r'p class="price_color">(Â£\d+\.\d+)',str(data))
name=re.findall(r'title="(.*)"',str(data))
stock=re.findall(r'<i class="icon-ok"></i>\s*(.+)\s*</p>',str(data))
print(price)
print(name)
print(stock)

dic={}
for i in range(len(name)):
    
    dic[name[i]]=price[i],stock[i]
print (dic)


    
    
table=[]
for i in range(len(name)):
    table.append([name[i],price[i],stock[i]])
    
print(tabulate.tabulate(table,headers=['name','prise','stock'],tablefmt="grid"))
    

