#Python内置了字典：dict的支持，dict全称dictionary，
#在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
d = {'孟行':96,'周琪':99,'桑菁':96}#大括号声明字典
print(d['孟行'])#96

#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['王富鑫'] = 88
print(d['王富鑫'])

#由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉
d['Jerry'] = 90
d['Jerry'] = 99
print(d['Jerry'])#99

#如果key不存在，dict就会报错
#print(d['Tom'])#KeyError: 'Tom'就是Tom这个key不存在

#要避免key不存在的错误，有两种办法:
#一是通过in判断key是否存在
print('Tom' in d)#False
#二是通过dict提供的get()方法，如果key不存在，可以返回None
print(d.get('Tom'))#None

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除
print(d)#{'孟行': 96, '周琪': 99, '桑菁': 96, '王富鑫': 88, 'Jerry': 99}
d.pop('孟行')
print(d)#{'周琪': 99, '桑菁': 96, '王富鑫': 88, 'Jerry': 99}