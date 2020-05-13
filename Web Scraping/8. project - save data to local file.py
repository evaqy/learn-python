#根据已给⽹址爬取果壳前10⻚标题和对应的⽹址信息，并将爬取到的数据写⼊到excel表格或则是CSV中。
#url = https://www.guokr.com/ask/highlight/?page=1

import openpyxl
import requests
from bs4 import BeautifulSoup

url = 'https://www.guokr.com/ask/highlight/?page=1'

#创建工作薄
wb = openpyxl.Workbook()
#获取工作薄的活动表
sheet = wb.active
#工作表重命名
sheet.title='guokr'
#定义表格的每一列的名称
column_name = ['标题','网址']
sheet.append(column_name)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}
for i in range(1,11): 
    start_url = "https://www.guokr.com/ask/highlight/"
    params = {
        "page":str(i)
    }
    #print(start_url)
    response = requests.get(url=start_url, headers=headers,params=params)
    try:
        if response.status_code == 200:
            answer = BeautifulSoup(response.text, 'html.parser')
            question_list = answer.find_all("div", class_="ask-list-detials")
            for question in question_list:
                text=question.find('a')
                title=text.text
                q_url=text['href']
            # 把title, q_url写成列表，用append函数多行写入Excel
            sheet.append([title, q_url])
            #最后保存并关闭这个Excel文件       
            wb.save('guokr.xlsx')
            wb.close()
        else:
            print('网页请求失败')

    except Exception as error:
        print(error)
        
