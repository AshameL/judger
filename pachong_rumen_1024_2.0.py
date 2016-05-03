#coding=utf-8  
import urllib.request  
import re  
import os
import urllib

from collections import deque


#伪装浏览器访问目的网址 
def getHtml(url):
    req = urllib.request.Request(url, headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})
    page = urllib.request.urlopen(req);  
    html = page.read();
    #print(html.decode())
    return html;


#正则区分图片
def getImg(html):
    #引入图片的方法是在是太多了，总结起来是以上4种
    imglist = re.findall("input src='(http.*?)'",html)
    imglist2 = re.findall("input src='(https.*?)'",html)
    imglist3 = re.findall("img src='(http.*?)'",html)
    imglist4 = re.findall('img src="(https.*?)"',html)
    
    imglist.extend(imglist2)
    imglist.extend(imglist3)
    imglist.extend(imglist4)
    
    return imglist


##################################################################
  
##########################################主程序#######################################
queue = deque()
visited = set()

#url手动输入
url_target="http://on.clcl.online/htm_data/7/1604/1905769.html"

queue.append(url_target)
cnt = 0

while queue:
    url = queue.popleft()
    visited |= {url}  #按位或，标记为已经访问

    print('已经抓取:' + str(cnt) +'正在抓取 <------' + url)
    cnt += 1
    
html = getHtml(url_target).decode('GBK');  
imagesUrl = getImg(html);


#这里进行url命名文件名

url_temp = url_target[7:]
url_list = re.split(r'./?',url_temp)
url_folder = '_'.join(url_list)
url_folder =  "D:/imags/" + url_folder + r"/"

if os.path.exists(url_folder) == False:  
    os.mkdir(url_folder);  

count = 0;
#对于url进行预处理,第一个部分是链接

for url in imagesUrl:
    #1024里不需要去掉get报文内容
        
    print(url)  
    if(url.find('.') != -1):
        name = url[url.find('.',len(url) - 5):];
        if name.strip()=='':
            name='.jpg'
        #print('name:'+name)
        try:
            req = urllib.request.Request(url, headers = {
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
             })
            bytes = urllib.request.urlopen(req,timeout = 2);
            f = open(url_folder+str(count)+name, 'wb');  
            f.write(bytes.read());  
            f.flush();  
            f.close();
        except BaseException as e:
            print(e)
            print(count," cannot be downloaded...")
        count+=1;
    
    #urlop = urllib.request.urlopen(url,timeout = 2)

    if 'html' not in bytes.getheader('Content-Type'):
        continue

    # 避免程序异常

    try:
        data = bytes.decode()
        print(data)

    except BaseException as e:
        print(e)
        continue
   
    # 正则表达式提取页面中所有队列，并判断是否已经访问过，然后加入待爬队列

    linkre = re.compile(r'href="(.+?)"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列----->' + x)
            


