#1 
x = int(input('请输入学生的成绩'))

def score(x):
    if x>=90:
        print('A')
    elif 60<x<=89:
        print('B')
    elif x<60:
        print('C')

score(x)

#2
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

caculator(num1,num2)