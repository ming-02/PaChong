#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2022/3/13 10:01
# @Author  : wmj
# @project    : xpath解析.py
# @Email   : 1136558177@qq.com
#xpath基础知识
from lxml import etree
if __name__ == '__main__':
    #实例化好了一个etree对象，且将被解析的源码加载到该对象中。
    parser=etree.HTMLParser(encoding='utf-8')
    tree = etree.parse('通用爬虫.html',parser=parser)
    # r=tree.xpath('.html/body/title')#xpath层级定位法
    # r=tree.xpath('/html//title')
    # r=tree.xpath('//div')
    # r=tree.xpath('//div[@class="song"')#选择定位
    r=tree.xpath('//div[@class="song"]/p[3]')#此处为索引，3指的是偏移量，与指针的定位有所不同
    r=tree.xpath('//div[@class="song"]//li[5]/a/text()')[0]
    r=tree.xpath('//li[7]//text()')
    r=tree.xpath('//div[@class="song"]/img/@src')
    print(r)