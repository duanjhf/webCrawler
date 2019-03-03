'''
Created on Jan 20, 2019

@author: duan
'''

import urllib.request, gzip, re, http.cookiejar, urllib.parse
import sys
from _multiprocessing import flags

def ungzip(data):
    try:
        print("正在解压缩...")
        data = gzip.decompress(data)
        print("解压完成...")
    except:
        print("未压缩，无需解压...")
    return data

def getOpener(header):
    cookieJar = http.cookiejar.CookieJar()
    cp = urllib.request.HTTPCookieProcessor(cookieJar)
    opener = urllib.request.build_opener(cp)
    headers = []
    for key,value in header.items():
        elem = (key, value)
        headers.append(elem)
    opener.addheaders = headers
    return opener

def getXsrf(data):
    cer = re.compile('name=\"_xsrf\"value=\"(.*)\"', flags=0)
    strlist = cer.findall(data.decode('utf-8'))
    return strlist[0]

headers = {
    'Connection': 'Keep-Alive',
    'Accept': '*/*',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Accept-Encoding': 'gzip,deflate,br',
    'Host': 'www.zhihu.com',
    'DNT':'1'
}

url = "https://www.zhihu.com"
req = urllib.request.Request(url, headers=headers)
res = urllib.request.urlopen(req)

#读取zhihu首页内容，获得_xsrf
data = res.read()
data = ungzip(data)
#_xsrf = getXsrf(data.decode('utf-8'))
_xsrf = getXsrf(data)

opener = getOpener(headers)

#post数据接收和处理的页面，我们要向这个页面发送构造的post数据
url += 'login/email'
name = '18688742099'
passwd = '8114yunyue'

#分析构造post数据
postDic = {
    '_xsrf':_xsrf,
    'email':name,
    'password':passwd,
    'remeber_me':'true'
}

#给post数据编码
postData=urllib.parse.urlencode(postDic).encode()

#构造请求
res = opener.open(url, postData)
data = res.read()

#解压缩
data = ungzip(data)
print(data.decode())








