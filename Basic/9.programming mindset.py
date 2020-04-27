#1 输入n个整数，把n个数由小到大输出。
import random
randomlist = random.sample(range(1,500),5)
randomlist.sort()
print(randomlist)

#2 编写程序判断用户输入是否是数字
# def ifSeven():
#     a = input('请输入数字：')
#     if a.isdigit():
#         if int(a) % 7 == 0 or '7' in a: 
#             print('是')
#         else:
#             print('否')
#             ifSeven()
             
#     else:
#         print('不是数字，请重新输入') 
#         ifSeven()

# ifSeven()

# while
def ifSeven(a):
    if a.isdigit():
        if int(a) % 7 == 0 or '7' in a: 
            print('是')
        else:
            print('否')

    elif a == 'done':
        print('完成')

    else:
        print('不是数字，请重新输入') 
        
a = 0
while a != 'done':
    a = input('请输入数字, 或 done 以退出程式：')
    ifSeven(a)