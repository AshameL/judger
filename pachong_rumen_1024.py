#coding=utf-8  
import urllib.request  
import re  
import os  
  
''''' 
Urllib 模块提供了读取web页面数据的接口，我们可以像读取本地文件一样读取www和ftp上的数据 
urlopen 方法用来打开一个url 
read方法 用于读取Url上的数据 
'''  
  
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
#这里与美空版不同。主要抓取内容图。img 内容进行修改
def getImg(html):  
    imglist = re.findall("input src='(http.*?)'",html)  
    return imglist

# 这个方法用来补充https的img
def getImg2(html):  
    imglist = re.findall("input src='(https.*?)'",html)  
    return imglist  
#url手动输入
url_target="http://on.clcl.online/htm_data/16/1604/1906251.html" 
html = getHtml(url_target).decode('GBK');  
imagesUrl = getImg(html);
#补充https
imagesUrl.extend(getImg2(html))


#创建文件目录
'''
if os.path.exists("D:/imags") == False:  
    os.mkdir("D:/imags");  
'''
#这里进行url命名文件名
url_temp = url_target[7:]
url_list = re.split(r'./',url_temp)
url_folder = '_'.join(url_list)
url_folder =  "D:/imags/" + url_folder + r"/"

if os.path.exists(url_folder) == False:  
    os.mkdir(url_folder);  

count = 0;
#对于url进行预处理,第一个部分是链接

for url in imagesUrl:
    #1024里不需要去掉get报文内容
    #url = url.split('?')[0]
    print(url)  
    if(url.find('.') != -1):  
        name = url[url.find('.',len(url) - 5):];
        if name.strip()=='':
            name='.jpg'
        #print('name:'+name)
        try:
            bytes = urllib.request.urlopen(url,timeout = 2);
            f = open(url_folder+str(count)+name, 'wb');  
            f.write(bytes.read());  
            f.flush();  
            f.close();
        except:
            print(count," cannot be downloaded...")
        count+=1;  
