#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2022/2/23 15:34
# @Author  : wmj
# @project    : 糗图爬取.py
# @Email   : 1136558177@qq.com
# 爬取糗事百科中囚徒版块下所有的糗图图片（爬取单个图片）
import requests
if __name__ == '__main__':
    #如何为爬取图片数据
    header = {
       ' User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 98.0.4758.102Safari / 537.36Edg / 98.0.1108.56'
    }
    url='http://pic.xiaomingming.org/FileUpload/1696.jpg'
    # img_data=requests.get(url=url,headers=header).text#获得字符串形式的响应数据，json（）返回对象形式的相应数据
    img_data=requests.get(url=url).content#返回二进制数据。图片对应的是二进制的数据
    print(img_data)
    with open('./糗图.jpg','wb') as fp:#持久化存储
        fp.write(img_data)
