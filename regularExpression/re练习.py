'''
抓取腾讯主页中的图片到本地
1. 抓取网页
2. 抓取图片地址
3. 抓取图片内容并保存到本地
'''


import requests
def getdata():
    url = 'http://www.qq.com/'
    buf = requests.get(url)
    return buf

buf = getdata()

import re
from numpy import *

# 抓取png和jpg图像
listurl1 = re.findall(r'src="http://.*\.png', buf.text)
listurl2 = re.findall(r'src="http://.*\.jpg', buf.text)
listURL = []

# 去除url上不必要的前缀
for url in listurl1:
     listURL.append(re.findall(r'http:.*\.png', url))
for url in listurl2:
    listURL.append(re.findall(r'http:.*\.jpg', url))

# 将网上图片写入本地
i = 0
for url in listURL:
    f = open(str(i)+'.png', 'wb')
    buf = requests.get(url[0], stream=True)
    for chunk in buf.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)
            f.flush()
    f.close()
    i += 1