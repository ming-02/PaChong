#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2022/3/14 8:42
# @Author  : wmj
# @project    : xPath-图片下载.py
# @Email   : 1136558177@qq.com
#需求：xpath的图片的下载
from lxml import etree
import requests
import os
if __name__ == '__main__':
    header={
        'user-agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 99.0.4844.51Safari / 537.36Edg / 99.0.1150.36'
    }
    url="https://pic.netbian.com/"
    page_text=requests.get(url=url,headers=header).content
    # page_text.encoding='utf-8'#对响应头进行编码设置
    # response.encoding=respone.apparent_encoding：也是用来解码
    #解析出src属性
    tree=etree.HTML(page_text)
    tr_list=tree.xpath('//div[@class="slist"]/ul/li')
    if not os.path.exists('./4k图片下载'):
        os.mkdir("./4k图片下载")
    for li in tr_list:
        print(li.xpath('./a//img/@src'))
        img_src='https://pic.netbian.com'+str(li.xpath('./a//img/@src')[0])
        img_name=str(li.xpath('./a//img/@alt'))+".jpg"
        # img_name=img_name.encode('iso-8859-1').decode('gbk');#通用处理中文乱码的解决方案
        img_data=requests.get(url=img_src,headers=header).content
        fp = open('./4k图片下载/'+img_name, 'wb')  # 图片用wb
        fp.write(img_data)
        print(img_name,'下载成功')