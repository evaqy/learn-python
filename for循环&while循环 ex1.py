# 1.
# for循环和while循环最大的区别就是在于【循环的工作量是否确定】，
# for循环就像ATM依次取钱一样，直到把所有人的钱都取完才下班。
# 但是while循环就像收费站一样，只要【满足条件】就干活，不满足条件不干活。
# for循环次数明确，while循环次数不明确

# 2.
# 使用for从1加到100
x = 0
for i in range(1,101):
     x = x+i
print(x)

# 使用while从1加到100
x = 0
i = 1
while i<101:
    x = x+i
    i= i+1
print(x)

# 3.
# 使用for 1-100 偶数相加
total = sum([i for i in range(1,101) if i%2 == 0])
print(total)

# 使用while 1-100 偶数相加
i = 1
x = 0
while i<101:
    if i%2 == 0:
        x = x+i
    i=i+1
print(x)
