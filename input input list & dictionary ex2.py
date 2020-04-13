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

