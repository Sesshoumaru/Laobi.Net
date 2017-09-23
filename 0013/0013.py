from bs4 import BeautifulSoup
from urllib import request
import requests
from html.parser import  HTMLParser
import os

def requset_url(url):
    # 设置报头，Http协议
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36'}
    main_page = requests.get(url, headers = header)
    return main_page.text

def getExtension(url):
        extension = url.split('.')[-1]
        return extension

def download_pic(src,file_name):
    floder = "images"
    if not os.path.exists(floder):
        os.makedirs(floder, exist_ok=True)

    path_name = os.path.join(floder,file_name)
    with open(path_name,'wb') as f:
        try:
            f.write(requests.get(src).content)
        except:
            pass

if __name__ == "__main__":
    text = requset_url("http://tieba.baidu.com/p/2166231880")
    soup = BeautifulSoup(text, 'html.parser')
    imgs = soup.findAll('img')

    count = 1
    for img in imgs:
        src = img.attrs["src"]
        ext = getExtension(src)
        if(ext not in ('jpg','png')):
            continue

        file_name = str(count) + "." + ext
        print(src)
        print( file_name)
        count += 1
        download_pic(src,file_name)

    #my_parser = MyHtmlParser()
    #my_parser.feed(text)
    #print(my_parser.links)
