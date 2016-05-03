# -*- coding: utf-8 -*-
import urllib.request
url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode()
f = open('data.html','w',encoding='utf-8')

f.write(data)
#print(d)

