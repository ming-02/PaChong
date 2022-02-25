# 爬取搜狗首页#
# ctrl+alt+l自动换行
import requests
if __name__ == '__main__':
    #step1:指定URl
    url='https://www.sogou.com/'
    #2：发起请求（get返回一个响应对象）
    response=requests.get(url=url)
    #3:获取响应数据(.text返回字符串形式的相应数据
    page_text=response.text
    print(page_text)
    #4:持久化存储(fp 别名）
    with open('./sogou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print("爬取数据结束！")