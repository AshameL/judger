'''
Created on 2014-9-23

@author: holiday
'''
import urllib.request
import os


url = "http://img0.imgtn.bdimg.com/it/u=4054848240,1657436512&fm=21&gp=0.jpg"
# headers = [(‘User-Agent’,’Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11’),
# (‘Accept’,’text/html;q=0.9,*/*;q=0.8’),
# (‘Accept-Charset’,’ISO-8859-1,utf-8;q=0.7,*;q=0.3’),
# (‘Accept-Encoding’,’gzip’),
# (‘Connection’,’close’),
# (‘Referer’,None )]#注意如果依然不能抓取的话，这里可以设置抓取网站的host
headers = [('Host','img0.imgtn.bdimg.com'),
('Connection', 'keep-alive'),
('Cache-Control', 'max-age=0'),
('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'),
('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36'),
('Accept-Encoding','gzip,deflate,sdch'),
('Accept-Language', 'zh-CN,zh;q=0.8'),
('If-None-Match', '90101f995236651aa74454922de2ad74'),
('Referer','http://image.baidu.com/i?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&word=%E4%BA%A4%E9%80%9A&ie=utf-8'),
('If-Modified-Since', 'Thu, 01 Jan 1970 00:00:00 GMT')]


opener = urllib.request.build_opener()
opener.addheaders = headers
data = opener.open(url)

print(data.decode())

'''path = "c:/151.jpg"  
f = open(path,"wb")  
f.write(data.read())  
f.close()'''
