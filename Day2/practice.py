name = input("请输入要学生姓名：")
s1 = input('上次成绩：')
s1 = float(s1)#input的数据是字符串类型，要强制类型转换
s2 = input('这次成绩：')
s2 = float(s2)
growth = ((s2-s1)/s1)*100
print('%s,成绩提高了%.2f%%'%('小米',growth))