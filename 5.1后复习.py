## 1-异常

#语法：
try:
    print(a)
except:
    print('出现异常执行的代码')

#捕获异常信息
try:
    print(a)
except (NameError) as result:
    print(result)

#捕获所有异常
try:
    print(a=1)
except Exception as result:
    print(result)

#没有异常执行的代码else
try:
    print(1)
except Exception as result:
    print(result)
else:
    print('没有异常执行的部分')

#无论是否有异常，都需要执行的部分
try:
    print(a)
except Exception as result:
    print(result)
finally:
    print("有没有异常，都要执行这段话")

## 2—面向对象基础
'''
1.用类创建一个对象
2.类有属性和方法
3.语法：
class 类名():
    代码
4.类名遵循大驼峰命名习惯
5.self是调用该函数的对象
6.对象属性既可以在类外⾯添加和获取，也能在类⾥⾯添加和获取。
'''
#类的使用
class Washer():
    def wash(self):
        print('这是一个实例方法')
#创建对象-对象名=类名()
haier1=Washer()
#当前对象在内存中存储地址
print(haier1)
#对象调用实例方法
haier1.wash()
#类外面 添加 对象属性-对象名.属性名=值
haier1.width=500
haier1.height=800
#类外面 获取 对象属性-对象名.属性名
print(f'haier1洗⾐机的宽度是{haier1.width}')
print(f'haier1洗⾐机的⾼度是{haier1.height}')
#类里面 获取 对象属性
# #定义类
# class Washer():
#     def print_info(self):
# #类⾥⾯获取实例属性
#         print(f'haier1洗⾐机的宽度是{self.width}')
#         print(f'haier1洗⾐机的⾼度是{self.height}')
# # 创建对象
# haier1 = Washer()
# # 添加实例属性
# haier1.width = 500
# haier1.height = 800
# haier1.print_info()




