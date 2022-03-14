#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 9:53
# @Author  : wmj
# @project    : xpath-城市名称.py
# @Email   : 1136558177@qq.com
#爬取所有城市名称
import requests
from lxml import etree
if __name__ == '__main__':
    header = {
        'user-agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 99.0.4844.51Safari / 537.36Edg / 99.0.1150.36'
    }
    url = "https://www.aqistudy.cn/historydata/"
    page_text = requests.get(url=url, headers=header).content

    tree=etree.HTML(page_text)
    tr_hot_city=tree.xpath('.//div[@class="bottom"]/ul/li')
    all_city_name=[]
    for li in tr_hot_city:
        hot_city_name=li.xpath('./a/text()')[0]
        print(hot_city_name)
        all_city_name.append(hot_city_name)
    tr_all_city=tree.xpath('.//div[@class="bottom"]/ul/div[2]/li')#获取到全部的li对象
    for li in tr_all_city:
        all_city=li.xpath('./a/text()')[0]
        all_city_name.append(all_city)
    print(all_city_name,len(all_city_name))