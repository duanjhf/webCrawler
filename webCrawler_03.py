'''
Created on Oct 21, 2018

@author: duan
'''

import urllib.request,re,os

targetPath = "/home/duan/tmp/spiderImages/"

def saveFile(path):
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)
    
    pos = path.rindex('/')
    t = os.path.join(targetPath, path[pos+1:])
    return t;

url = "https://www.douban.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

req = urllib.request.Request(url = url, headers = headers)
res = urllib.request.urlopen(req)

data = res.read()

for link,t in set(re.findall(r'(https:[^\s]*?(jpg|png|gif))', str(data))):
    print(link)
    try:
        urllib.request.urlretrieve(link, saveFile(link))
    except:
        print("failed")
                   




