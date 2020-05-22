#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
#要创建一个set，需要提供一个list作为输入集合
s = set([1,2,3])
print(s)#传入的参数[1, 2, 3]是一个list，而显示的`{1, 2, 3}`只是告诉你这个set内部有1，2，3这3个元素

#重复元素在set中自动被过滤
s = set([1,1,2,2,3,3,4,4])
print(s)#{1,2,3,4}

#通过`add(key)`方法可以添加元素到set中，可以重复添加，但不会有效果
s.add(10)
print(s)#{1, 2, 3, 4, 10}
s.add(2)
print(s)#{1, 2, 3, 4, 10}

#通过`remove(key)`方法可以删除元素
s.remove(10)
print(s)#{1, 2, 3, 4}

#set中的交并补
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1&s2)#{2, 3}
print(s1|s2)#{1, 2, 3, 4}
