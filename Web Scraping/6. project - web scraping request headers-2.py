#2 请⾃动获取⽤户输⼊的关键字完成搜索 360的关键词接⼝是q 
# 统计出输⼊关键字后爬取下来数据的数量,通过捕获异常的⽅法
# 如果爬取失败输出爬取失败字样
# 地址：http://so.com/s

import requests
from bs4 import BeautifulSoup

url= "http://so.com/s"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}

parameters = {
    "ie": "utf-8",
    "fr": "none",
    "src": "home_suggst_personal",
    "q": input("请输入你想搜索的内容:"),
    "eci": "nlpv: shbt_aa_8"
}

try:
    response=requests.get(url=url,params=parameters,headers=headers)
    if response.status_code == 200:
        info=BeautifulSoup(response.text,'html.parser')
        tag=info.find('span', class_="nums")
        print(tag.text)
        
    else:
        print('网页请求失败')

except Exception as error:
    print(error)



