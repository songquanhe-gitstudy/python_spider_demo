#!/usr/bin/python3
#-*- coding:utf-8 -*-
import requests,sys #python Http客户端库，编写爬虫和测试服务器响应数据经常会用到
import re
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request


#参考网址：http://blog.csdn.net/u010154424/article/details/52273868

print("正在从豆瓣电影中抓取数据...")

#Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36

#https://movie.douban.com/top250?start=0



for page in range(50):
   
    url = 'http://www.dianping.com/shanghai/ch10/p'+str(page)
    print('--------------------------------正在爬取第'+str(page+1)+'页数据----------------------------------')

    
    headers = {'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'} 
    req = urllib.request.Request(url=url, headers=headers)  
    html = urllib.request.urlopen(req).read()

    #html = requests.get(url)#根据URL网址获取网页的源代码
    html.raise_for_status()

    soup = BeautifulSoup(html, 'html.parser') #解析HTML
    #soup = str(soup)#转换成字符串
    #types = soup.findall(attrs={"class":"shop-list"}).string
    #all_div = soup.find_all("div", class_="pic")
    #all_div = soup.select('.pic')
    #print(all_div)
    
    f = open("song3.txt", 'a', encoding='utf-8')
    f.write(str(soup))
  
       
   



print('爬取完毕！')
