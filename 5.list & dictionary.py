#1
mv_list = ['西红柿首富','银河护卫队','金刚狼','银河补习班','叶问','狮子王','钢铁侠']
print(mv_list[2:5])

del mv_list[4]
print(mv_list)

mv_list.append('蜘蛛侠')
print(mv_list)

#2
phonebook = {'marry':123, 'peter':456, 'john':789}

# 增加姓名和手机
name = input('请输入姓名')
phone = input('手机号')

phonebook[name]=phone
print(phonebook)

# 删除姓名
del phonebook['marry']
print(phonebook)

# 查询所有用户
print(list(phonebook.keys()))

# 根据姓名查找手机号
print(phonebook['peter'])
