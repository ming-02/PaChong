#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2022/2/12 17:43
# @Author  : wmj
# @project    : 肯德基餐厅查询.py
# @Email   : 1136558177@qq.com
import requests
import json
if __name__ == '__main__':
    url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    search=input("请输入地址")
    param={
        'cname':'',
        'pid':'',
        'keyword': search,
        'pageIndex': '1',
        'pageSize': '10'
    }
    header={
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 98.0.4758.80Safari / 537.36Edg / 98.0.1108.43'
    }
    response=requests.post(url=url,params=param,headers=header)
    list_data=response.json()
    fp=open('./4肯德基.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)
    # page_text = response.text
    # with open('4肯德基.json','w',encoding='utf-8') as f:
    #     f.write(page_text)
    print('over')