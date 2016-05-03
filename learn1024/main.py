# coding=utf-8
import urllib.request
import re
import os
import urllib

from collections import deque


# 伪装浏览器访问目的网址
# 注意下返回值
def getHtml(url):
    req = urllib.request.Request(url, headers={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })
    page = urllib.request.urlopen(req)
    html = page.read()
    # print(html.decode())
    return html


# 正则区分图片，返回一个list
def getImg(html):
    # 引入图片的方法是在是太多了，总结起来是以上4种
    imglist = re.findall("input src='(http.*?)'", html)
    imglist2 = re.findall("input src='(https.*?)'", html)
    imglist3 = re.findall("img src='(http.*?)'", html)
    imglist4 = re.findall('img src="(https.*?)"', html)

    imglist.extend(imglist2)
    imglist.extend(imglist3)
    imglist.extend(imglist4)

    return imglist


##########################################主程序#######################################
queue = deque()
visited = set()
# url手动输入
#域名规律待探索中......
url_target = "http://on.clcl.online/thread0806.php?fid=16"

queue.append(url_target)
cnt = 0
while queue:
    url = queue.popleft()
    visited |= {url} #或运算，标记已经访问
    print('已经抓取:' + str(cnt) + '正在抓取 <------' + url)
    cnt += 1
    req = urllib.request.Request(url, headers={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })
    urlop = urllib.request.urlopen(req, timeout=2)
    if 'html' not in urlop.getheader('Content-Type'):
        continue
        #测试url   http://on.clcl.online/htm_data/16/1605/1916817.html

        # 避免程序异常
    try:
        data = urlop.read().decode("GBK")
    except:
        continue

    # 正则表达式提取页面中所有队列，并判断是否已经访问过，然后加入待爬队列
    # <a target="_blank" href="htm_data/16/1605/1916284.html" title="打開新窗口">.::</a>
    linkre = re.compile(r'href="(htm_data+html)"')
    #############################在这里修改
    for x in linkre.findall(data):
        y = r'http://on.clcl.online/' + x
        queue.append(y)
        print('加入队列----->' + y)
