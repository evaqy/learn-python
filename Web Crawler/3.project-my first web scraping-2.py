#2.爬取三国演义每回题⽬，将第⼀回到第⼀百⼀⼗九回的题⽬到爬取到本地。
import requests
from bs4 import BeautifulSoup

# 获取数据
res_headers = requests.get('http://www.shicimingju.com/book/sanguoyanyi.html')
# 解析数据
bs_headers = BeautifulSoup(res_headers.text, 'html.parser')
# 查找最小父级标签
list_headers = bs_headers.find_all('div',class_='book-mulu')
for header in list_headers:
    with open('threekindoms.txt','a', encoding='utf-8') as file:
        file.write(header.text)