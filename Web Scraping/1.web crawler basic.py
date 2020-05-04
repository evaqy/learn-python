import requests

#1 请使⽤request s爬取⽂章，开掘⼀座⽂学理论富矿 并是⽤open⽅法将爬取的数据写⼊⽂件data.txt中
# url = 'https://baijiahao.baidu.com/s?id=1661382527708632196&wfr=spider&for=pc'
url = 'https://baijiahao.baidu.com/s?id=1661382527708632196&wfr=spider&for=pc'
response = requests.get(url)
data = response.content
with open ('data.txt','wb') as text:
    text.write(data)

#2 请使⽤requests请求百度logo图⽚ 并且使⽤open⽅法将图⽚保存下来
url = 'https://www.baidu.com/img/bd_logo1.png'
response = requests.get(url)
baidulogo = response.content
with open ('pic.png','wb') as picture:
    picture.write(baidulogo)