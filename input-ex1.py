money = int(input('请输入地铁卡余额：'))

if money<5:
    print('余额不足请及时充值，不能乘车')

elif money>15:
    print('输出余额充足，请放心乘车')

else:
    print(money)