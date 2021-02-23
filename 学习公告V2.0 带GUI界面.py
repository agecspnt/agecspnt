import requests
from bs4 import BeautifulSoup
import tkinter as tk

def getHtml(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOWh64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
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
    print('请输入要显示的总页数:')
    page=int(input())
    x=[]
    cnt=0
    print('请等待...')
    for mark in range(1,page+1):
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
                #print(res,end='---')
                #print(str(alldate)[-18:-8])
                new = res+'---'+str(alldate)[-18:-8]
                x.append(new)
                cnt+=1
                print('正在加载 %d/%d'%(cnt,18*page))
            except:
                continue
    window = tk.Tk()
    window.title("郑州轻工业大学公告板")
    window.geometry('700x400')

    # 列表部件
    v = tk.StringVar()
    v.set(x)
    ls = tk.Listbox(window, listvariable=v, width=70, height=50)
    ls.pack()

    window.mainloop()

if __name__ == '__main__':
    main()
