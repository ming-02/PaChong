#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2022/3/10 20:28
# @Author  : wmj
# @project    : bs4解析.py
# @Email   : 1136558177@qq.com
from bs4 import BeautifulSoup
if __name__ == '__main__':
   fp = open("./通用爬虫.html",'r',encoding='utf-8')
   soup = BeautifulSoup(fp,'lxml')
   #print (soup)
   #print(soup.a)#soup.对象中的属性,只返回html中第一次出现的a标签
   print(soup.div)
   #find函数的用法1：等同于soup.tagName返回文本中的第一次出现的标签
   #find函数的属性定位：
   print(soup.find('div'))
   # print(soup.find('div',class_='navbar'))
   print(soup.find_all('a'))
   # print(soup.select('.excerpt'))#可用标签选择器，id选择器等
   #层级选择
   # exampel:print(soup.select('.tang > ul > li > a')[0])
   print(soup.select('.pagination > ul > li > a'))