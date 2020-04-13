#1 请找出以下代码的错误，并修改使其正常运行

def age():
    age = int(input('请输入数字： '))
    if age == 10:
        print('小明今年%d岁了'%age)
    else:
        print('程序结束')
age()

#2 请修改以下代码的错误，并修改使其正常运行（代码实现对列表求和）
list = [1,2,3,4]

def run():
    he = sum(list)
    print(he)
run()