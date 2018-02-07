#!/usr/bin/python3
#-*- coding:utf-8 -*-
import requests,sys #python Http客户端库，编写爬虫和测试服务器响应数据经常会用到
import re
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import urllib.request

#参考网址：http://blog.csdn.net/u010154424/article/details/52273868

print("正在从豆瓣电影中抓取数据...")

#Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36

#https://movie.douban.com/top250?start=0

for page in range(50):
   
    url = 'https://movie.douban.com/top250?start='+str(page*25)
    print('--------------------------------正在爬取第'+str(page+1)+'页数据----------------------------------')

    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'} 
    req = urllib.request.Request(url=url, headers=headers)  
    html = urllib.request.urlopen(req).read()
    
    #html = requests.get(url)#根据URL网址获取网页的源代码
    #html.raise_for_status()

    soup = BeautifulSoup(html, 'html.parser') #解析HTML
    #soup = str(soup)#转换成字符串

    #http://www.jb51.net/article/81810.htm
    #all_div = soup.find_all('div', 'shop-list J_shop-list shop-all-list')
    all_div = soup.select('div.pic a')
    for a_item in all_div:
        print('==========')
        print(a_item['href'], end=',')
        print(a_item.img['alt'], end=',')
        
        req = urllib.request.Request(url=a_item['href'], headers=headers)
        request_c = urllib.request.urlopen(req)
        if request_c.getcode() == 200:
            html = request_c.read()
            soup = BeautifulSoup(html, 'html.parser') #解析HTML
            types = soup.find(attrs={"class":"top250-no"}).string
            if types != '':
                print(types)
    #for row in all_div:
     #   print('----------------------------------------------------------------------')
      #  print(row.contents[0])
      #  item = all_div_item = row.find_all('div', attrs={'class': 'item'})
       # for row in item:
        #    print('----------------------------------------------------------------------')
        #    print(item)
     #   for r in all_div_item:
      #      print(r)
        
    #print(all_div)
    
    #title = re.compile(r'<h4>(.*)</h4>')#该函数根据包含正则表达式的字符串解析创建模式对象
    #click_url = re
    #names = re.findall(title, soup)
    #for name in names:
     #   if name.find('/') == -1: #剔除英文名（英文名特征是含有'/'）
      #        print(name)



print('爬取完毕！')
