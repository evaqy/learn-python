# 煎饼果子老师傅配方
class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子配方'
    
    def make_cake(self):
        print('[古法]按照<%s>制作了一份煎饼果子'%self.kongfu)

# 煎饼果子学校配方
class School(object):
    def __init__(self):
        self.kongfu = '现代煎饼果子配方'
    
    def make_cake(self):
        print('[现代]按照<%s>制作了一份煎饼果子'%self.kongfu)

# 大猫掌握了师傅的配方可以制作古法煎饼果子, 也学习到了煎饼果子学校的配方

class Apprentice(Master, School):
    def __init__(self):
        self.kongfu = '猫氏煎饼果子配方'
    
    def make_cake(self):
        self.__init__() #执行本类的__init__()的方法 self.kongfu = '猫氏煎饼果子配方'
        print('[大猫]按照<%s>制作了一份煎饼果子'%self.kongfu)

    def make_old_cake(self):
        Master.__init__(self) #调用父类Master__init__()的方法 self.kongfu = '古法煎饼果子配方'
        print('[大猫]按照[古法]<%s>制作了一份煎饼果子'%self.kongfu)

    def make_new_cake(self):
        School.__init__(self) #调用父类School__init__()的方法 self.kongfu = '现代煎饼果子配方'
        print('[大猫]按照[现代]<%s>制作了一份煎饼果子'%self.kongfu)

BigCat = Apprentice()
BigCat.make_cake()
BigCat.make_old_cake()
BigCat.make_new_cake()




