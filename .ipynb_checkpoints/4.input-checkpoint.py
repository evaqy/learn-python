#1
money = int(input('请输入地铁卡余额：'))

if money<5:
    print('余额不足请及时充值，不能乘车')

elif money>15:
    print('输出余额充足，请放心乘车')

else:
    print(money)

#2
print('''给你10个亿你想干什么，你选哪个？ 
      1.想飞上天和太阳肩并肩。 
      2.在天安门面前开游泳馆。
      3.离开地球去宇宙。
      4.拯救中国足球。''')

hobby = input('来吧输入序号： ')

if hobby=='1':
    print('你最好别下来！')

elif hobby=='2':
    print('别做梦了 可能吗')

elif hobby=='3':
    print('行 拜拜')
    
else:
    print('这个行 有魄力')