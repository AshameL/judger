#仅适用于鼠绘漫画网
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
    #f = open('text.html','w',encoding = 'utf-8')
    #print(html.decode())
    #f.write(html.decode())
    
    return html;  

def getImg(html):
    #这里的正则仅适用与鼠绘网
    
    imglist = re.findall('src="(http.*png)"',html)
    list1 = []
    for x in imglist:
        y = x.split('"')
        #print('this is ',y[0])
        list1.append(y[0])
    print(list1)
    return list1


#url手动输入
url_target="http://www.ishuhui.com/post/375882" 
html = getHtml(url_target).decode();  
imagesUrl = getImg(html);


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
