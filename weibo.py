import requests

cook = {'Cookie':''}
url = 'http://weibo.cn/'
html = requests.get(url).content
print (html)
