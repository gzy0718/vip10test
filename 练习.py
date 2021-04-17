# class Teacher():
#     def __init__(self,name,sex,lesson):
#         self.name=name
#         self.sex=sex
#         self.lesson=lesson
#     # def lst(self):
#     #     print("可以教学")
#     def __str__(self):
#         return f"老师名字是{self.name}，性别{self.sex},教的是{self.lesson}课"
#
# teacher1= Teacher("tom","男","数学")
# teacher2= Teacher("lily","女","英语")
# # teacher1.lst()
# print(teacher1)
# # teacher2.lst()
# print(teacher2)

'''
类：房子类；家具类
属性：房子（地理位置，占地面积，剩余面积，家具列表）
    家具（家具名称，家具占地面积）
方法：房子（容纳家具）
print（显示房屋信息）
'''
# class Jiaju():
#     def __init__(self,name,mianji1):
#         self.name=name
#         self.mianji1=mianji1
#
# class House():
#     def __init__(self,weizhi,mianji,shengyu,jiaju):
#         self.weizhi=weizhi
#         self.mianji=mianji
#         self.shengyu=mianji
#         self.jiaju=[]
#
#     def __str__(self):
#         return f"房子位置在{self.weizhi}，占地面积{self.mianji}，剩余面积{self.shengyu}，家具有{self.jiaju}"
#     def fun(self,iteam):
#         if self.shengyu >= iteam.mianji1:
#             self.jiaju.append(iteam.name)
#             self.shengyu -= iteam.mianji1
#         else:
#             print("面积太大了，放不下")
# jia=House("五环",100,100,[])
# jiaju=Jiaju("床",5)
# print(jia)
# jia.fun(jiaju)
# print(jia)


class Furniture():
    def __init__(self, name, area):
 # 家具名字
        self.name = name
 # 家具占地⾯积
        self.area = area

class Home():

     def __init__(self, address, area):

     # 地理位置
        self.address = address
     # 房屋⾯积
        self.area = area
     # 剩余⾯积
        self.free_area = area
     # 家具列表
        self.furniture = []

     def __str__(self):
         return f'房⼦坐落于{self.address}, 占地⾯积{self.area}, 剩余⾯积{self.free_area}, 家具有{self.furniture}'

     def add_furniture(self, item):
     #容纳家具
            if self.free_area >= item.area:
                self.furniture.append(item.name)
 # 家具搬 ⼊后，房屋剩余⾯积 = 之前剩余⾯积 - 该家具⾯积
                self.free_area -= item.area
            else:
                print('家具太⼤，剩余⾯积不⾜，⽆法容纳')
bed = Furniture('双人床',6)
jia1 = Home('北京', 1200)
print(jia1)
jia1.add_furniture(bed)
print(jia1)




