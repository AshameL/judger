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
if __name__ == '__main__':
    #url手动输入
    count = 0;#微博条数
    #url_target="http://weibo.cn/gtv7777777"
    url_target = input("请用复制需要爬取的微博url（例：http://weibo.cn/gtv7777777）")
    html = getHtml(url_target).decode();
    #在这里找到总共的页数
    re_str = r'\d\/[0-9]+[\u4e00-\u9fa5]'
    list = re.findall(re_str, html)
    m = re.findall(r'(\w*[0-9]+)\w*',list[0])
    print(m)    #m[0]是当前页 ，m[1]是总页数 需要格式转换
    filelist = url_target.split('/')
    print(filelist)
    filename = filelist[-1]
    f = open(filename+'.txt','w')

    #启动循环开始爬虫   int(m[1])+1
    for page_now in range(1,int(m[1])+1):

        #修改url加上get的page参数
        url_now = url_target +'?page='+str(page_now)
        f.write(url_now+'\n')
        f.write('条数\t赞\t转发\n')
        print(url_now)
        #开始爬虫
        html_now = getHtml(url_now).decode()
        #在这里注意区分 转发 和 原文转发 的区别
        #赞：正则[\u8d5e]
        re_zan = '[\u8d5e]\[(\d+)\]<\/a'
        # 转发 正则[\u8f6c][\u53d1]
        re_zhuanfa = '[\u8f6c][\u53d1]\[(\d+)\]<\/a>'

        list_zan_row = re.findall(re_zan, html_now)
        list_zhuanfa = re.findall(re_zhuanfa, html_now)
        print('赞：')
        #这里进行二次筛选
        list_zan = []
        for i in list_zan_row:
            try:
                int(i)
                print(i)
            except BaseException as e:
                print(e)
                continue
            list_zan.append(i)

        print('转发：')
        for i in list_zhuanfa:
            print(i)
        print('\n')
        print(len(list_zan))
        print(len(list_zhuanfa))

        for i in range(0, len(list_zhuanfa)):
            count = count +1
            f.write(str(count)+'\t'+str(list_zan[i])+'\t'+str(list_zhuanfa[i])+'\n')
    f.close()
