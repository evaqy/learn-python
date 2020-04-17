#1
myfile = open(r'test1.txt','w')
myfile.write(b'\xe5\x93\x88\xe5\x96\xbd\xef\xbc\x8c\xe5\xa4\xa7\xe5\xae\xb6\xe5\xa5\xbd'.decode('utf-8'))
myfile.close()

#2
message = '哈喽，小伙伴们，大家好，今后我们要一起好好学习哦'
message_utf = message.encode()

myfile = open(r'text2.text','w')
myfile.write(message)
myfile.write(str(message_utf))
myfile.close()


