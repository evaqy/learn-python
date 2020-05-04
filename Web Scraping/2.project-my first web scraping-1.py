#1.请使⽤requests爬取⽂章，开掘⼀座⽂学理论富矿。并要求使⽤BeautifulSoup4提取出⽂本数据，将所有的标签部分去掉。

import requests
from bs4 import BeautifulSoup

# 获取数据
res_article = requests.get('https://baijiahao.baidu.com/s?id=1661382527708632196&wfr=spider&for=pc')
#把网页解析为beautifulsoup对象
bs_article = BeautifulSoup(res_article.text, 'html.parser') 
#查找最小父级标签
items = bs_article.find('div', class_='article-content') 
for item in items:
    print(item.text)



