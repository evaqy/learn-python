#根据已给出的⽹址爬取衢州的天⽓，爬取⽩天、夜间的温度、阴天或晴天数据具体数据位置⻅下⾯图⽚,红⾊框圈出来的是需要爬取的数据。将爬取到的数据写⼊到发送邮件模板中并定时每天早上⼋点，发送天⽓情况。
#url=http://www.weather.com.cn/weather/101211001.shtml

import requests
from bs4 import BeautifulSoup
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import schedule
import time

#获取天气数据
def get_weather():
    headers = {
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    url = 'http://www.weather.com.cn/weather/101211001.shtml'
    res = requests.get(url,headers=headers)
    if res.status_code == 200:
        res.encoding='utf-8'
        bsdata = BeautifulSoup(res.text, 'html.parser')
        weather = bsdata.find('p', class_='wea')
        temperature = bsdata.find('p', class_='tem')
        return weather,temperature
    else:
        print('请求失败')

#发送邮件
def send_email(weather,temperature,sender,pwd,receiver):

    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr(( Header(name, 'utf-8').encode(), addr))

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()#enable security
        server.login(sender, pwd)

        content = '今天的天气是： ' + weather + temperature
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = _format_addr(u'小明 <%s>' % sender)
        msg['To'] = _format_addr(u'小华 <%s>' % receiver)
        msg['Subject'] = Header(u'今日天气预报', 'utf-8').encode()

        server.sendmail(sender, receiver, msg.as_string())
        return True
    except:
        return False
    server.quit()

                 
#定时
def job():
    print('开始执行一次发送任务')
    weather,temperature = get_weather()
    sender = input('邮箱地址: ')
    pwd = input('邮箱密码: ')
    receiver = input('请输入收件人邮箱：')

    IsSuccess = send_email(weather,temperature,sender,pwd,receiver)   
    while IsSuccess is False:
        print("邮件发送失败，正在尝试重新发送")
        IsSuccess = send_email(weather,temperature,sender,pwd,receiver)
    print('任务完成')

schedule.every().day.at("08:00").do(job) 

while True:
    schedule.run_pending()
    time.sleep(1)