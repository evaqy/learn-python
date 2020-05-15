#已给出⽹址请⼤家⾃⾏分析⽹站结构，将下图⽤红框圈出来的部分爬取到本地并写⼊excel表格中,数据取前12条即可。
#url=https://www.shobserver.com/news/list?section=42

import openpyxl
import requests
from bs4 import BeautifulSoup

#创建工作薄
wb = openpyxl.Workbook()
#获取工作薄的活动表
sheet = wb.active
#工作表重命名
sheet.title='shangguan'
#定义表格的每一列的名称
column_name = ['标题','内容','作者及日期']
sheet.append(column_name)

start_url = "https://www.shobserver.com/news/list?section=42&page=42"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}
response = requests.get(url=start_url, headers=headers)
#print(response.status_code)

try:
    if response.status_code == 200:
        bsarticle = BeautifulSoup(response.text, "html.parser")
        article_list = bsarticle.find_all("div", class_="chengshi")
        for article in article_list:
            title=article.find("a")["title"]
            summary=article.find("div", class_="chengshi_wz_m").text
            author=article.find("div", class_="chengshi_wz_f").text.replace(' ','').replace('\n','')
            #print(title,summary,author)
            sheet.append([title, summary, author])     
        wb.save('shangguan.xlsx')
        wb.close()

    else:
        print('网页请求失败')

except Exception as error:
    print(error)