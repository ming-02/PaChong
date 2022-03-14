#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/3/13 14:16
# @Author  : wmj
# @project    : xpathanli-58同城.py
# @Email   : 1136558177@qq.com
#需求：爬取58二手房中的额房源信息
import requests
from lxml import etree
if __name__ == '__main__':
    #爬取页面源码数据
    url='https://wh.58.com/ershoufang/'
    header={
        'user-agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 99.0.4844.51Safari / 537.36Edg / 99.0.1150.36'
    }
    page_text=requests.get(url=url,headers=header).text
    fp =open("./58二手车.html",'w',encoding="utf-8")
    fp.write(page_text)
    #数据解析
    tree=etree.HTML(page_text)
    #存储就是li标签对象
    # tree.xpath('//ul[@class="house-list-wrap"]/li')
    # t_list=tree.xpath('./html/body')
    t_list=tree.xpath('//div[@class="list"]//div[@class="property"]')
    # t_list=tree.xpath('//section[@class="list"]/div[@class="property"]/a/div[@class="property-content"]/div[@class="property-content-detail"]/div[@class="property-content-title"]/h3/text()')
    print(t_list)
    for t in t_list:
        title = t.xpath('./a//div[@class="property-content-title"]/h3/text()')
        print(title)