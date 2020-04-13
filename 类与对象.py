#1 创建一个类，要求在实例化的时候自动打出你的名字,并且调用类方法run的时候打印出名字，星座，年龄
class Person:
    name = 'john'

    def run(self):
        print('我的名字是%s, 星座是金牛座, 年龄是33岁'%self.name)  

user = Person()
print(user.name)
user.run()

print('*'*30)

#2 创建一个类，初始化两个变量name,age，定义两个类方法分别打印出姓名和年龄
class Person2:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def username(self):
        print('我的名字是%s'%self.name)

    def old(self):
        print('我的年龄是%d'%self.age)

peter = Person2('peter', 23)
peter.username()
peter.old()


