#简易网页采集器

#反反爬机制：UA伪装
#UA：User-Agent（请求载体的身份标识）
#门户网站的服务器会检测对应请求的载体身份标识，如果检测到载体身份为某一款浏览器，则视为该请求是正常请求
#若为不正常请求，则视为爬虫，可能被服务器拒绝

#为确保每次请求成功则采用反爬策略。UA策略：让爬虫对应的请求载体身份标识伪装成某一款浏览器
import requests
if __name__ == '__main__':
    # UA伪装
    header={
        'User-Agent':'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 98.0.4758.80Safari / 537.36Edg / 98.0.1108.43'
    }
    url='https://sogou.com/web'
    #处理url携带的参数（单独对参数做处理）：参数封装到字典中
    kw =input('enter a word:')
    param ={
        'query':kw
    }
    #对指定url发起的请求对应的url是携带参的请求
    response =requests.get(url=url,params=param,headers=header)
    page__text = response.text
    fileName=kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
       fp.write(page__text)
    print(fileName,"保存成功！！")