#
# # 单继承
# class shifu():
#     def __init__(self):
#         self.peifang="五香味配方"
#     def jishu(self):
#         print(f"通过{self.peifang}制作煎饼果子")
#
# #多继承
# class school():
#     def __init__(self):
#         self.peifang="香辣味煎饼果子配方"
#     def jishu(self):
#         print(f"通过{self.peifang}制作煎饼果子")
#
# class tudi(shifu,school):#子类和父类有同名属性和方法，默认使用子类的。
#
#     def __init__(self):
#         self.peifang="自创煎饼果子配方"
#         self.__money=200
#
#     def get__money(self):
#         return self.__money
#     def set__money(self,mach):
#         self.__money=mach
#
#     def jishu(self):
#     #     tudi.__init__(self)
#         print(f"通过{self.peifang}制作煎饼果子")
#     def __info_money(self):
#         print(self.peifang)
#     # def shifu_jishu(self):#子类调用父类事，需要再次封装父类方法
#     #     shifu.__init__(self)
#     #     shifu.jishu(self)
#     #
#     # def school_jishu(self):
#     #      school.__init__(self)
#     #      school.jishu(self)
#         super().__init__()
#         super().jishu()
# class tusun(tudi):
#     pass
#
# xiaoming=tudi()
# # print(xiaoming.peifang)#访问实例属性
# xiaoming.jishu()#对象调用实例方法
# # 对象不能访问私有属性和私有方法
# # print(xiaoming.__money)
# # xiaoming.__info_money()
# print(xiaoming.get__money())
# xiaoming.set__money(300)
# print(xiaoming.get__money())
# xiaogang=tusun()
# xiaogang.jishu()
# print(xiaogang.get__money())
# xiaogang.set__money(500)
# print(xiaogang.get__money())
# # 子类无法继承父类的私有属性和私有方法
# # print(xiaogang.__money)
# # 无法访问实例属性__money

#多态

# class dog(object):
#     pass
# class armydog(dog):
#     def work(self):
#         print("追击敌人")
#
# class drugdog(dog):
#     def work(self):
#         print("追查毒品")
#
# class person(object):
#     def work_with_dog(self,dogg):
#         dogg.work()
# a=armydog()
# b=drugdog()
# xiaoliang=person()
# xiaoliang.work_with_dog(a)
# xiaoliang.work_with_dog(b)

#类属性
class dog(object):
    tooth=10
    __tooth1=11
    @classmethod
    def get_tooth(cls):   #类方法--使用私有类属性的时候，会定义类方法
        return cls.__tooth1
    @staticmethod
    def info_print():#静态方法定义
        print("这是狗的类集合")
wangcai=dog()
xiaohei=dog()

dog.tooth=12 #修改类属性
print(wangcai.tooth)
print(xiaohei.tooth)

wangcai.tooth=20 # 不能通过对象修改属性，如果这样操作，实则是创建了⼀个实例属性
print(wangcai.tooth)

result=wangcai.get_tooth()#使用类方法
print(result)

#静态方法使用
wangcai.info_print()# 静态⽅法既可以使⽤对象访问⼜可以使⽤类访问
dog.info_print()


