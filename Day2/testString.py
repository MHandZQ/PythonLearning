#测试转义字符
print('\\')#\
print('I\'m learning \npython')
#I'm learning
#python
print("I\'m \"OK\"")#I'm "Ok"
print('\\\n\\')
#\
#\
print(r'\\\n\\')#\\\n\\，r''表示内部字符串默认不转义

#多行字符串
print('''line1
line2
line3''')

#在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言
print('包含中文的str')

#对于单个字符的编码，Python提供了`ord()`函数获取字符的整数表示，`chr()`函数把编码转换为对应的字符
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))

#Python对`bytes`类型的数据用带`b`前缀的单引号或双引号表示：
#要注意区分`'ABC'`和`b'ABC'`，前者是`str`，后者虽然内容显示得和前者一样，但`bytes`的每个字符都只占用一个字节
x = b'ABC'
print(x)
x = 'ABC'
print(x)

#以Unicode表示的`str`通过`encode()`方法可以编码为指定的`bytes`
print('ABC'.encode('ascii'))#英文字符串'ABC'的ascii编码是b'ABC'
print('中文'.encode('utf-8'))#中文的utf-8编码是b'\xe4\xb8\xad\xe6\x96\x87'

#反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是`bytes`。要把`bytes`变为`str`，就需要用`decode()`方法
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

#要计算`str`包含多少个字符，可以用`len()`函数
print(len(b'ABC'))#3
print(len("ABC"))#3

#格式化
print('Hello,%s'%'World')
print('Hello, %s,you have $%d.'%('MH',10000))
print('%.2f'%3.1415926)#指定保留小数位数
print('Age: %s,Gender: %s'%(25,'M'))#不太确定应该用什么，`%s`永远起作用，它会把任何数据类型转换为字符串
print('growth rate:%d%%'%7)#字符串里面的`%`是一个普通字符,这个时候就需要转义，用`%%`来表示一个`%`

#format
#它会用传入的参数依次替换字符串内的占位符`{0}`、`{1}`……
print('Hello,{0},成绩提高了{1:.2f}'.format('小明',17.1258))#Hello,小明,成绩提高了17.13,保留两位小数，且自动四舍五入
