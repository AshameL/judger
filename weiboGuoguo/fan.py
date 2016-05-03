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
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Cookie':' _T_WM=b736d63c5dc68324d700af9fa340c459; SUB=_2A256JNFgDeRxGeNN6FcV9y7FyjuIHXVZ5v8orDV6PUJbrdAKLW_FkW1LHeti_rGyLc9pSuJy4cfbS0k0zqeb9w..; SUHB=0rr76uMORU89v3; SSOLoginState=1461756208; gsid_CTandWM=4uQ5CpOz5cx14XqHlQaGTmnZYeN'

    })
    page = urllib.request.urlopen(req);
    html = page.read();
    #print(html.decode())
    return html;

def getImg(html):
    #引入图片的方法是在是太多了，总结起来是以上4种
    imglist = re.findall('img src="(http.*?)"',html)

    return imglist

if __name__ == '__main__':
    url_target = "http://weibo.cn/1658761387/fans" #/fans 是粉丝数量爬取
    html = getHtml(url_target).decode();
    print(html)
    #<td valign="top"><a href="http://weibo.cn/u/5335470917">AshameL</a><br/>粉丝23人<br/>
    fans_link = '<td valign="top"><a href="(.*?)">'
    listfans = re.findall(fans_link, html)
    for i in listfans:
        print(i)