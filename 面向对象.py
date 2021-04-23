'''
类的属性是静态的，是描述性的；类的方法是动态的，是具体能做什么的。
类下的方法，一定要加self

'''
#创建类
# class Washer():
#     #创建类下的方法
#     def wash(self):
#         print(f"haier洗衣机的宽度是{self.width}")
#         print(f"haier洗衣机的高度是{self.hight}")#类里面获取实例属性
#
# #创建对象,创建对象的过程也叫实例化对象
# haier= Washer()
# haier2=Washer()
# #对象调用类下的方法
# #haier.wash()
#
# #类的外面给类添加属性并被对象获取
# haier.width=500
# haier.hight=800
# # # print(f"haier洗衣机的宽度是{haier.width}")
# # # print(f"haier洗衣机的高度是{haier.hight}")
# haier.wash()
# # haier2.wash()#不能直接调用对象1的属性

#魔法方法_init_(self)
# class washer():
#     def __init__(self):
#         self.width=500
#         self.height=800 #写死的方法
#     def wash(self):
#         print(f"{self.width}")
#         print(f"{self.height}")
# haier1=washer()
# haier1.wash()

#带参数的_int_(self)
class Washer():
    def __init__(self,width,heigth):
        self.width=width
        self.height=heigth

    def wash2(self):
        print(f"{self.width}")
        print(f"{self.height}")
    # 如果类定义了 __str__ ⽅法，那么就会打印从在这个⽅法中 return 的数据。
    def __str__(self):
        return f"宽度{self.width}"
    #当删除对象时，python解释器也会默认调⽤ __del__() ⽅法
    # def __del__(self):
    #     print("我被删除了")

haier2=Washer(10,20)
haier3=Washer(20,50)
print(haier3)
#haier2.wash2()
#haier3.wash2()
#print(haier3)
#del haier3
#print(haier3)



