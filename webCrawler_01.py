'''
Created on Oct 18, 2018

@author: duan
'''

import urllib.request

url = "http://www.douban.com/"

request = urllib.request.Request(url)

response = urllib.request.urlopen(request)

data = response.read()

data = data.decode('utf-8')

# print(data)

print(type(response))
print(response.geturl())
print(response.getcode())

print(response.info())