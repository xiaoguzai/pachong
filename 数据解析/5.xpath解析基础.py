#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from lxml import etree
if __name__ == "__main__":
    #实例化好了一个etree对象，且将被解析的源码加载到了该对象中
    tree = etree.parse('test.html')
    r = tree.xpath('/html/body/div')
    #xpath是通过层级标签进行定位，并且他也只能通过层级标签进行定位
    #最外层为html层，下面一层为body层，然后为div层
    print(r)
    #返回的列表当中存储的为3个element对象
    r = tree.xpath('/html//div')
    print(r)
    #//表示的是多个层级，可以表示从任意位置开始定位
    r = tree.xpath('//div')
    print(r)
    r = tree.xpath('//div[@class="song"]')
    print(r)
    #@class="song"定位到class="song"所对应到的div，这是属性定位
    r = tree.xpath('//div[@class="song"]/p[3]')
    print(r)
    #拿到了苏轼对应的p标签，需要注意的一点是标签是从1开始的
    #索引定位
    r = tree.xpath('//div[@class="tang"]//li[5]/a/text()')[0]
    #div然后跳过ul到li然后到a再取出里面的text(),因为杜牧是存在一个列表中
    #所以需要[0],取得的是标签中直系的内容
    print(r)
    r = tree.xpath('//li[7]//text()')
    #中间需要跳过一个<i>标签获取里面的文本内容
    #这里写成tree.xpath('///li[7]//text()')也可以获得相应的内容
    #//text()标签中非直系的文本内容(所有的文本内容)
    print(r)
    r = tree.xpath('//div[@class="tang"]//text()')
    print(r)
    #获取[@class="tang"]下面所有的text()的内容
    r = tree.xpath('//div[@class="tang"]/text()')
    print(r)
    #这样子获得的是\n以及\t,因为只有\n和\t才属于这个相应的div下面的
    #直系的内容
    r = tree.xpath('//div[@class="song"]/img/@src')
    #获取img下面的src对应的定位值
    print(r)
