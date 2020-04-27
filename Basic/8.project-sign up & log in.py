# 1.
# 格式化输出：格式符%后面有一个字母，这个字母用来控制数据显示的类型。【%s】就是占住这个位置，将变量转换成字符串。
# %s 字符串 %f 浮点数 %d 整数

# 2.完成登入系统
user_dict = {'marry':12345, 
             'peter':23456, 
             'john':34567}

#Define Functions
def login():
    name = input('请输入用户名： ')
    password = int(input('请输入密码： '))

    if name in user_dict.keys():
        if user_dict[name] == password:
            print('登陆系统成功')
        else:
            print('密码输入错误,请重新登陆')
            login()
    else:
        choice = input('用户名不存在，请输入q回到首页选择注册:')
        if choice == 'q':
            register()

def register():
    name = input('请输入用户名： ')
    password = int(input('请输入密码： '))

    if name not in user_dict.keys():
        user_dict[name] = password
        print('注册成功')
    else:
        choice = input('该用户已存在，请输入q回到首页选择登陆: ')
        if choice == 'q':
            login() 

def respond(userinput):
    choice = int(userinput)
    if choice == 1:
        login()
    elif choice == 2:
        register()
    else:
        print('欢迎下次使用')
    

#The main program
start = input('''
    ======登入系统======
    1.登入
    2.注册
    3.退出  
    ''')
#start==1  or start==2 or start==3
respond(start)