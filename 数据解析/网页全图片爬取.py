#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2022/2/23 15:58
# @Author  : wmj
# @project    : 网页全图片爬取.py
# @Email   : 1136558177@qq.com
#爬取某网站的全部图片并存储
#第一页网址https://52sharing.cn/category/book/
#第二页网址https://52sharing.cn/category/book/page/3
import requests
import re
import  os
if __name__ == '__main__':
    # 创建一个文件夹，保存所有的图片
    if not os.path.exists('./爬取图片'):
        os.mkdir('./爬取图片')
    header = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 98.0.4758.80Safari / 537.36Edg / 98.0.1108.43'
    }
    #设置一个通用的URL模板
    url='https://52sharing.cn/category/book/page/%d'
    for pageNum in range(1,3):#分页爬取，可以用参数也可以format具体的形式要看具体的网址请求
        #设置新的url
        new_url=format(url%pageNum)
    # url='https://52sharing.cn/category/book/'单页访问
    #使用通用爬虫爬取对应url的一整张页面
        respsone1=requests.get(url=new_url,headers=header).text
    # with open('./通用爬虫.html','w',encoding='utf-8') as fp:
    #     fp.write(respsone1) #不再需要存储每一个页面，因此略去
    #使用聚焦爬虫对页面中的图片进行解析
    #正则解析
        ex='<div class="focus">.*?src="(.*?)" alt.*?</div>'
        img_src_list=re.findall(ex,respsone1,re.S)#有re.S可以匹配换行符，无则不匹配换行符。re.m是多行匹配.返回值为列表
        print(img_src_list)
        for src in img_src_list:#循环
        # src='https:'+src#完整的图片地址
            img_data=requests.get(url=src,headers=header).content#图片为二进制.请求到图片的二进制数据
        #生成图片名称
            img_name=src.split('/')[-1]#切分成数组，方法后的数组表示取数组中的第几个数据
            img_name=img_name.split('&')[0]
            # print(img_name)
        #图片存储的路径
            imgPath='./爬取图片/'+img_name+'.jpg'
            with open(imgPath,'wb')as fw:
                fw.write(img_data)
                print(img_name+'下载成功')
