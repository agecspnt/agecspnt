import requests
from bs4 import BeautifulSoup

def getHtml(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
               "Referer": "http://news.zzuli.edu.cn/511"
        }
    html = requests.get(url, headers = headers)
    html.encoding = html.apparent_encoding #去除乱码 正常显示中文
    return html

def getSoup(html):
    return BeautifulSoup(html.text, "html.parser")

def gettitle(soup,num):#得到标题
    alltitle = soup.select(f'#wp_news_w9 > ul > li.news-item.item-{num}.clearfix > span.column-news-title > a ')
    return alltitle

def getdate(soup,num):
    alldate = soup.select(f'#wp_news_w9 > ul > li.news-item.item-{num}.clearfix > span.column-news-date.news-date-hide')
    return alldate

def main():
    for mark in range(1,17):
        for i in range(1,19):
            try:
                html = getHtml(f"http://news.zzuli.edu.cn/511/list{mark}.htm")
                soup = getSoup(html)
                alltitle = gettitle(soup,i)
                alldate = getdate(soup,i)
                s = str(alltitle)[66:]
                temp = [0, 1]
                a = s.split(">")
                res = a[0]
                res = res[0:-1]
                print(res,end='---')
                print(str(alldate)[-18:-8])
            except:
                continue

if __name__ == '__main__':
    main()
