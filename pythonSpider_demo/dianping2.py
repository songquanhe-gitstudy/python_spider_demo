#!/usr/bin/python3
#-*- coding:utf-8 -*-
import requests,sys #python Http客户端库，编写爬虫和测试服务器响应数据经常会用到
import re
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import urllib.request

#参考网址：http://blog.csdn.net/u010154424/article/details/52273868

print("正在从大众点评中抓取数据...")

#Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36

#https://movie.douban.com/top250?start=0

for page in range(50):
   
    url = 'http://www.dianping.com/shanghai/ch10/p'+str(page+1)
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
    for all_item in all_div:
        print(all_item['href'], end=',')
        print(all_item.img['title'], end=',')
        
        req = urllib.request.Request(url=all_item['href'], headers=headers)
        request_c = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(request_c, 'html.parser') #解析HTML
        #tag = soup.find_all("class", 'expand-info address')
        #tag.p.a.get_text()
        types = soup.find(attrs={"id":"reviewCount"}).string
        print('评论：', types)
    #soup = str(soup)#转换成字符串
    #types = soup.findall(attrs={"class":"shop-list"}).string
    #all_div = soup.find_all("div", class_="pic")
    #all_div = soup.select('.pic')
    #print(all_div)
    
    #f = open("song3.txt", 'a', encoding='utf-8')
    #f.write(str(soup)) 
    
   



print('爬取完毕！')
