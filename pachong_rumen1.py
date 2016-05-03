import re
import urllib.request
import urllib

from collections import deque

queue = deque()
visited = set()

url = 'https://www.hao123.com/'

queue.append(url)
cnt = 0

while queue:
    url = queue.popleft()
    visited |= {url}  #按位或，标记为已经访问

    print('已经抓取:' + str(cnt) +'正在抓取 <------' + url)
    cnt += 1
    urlop = urllib.request.urlopen(url,timeout = 2)
    if 'html' not in urlop.getheader('Content-Type'):
        continue

    # 避免程序异常
    try:
        data = urlop.read().decode()

    except:
        continue

    # 正则表达式提取页面中所有队列，并判断是否已经访问过，然后加入待爬队列

    linkre = re.compile(r'href="(.+?)"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列----->' + x)
            
