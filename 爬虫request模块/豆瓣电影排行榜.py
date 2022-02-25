# -*- coding: utf-8 -*-
# @Time    : 2022/2/12 16:13
# @Author  : wmj
# @project    : 豆瓣电影排行榜.py
# @Email   : 1136558177@qq.com
#爬取豆瓣电影排行榜,下拉利用ajax请求自动加载新内容
import requests
import json
if __name__ == '__main__':
    url='https://movie.douban.com/j/chart/top_list'
    param = {
        'type_name': '恐怖',
        'type': '20',
        'interval_id': '100:90',
        'action':'',
        'start':'0',#从库中的第几部电影去取
        'limit':'20',#一次取出的个数
    }
    header={
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 98.0.4758.80Safari / 537.36 Edg / 98.0.1108.43'
    }
    response=requests.get(url=url,params=param,headers=header)
    # page__text=response.text
    # fileName='./豆瓣爬取.html'
    # with open(fileName,'w',encoding='utf-8') as fw:
    #     fw.write(page__text)
    # print("页面抓取over")
    list_data=response.json()
    fp=open('./豆瓣电影.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)#数据转换成json格式
    print("over")