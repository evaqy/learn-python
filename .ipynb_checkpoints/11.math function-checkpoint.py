#1 
import math
class Program:
    def __init__(self):
        self.key = 1

    #输入数据
    def BOSS_input(self):
        #设置默认参数
        self.length = int(input('请输入这段路的长度'))
        self.people = int(input('请输入工作人员的总人数'))
    
    #计算工程所需天数
    def calculate_job(self):
        print('计算结果如下：')
        self.team = math.ceil(self.people/5)
        self.day = math.ceil(self.length / self.team / 1)
        print('%d公里的路程，由%d位工作人员修路，则需要%d天完成' %(self.length, self.people, self.day))

    #继续计算或退出程序
    def again(self):
        choice = input('是否继续计算？继续请输入y，输入其他键将结束程序')
        if choice != 'y':
            self.key = 0

    def res(self):
        print('欢迎BOSS使用工程计算小程序')
        while self.key == 1:
            self.BOSS_input()
            self.calculate_job()
            self.again()
        print('工作辛苦了')

pro = Program()
pro.res()

print('*'*10)

#2 
weight = math.ceil(float(input('请输入运输货物的重量kg:可以输入小数')))
def calculate(weight):
    if weight<=5:
        money = 20
    elif weight>5:
        money = 20+(weight-5)*2
    print('运输这批货物的价格为：%d元'%money)
calculate(weight)