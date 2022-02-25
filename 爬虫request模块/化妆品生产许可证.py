#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2022/2/14 15:58
# @Author  : wmj
# @project    : 化妆品生产许可证.py
# @Email   : 1136558177@qq.com
# 请求每个企业化妆品详情页
# 注：1.在首页对应的信息是通过ajax请求取到的2.只有企业名称，没有企业的详细信息，但有ID3.
# 4.通过对详情页url观察，url的域名一样，只有参数（ID值）不一样，5.id值从ajax请求中获取，-域名和id值拼接出一个完整的url
# 通过转包工具
# http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById对应企业详情页请求
# http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList实际请求
# 观察知post请求url一样。参数id不同、因此批量获取多家企业id后，就可以将id和url组合请求企业详情页
import requests
import  json
if __name__ == '__main__':
    # 建议的化妆品信息服务平台信息爬取
    # url='http://scxk.nmpa.gov.cn:81/xk/'
    # header={
    #     'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 98.0.4758.80Safari / 537.36Edg / 98.0.1108.43'
    # }
    # page_text =requests.get(url=url,headers=header).text
    # with open('./5化妆品许可证.html','w',encoding='utf-8') as fp:
    #     fp.write(page_text)
    # 爬取企业详情页
    # 批量获取参数id
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    header = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 98.0.4758.80Safari / 537.36Edg / 98.0.1108.43'
    }
    id_list = []  # 存储企业的id数组
    all_data_list = []  # 存储所有的企业详情数据
    # 参数的封装
    for page in range(1,6):#实际爬取范围1-5页
        page=str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': ' ',
            'conditionType': '1',
            'applyname': ' ',
            'applysn': ' ',
        }
        print(page)
        json_ids=requests.post(url=url,headers=header,data=data).json()
        for dic in json_ids['list']:#循环
            id_list.append(dic['ID'])#将循环字典中的id字段添加进id_list集合
    print(id_list)
    #批量获取了id，接着获取企业详情数据
    post_url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data_id={#字典
        'id':id
        }
        detal_json=requests.post(url=post_url,headers=header,data=data_id).json()
        # print(detal_json)
        all_data_list.append(detal_json)#循环存储金list
    #持久化存储
    fp=open('./allData化妆品详情页.json','w',encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)
    print("over")
    #以上仅是单页爬取，以下加入分页操作
    #将page后面参数设置成循环即可，将同时整体变量调整到外部，仅用循环变量将所要爬取的企业id添加到id——list中
