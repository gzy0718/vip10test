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
class House():
    # def __init__(self,weizhi,mianji,shengyu,jiaju):
    #     self.weizhi=weizhi
    #     self.mianji=mianji
    #     self.shengyu=shengyu
    #     self.jiaju=jiaju

    def shuxing(self):
        print(f"{self}")
    def __str__(self):
        return f'房子位置在{house.weizhi},面积为{house.mianji},剩余面积{house.shengyu},'
class Jiaju():
    def jiajushuxing(self):
        print(f"{self}")
house=House()
house.weizhi='五环'
house.mianji=100
house.shengyu=100
house.jiaju='床'

jiaju1=Jiaju()
jiaju1.name='床'
jiaju1.mianji=10

if

