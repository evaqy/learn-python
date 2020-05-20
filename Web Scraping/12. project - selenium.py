#请使⽤selenium⾃动打开github⽹站，完成⾃动输⼊账号和密码然后完成登录，界⾯显示主⻚⾯即可。

from selenium import webdriver
import time

driver = webdriver.Chrome('/Library/Developer/CommandLineTools/SDKs/MacOSX10.14.sdk/usr/bin/chromedriver')
driver.get('https://github.com/login')
time.sleep(2)

########登录#########
#输入用户名
login_user = driver.find_element_by_id("login_field")
user = input("请输入用户名：")
login_user.send_keys(user)
#输入密码
login_password = driver.find_element_by_id("password")
pwd = input("请输入密码：")
login_password.send_keys(pwd)
#点击登录
login_confirm = driver.find_element_by_name("commit")
login_confirm.click()