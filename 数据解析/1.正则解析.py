#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
import os
#需求：爬取糗事百科中糗图板块下所有的糗图图片
if __name__ == "__main__":
    #创建一个文件夹，保存所有的图片
    #if not os.path.exists('./qiutuLibs'):
    #    os.mkdir('./qiutuLibs')

    #url = 'https://www.qiushibaike.com'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    #使用通用爬虫对url对应的一整张页面进行爬取
    #page_text = requests.get(url=url,headers=headers).text
    #with  open('page_text.txt','w',encoding='utf-8')  as  file_obj:
    #    file_obj.write(page_text)
    #使用聚焦爬虫将页面中所有的糗图进行解析/提取
    with  open('page_text.txt','r',encoding='utf-8')  as  f:
        page_text = f.read()
    print('page_text = ')
    print(page_text)
    #ex = '<li class="item typs_multi.*?<img src="(.*?)" alt.*?</li>'
    #ex2 = '<li class="item typs_video.*?<img src="(.*?)" alt.*?</li>'
    ex = '<img src="(.*?)" alt.*?>'
    results = ex
    img_src_list = re.findall(results,page_text,re.S)
    print('img_src_list = ')
    print(img_src_list)
    # print(img_src_list)
    flag = 0
    for src in img_src_list:
        #拼接出一个完整的图片url
        if  src[0:6] != 'https:':
            src = 'https:'+src
        #请求到了图片的二进制数据
        print('src = ')
        print(src)
        img_data = requests.get(url=src,headers=headers).content
        #生成图片名称
        img_name = str(flag)+'.jpg'
        #图片存储的路径
        imgPath = './qiutuLibs/'+img_name
        print('imgPath = ')
        print(imgPath)
        with open(imgPath,'wb') as fp:
            fp.write(img_data)
            print(img_name,'下载成功！！！')
            flag = flag+1
