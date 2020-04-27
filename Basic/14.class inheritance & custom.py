# 1. 定义一个父类初始化几个属性（属性自定义），定义一个子类继承父类的属性，并添加一些属性，在子类定义一个方法，打印出子类所有属性

class Fruit:
    color = 'red'
    taste = 'sweet'

class Round(Fruit):
    shape = 'round'

    def inquire(self):
        print(self.color,self.taste,self.shape)

apple = Round()
apple.inquire()

#2. 定义一个父类Computer,定义一个子类继承该父类，添加电脑品牌属性，重写颜色和价格属性，并打印。实现无论输入什么颜色都打印红色，价格都是5000

class Computer:
    def __init__(self,color,price):
        self.color = color
        self.price = price 
    
class Apple(Computer):
    def __init__(self,brand):
        self.brand = brand
        self.color = 'red'
        self.price = 5000 

    def output(self):
        print(self.brand,self.color,self.price)

item = Apple('apple')
item.output()

