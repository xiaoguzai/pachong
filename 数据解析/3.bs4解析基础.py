#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
if __name__ == "__main__":
    #将本地的html文档中的数据加载到该对象中
    fp = open('./test.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    print('***1')
    print(soup)
    print('***2')
    print(soup.a) #soup.tagName 返回的是html中第一次出现的tagName标签
    print('***3')
    print(soup.div)
    #find('tagName'):等同于soup.div
    print('***4')
    print(soup.find('div'))  #print(soup.div)
    print('***5')
    print(soup.find('div',class_='song').string)
    print('***6')
    print(soup.find_all('a'))
    print('***7')
    print(soup.select('.tang'))
    print('***8')
    print(soup.select('.tang > ul a')[0]['href'])