print("本程序用于求BMI指数，判断是否健康")
height = input('请输入身高(m)：')
height = float(height)
weight = input('请输入体重(kg)：')
weight = float(weight)
BMI = weight/height**2
if(BMI<18.5):
    print("过轻")
elif (BMI>=18 and BMI<25):
    print('正常')
elif(25<=BMI<28):
    print('过重')
elif(28<=BMI<32):
    print('肥胖')
elif(BMI>=32):
    print('严重肥胖')
