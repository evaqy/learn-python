#实现⽤cookie请求获取⼈⼈⽹⾸⻚的rp信息
# url = 'http://www.renren.com/'

import requests
from bs4 import BeautifulSoup

url_login = "https://lp.open.weixin.qq.com/connect/l/qrconnect?uuid=071sQI6FtTi8Xse-&last=404&_=1589914522709"
rp_url = "http://www.renren.com/974469089"

headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}

login_data = {
    'uuid': '071sQI6FtTi8Xse-',
    'last': '404',
    '_': '1589914522709',
}
session = requests.session()
login_response = session.post(url=url_login, headers=headers, data=login_data)
#print(login_response)
cookie = login_response.cookies

rp_response = session.get(url=rp_url, headers=headers, cookies=cookie)
#print(rp_response)
content = rp_response.text
html = BeautifulSoup(content, 'html.parser')
rp = html.find('a', class_='for_content')
print(rp)






