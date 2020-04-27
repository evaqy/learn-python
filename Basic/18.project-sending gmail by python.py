#实现发送邮件功能，要求同时发送给多个用户且包含邮件头

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( Header(name, 'utf-8').encode(), addr))

try:
    # 输入Email地址和口令:
    from_addr = input('Your gmail Address: ')
    password = input('Your gmail Password: ')
    # 输入SMTP服务器地址:
    #smtp_server = input('请输入邮箱服务器地址SMTP server: ')
    # 输入收件人地址:
    to_addr = []

    while True:
        a=input('请输入收件人邮箱：')
        to_addr.append(a)
        b=input('是否继续输入，n退出，任意键继续：')
        if b == 'n':
            break

    content = '''
    Dear All,
        Good morning!
        This is a testing email sending by python.
        Let's see how it works.
    '''

    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = _format_addr(u'Your Name <%s>' % from_addr)
    msg['To'] = _format_addr(u'Receiver Name <%s>' % to_addr)
    msg['Subject'] = Header(u'A testing email sent by Python', 'utf-8').encode()

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()#enable security
    server.login(from_addr, password)

    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()
    print('Success! Email Sent!')
except:
    print('Email failed to send.')

    
