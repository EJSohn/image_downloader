#download_image.py

import http
from urllib.parse import urljoin, urlunparse
from urllib.request import urlretrieve
from html.parser import HTMLParser
import os

class ImageParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag != 'img':
            return 
        if not hasattr(self, 'result'):
            self.result = []
        for name, value in attrs:
            if name == 'src':
                self.result.append(value)

def downloadImage(srcUrl, data):
    if not os.path.exists('DOWNLOAD'):
        os.makedirs('DOWNLOAD')

    parser = ImageParser()
    parser.feed(data)
    resultSet = set(x for x in parser.result)

    for x in sorted(resultSet):
        src = urljoin(srcUrl, x)
        basename = os.path.basename(src)
        targetFile = os.path.join('DOWNLOAD',basename)

        print ("Downloading...", src)
        urlretrieve(src, targetFile)

def main():
    print ("http 혹은 https 프로토콜을 제외한 url 주소를 입력해주세요. 예 www.naver.com")
    url = str(input())
    for i in range(len(url)) :
        if url[i]=='/':
            host = url[0:i]
            url_1 = url[i:]
            break
            
    conn = http.client.HTTPConnection(host)

    conn.request('GET', url_1)
   
    resp = conn.getresponse()

    charset = resp.msg.get_params('charset')
    data = resp.read().decode(charset[1][1])
    conn.close()

    print ("\n>>>>>>>>Download Images from", host+url_1)
    url = urlunparse(('http',host,url_1,'','',''))
    downloadImage(url, data)

if __name__ == '__main__':
    main()
    
    
