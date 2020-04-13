# 1.break & continue区别
# break直接打破循环，continue是结束本次循环后回到开头再次循环至结束

# 2.import time这句话是什么意思
# 将time模块导入

# 3.
for a in [2,1,2,3,4,5,6]:
    if a == 2:
        continue
    elif a == 5:
        break
    else:
        print(a)

# 4.
num = 0
for i in range(1,101):
    if i%2 == 0:
        continue
    else:
        num = num+i
print(num)