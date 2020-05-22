#for...in循环求1加到100
#用range(n)生成0到n-1的整数序列，再用list()强制转换成list
sum = 0
for i in list(range(101)):
    sum = sum+i
print(sum)


#while循环求1加到100
sum1 = 0
n = 0
while(n<=100):
    sum1 = sum1+n
    n = n+1
print(sum1)

#请利用循环依次对list中的每个名字打印出Hello, xxx!
L = ['Bart', 'Lisa', 'Adam']
for i in L:
    print('Hello,'+i+"!")