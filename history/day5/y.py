'''
author:Tgotp

'''

import requests
import os
import time
import urllib.request,urllib.error

def askURL(url):
    head = {
           "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36" 
    }

    html = requests.get(url,headers = head) 

    html.encoding = html.apparent_encoding

    return html

def crawl(url,idx = -1):
    dirname = "ye" 
    name = dirname + "/URL"
    nam2 = dirname + "/JPG"
    nam3 = ""
    while idx > 0:
        nam3 = nam3 + str(idx % 10)
        idx = idx // 10

    name = name + nam3[::-1] + ".txt"

    nam2 = nam2 + nam3[::-1] + ".jpg"

    try:    
        open(name,"w")
    except:
        os.makedirs(dirname)
        print("不存在该目录，现已建立")

    fo = open(name,"w")
    f1 = open(nam2,"wb")

    html = askURL(url)

    fo.write(html.url)
    for chunk in html:
        f1.write(chunk)

    fo.close()
    f1.close()

def main():
    x = 1000
    for i in range(x):
        print ("正在爬取第%d 张图片" % (i + 1))
        crawl(url = 'http://iw233.cn/api/Random.php',idx = i + 1)
        time.sleep(0.1)
    print("爬取了 %d 张图!" % x)

if __name__ == '__main__':
	main()
