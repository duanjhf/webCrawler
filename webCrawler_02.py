'''
Created on Oct 21, 2018

@author: duan
'''

import urllib.request

def saveFile(data):
    path = "/home/duan/tmp/test2.txt"
    f = open(path, 'wb')
    f.write(data)
    f.close()

url = "https://www.douban.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

req = urllib.request.Request(url = url, headers = headers)

res = urllib.request.urlopen(req)
data = res.read()

saveFile(data)

data = data.decode('utf-8')

# print(data)

print(type(res))
print(res.geturl())
print(res.getcode())
print(res.info())
