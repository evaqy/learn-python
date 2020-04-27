#程序开始根据输入内容判断打印老师信息还是学生信息
#定义一个年级类，用来返回年级，定义一个班级类返回班级，定义一个老师类继承年级和班级类
#在老师类中定义一个run方法，在调用时可以打印出老师所在的年级，班级，学科，姓名信息，定义一个学生类继承年级和班级类，在该类中定义一个run方法用来打印学生的姓名，年龄，年级，班级信息。
while True:
    identity = int(input('''
        请输入您是:
        1 老师
        2 学生
        3 退出程序
        '''))

    class Grade(object):
        def __init__(self):
            self.grade = "高一"

    class Class(object):
        def __init__(self):
            self.number = 2

    if identity == 1:
        class Teacher(Grade,Class):
            def __init__(self):
                Grade.__init__(self)
                Class.__init__(self)
                self.name = "李宗盛"
                self.subject = "音乐"

            def run(self):
                print("老师%s，在%s%d班教%s"%(self.name,self.grade,self.number,self.subject))
            
        teacher = Teacher()
        teacher.run()

    elif identity == 2:
        class Student(Grade,Class):
            def __init__(self):
                Grade.__init__(self)
                Class.__init__(self)
                self.name = "周杰伦"
                self.age = 18

            def run(self):
                print("学生%s，今年%d岁，在%s%d班"%(self.name,self.age,self.grade,self.number))
            
        student = Student()
        student.run()
    
    else:
        break
