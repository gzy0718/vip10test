'''
类的属性是静态的，是描述性的；类的方法是动态的，是具体能做什么的。
类下的方法，一定要加self

'''
#创建类
class Washer():
    #创建类下的方法
    def wash(self):
        print('我会洗衣服')

#创建对象,创建对象的过程也叫实例化对象
haier= Washer()

#对象调用类下的方法
haier.wash()

#类的外面给类添加属性并被对象获取
haier.width=500
haier.hight=800
print(f"haier洗衣机的宽度是{haier.width}")
print(f"haier洗衣机的高度是{haier.hight}")
