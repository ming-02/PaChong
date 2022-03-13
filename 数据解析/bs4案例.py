#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2022/3/13 7:55
# @Author  : wmj
# @project    : bs4案例.py
# @Email   : 1136558177@qq.com
# 要求爬取三国演义小说所有的章节标题和内容https://www.shicimingju.com/book/sanguoyanyi.html
import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    # 对首页数据进行爬取
    header = {
        'user-agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 99.0.4844.51Safari / 537.36Edg / 99.0.1150.36'
    }
    url='https://www.shicimingju.com/book/sanguoyanyi.html'
    page_text =requests.get(url=url,headers=header).content
    #Q2乱码问题最有效的办法是将text改换成.content
    #在首页中解析出章节的标题和详情页的url
    #1.实例化beautifulsoup对象，需要将页面源码数据加载到该对象中
    soup =BeautifulSoup(page_text,'lxml')
    #解析章节的标题和详情页的url
    li_list=soup.select('.book-mulu >  ul > li',enconding='utf-8' )#返回的是一个列表
    #获取标题
    with open('./sanguo.txt','w',encoding='utf-8') as  fp:
        for li in li_list:
            title=li.a.text
            detail_url='https://www.shicimingju.com'+li.a['href']
            #对详情页发起请求，解析出章节内容(通过再度请求详情页，对每个详情页的内容进行爬取）
            detail_page_text=requests.get(url=detail_url,headers=header).content
            #解析出详情页相关的章节内容#  Q1:detail_page_text收到404界面
            deatail_soup=BeautifulSoup(detail_page_text,'lxml')
            #捕获第一章节的内容
            div_tag=deatail_soup.find('div',class_='chapter_content')
            content = div_tag.text
            #with open()#不能写在循环里
            fp.write(title+':'+content+'\n')
            print(title+'爬取成功')