#Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['MH','ZQ']#list
print(classmates)#打印list
print(len(classmates))#打印list长度
print(classmates[0])#打印list中的第一个元素
print(classmates[1])#打印list中的第二个元素
print(classmates[-1])#打印list中的倒数第一个元素
print(classmates[-2])#打印list中的倒数第二个元素

#list是可变的有序表，可随时添加删除元素
classmates.append('Tom')#添加元素到末尾
print(classmates)
classmates.insert(1,'Jerry')#插入元素到指定位置
print(classmates)
classmates.pop()#默认index是-1,即删除末尾元素
print(classmates)
classmates.pop(1)#删除指定索引的元素
print(classmates)
classmates[1] = 'MHandZQ'#直接赋值进行替换
print(classmates)

#list中的元素可以是不同类型
L = [1,0.02,'MJ',True]
print(L)

#list中的元素还可以是其他list
LinL = [1,0.02,'MJ',True,[2,5.0,'ZQ',False]]
print(LinL)
print(len(LinL))#5
print(LinL[4][3])#Flase
N = []#空list
print(len(N))#长度为0
