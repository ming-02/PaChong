#!/usr/bin/python3  
# -*- coding: utf-8 -*-
# @Time    : 2022/2/23 15:03
# @Author  : wmj
# @project    : 正则练习.py
# @Email   : 1136558177@qq.com
#正则表达式的简单练习
import re
if __name__ == '__main__':
    #提取出python
    key='javapythonc++php'
    a=re.findall('python',key)[0]
    print(a)
    #提取hello，world
    key='<html><h1>hellon world<h1></html>'
    b=re.findall('<html>(.*)<h1>',key)[0]#''单引号内的内容为匹配内容
    print(b)
    #提取170
    key='我喜欢身高为170的女孩'
    c=re.findall('\d+',key)#\d匹配的是所有数字
    print(c)#输出结果为['170']
    #提取http：//和https：//
    key='http://www.baidu,com and https://boob.com'
    d=re.findall('https?://',key)#？:问号前的字符可有可无 0次或者1次
    print(d)#['http://', 'https://']
    #提取hello
    key='lalala<html>hello</html>hahah'
    e=re.findall('<[Hh][Tt][Mm][Ll]>(.*)</[Hh][Tt][Mm][Ll]>',key)#匹配[]内任意字符
    print(e)
    #提取hit.
    key='bobo@hit.edu.com'
    f=re.findall('h.*?\.',key)#非贪婪模式，仅匹配一次h
    print(f)
    #匹配sas 和saas
    key='saas and sas and saaas'
    g=re.findall('sa{1,2}s',key)#{m,n}固定出现次数
    print(g)