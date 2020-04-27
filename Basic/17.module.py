# 1 总结导入模块的几种方式，并自定义一个计算器程序，延时1秒再返回结果，实现计算器程序执行的时间并打印出计算结果，程序运行开始时间（打印出年月日）及程序运行花费的时间。
# 1）import 模块
#     使用模块中的变量、函数与类：模块.变量名 模块.函数名 模块.类名
#     可以使用import…as…语句更改导入模块的名字
#     导入多个模块时，用逗号隔开：import 模块，模块，模块
# 2) from(模块名)import（指定模块中的部分代码）
#     导入后的指定部分可以直接使用，无需加上模块前缀
# 3）使用if __name__ == '__main__':来指定某个py文件为程序入口。
#     当被指定的某个py文件作为模块导入其他文件时，只会执行mian.py文件中本身代码，不会执行if __name__ == '__main__':后面的代码。

import time
from time import process_time

# Start the stopwatch / counter  
t1_start = process_time()

#程序运行开始时间
ticks = time.time()
localtime = time.localtime(time.time())
localtime = time.asctime( time.localtime(time.time()) )

#定义计算器程序
#定义函数
#加
def add(x,y):
    return x+y

#减
def substract(x,y):
    return x-y

#乘
def multiply(x,y):
    return x*y

#除
def divide(x,y):
    return x/y

#选择计算功能
choice = input('''
    请输入你的选择:
    1.加
    2.减
    3.乘
    4.除
''')

#输入计算数字
num1 = int(input('输入第一个数字: '))
num2 = int(input('输入第二个数字: '))

#主函数
def caculator(x,y):
    if choice == '1':
        print(num1,'+',num2,'=',add(num1,num2))
    elif choice == '2':
        print(num1,'-',num2,'=',substract(num1,num2))
    elif choice == '3':
        print(num1,'*',num2,'=',multiply(num1,num2))
    elif choice == '4':
        print(num1,'/',num2,'=',divide(num1,num2))

#延时1秒再返回结果
time.sleep(1)
caculator(num1,num2)

# Stop the stopwatch / counter 
t1_stop = process_time() 

#打印运行开始时间及花费的时间 
print ("程序开始时间:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
print("程序运行花费的时间:", t1_stop-t1_start) 




#2 定义几个列表（元素全部为数值）并将其按行全部写入csv文件，然后读取文件，并打印

import csv

with open("mytest.csv",'a')  as r:
    writer = csv.writer(r)
    writer.writerow([41,42,43])
    writer.writerow([51,52,53])
    writer.writerow([61,62,63])
print("写入完毕！")

with open("mytest.csv",encoding='utf-8-sig')  as r:
    print("内容如下\n")
    reader = csv.reader(r)
    #使用csv的reader()方法，创建一个reader对象
    for content in reader:
    #遍历reader对象的每一行
        print(content)

print("读取完毕！")