#3. 根据已给⽹址爬取果壳前10⻚标题和对应的⽹址信息
# 地址： https://www.guokr.com/ask/highlight/?page=1
#       https://www.guokr.com/ask/highlight/?page=2
#       https://www.guokr.com/ask/highlight/?page=3

#User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36

#url: https://www.guokr.com/ask/highlight/?page=1

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
}
for page_num in range(1,11): 
    start_url = "https://www.guokr.com/ask/highlight/"
    params = {
        "page":str(page_num)
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
                print(title,q_url)
        else:
            print('网页请求失败')

    except Exception as error:
        print(error)