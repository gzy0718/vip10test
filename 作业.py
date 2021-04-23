# 1、打印小猫爱吃鱼，小猫要喝水
# class cat():
#     def __init__(self,eat,drink):
#         self.eat=eat
#         self.drink=drink
#     def __str__(self):
#         return f"小猫爱吃{self.eat},小猫要喝{self.drink}"
# cat1=cat('鱼','水')
# print(cat1)

# 2、小明爱跑步，爱吃东西。
# 1）小明体重75.0公斤
# 2）每次跑步会减肥0.5公斤
# 3）每次吃东西体重会增加1公斤
# 4）小美的体重是45.0公斤
# class person():
#     def __init__(self,name,weigh):
#         self.name=name
#         self.weigh=weigh
#         print(f"{self.name}体重{self.weigh}公斤")
#
#
#     def run(self):
#
#         self.weigh-=0.5
#         print(f"每次跑步后的体重为{self.weigh}")
#
#     def eat(self):
#         self.weigh+=1
#         print(f"每次吃完东西的体重是{self.weigh}")
# xiaoming=person("小明",75)
# xiaoming.run()
# xiaoming.eat()
# xiaomei=person("小美",45.0)



# 3、摆放家具
# 需求：
# 1）.房子有户型，总面积和家具名称列表
#    新房子没有任何的家具
# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
# 3）.将以上三件家具添加到房子中
# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
class Furniture():
    def __init__(self, name, area):
        self.name = name
        self.area = area

class Home():

     def __init__(self, area):
        self.area = area
        self.free_area = area
        self.furniture = []

     def __str__(self):
         return f'房⼦占地⾯积{self.area}, 剩余⾯积{self.free_area}, 家具有{self.furniture}'

     def add_furniture(self, item):
            if self.free_area >= item.area:
                self.furniture.append(item.name)
                self.free_area -= item.area
            else:
                print('家具太⼤，剩余⾯积不⾜，⽆法容纳')
bed = Furniture('双人床',4)
yigui=Furniture('衣柜',2)
canzhuo=Furniture('餐桌',1.5)
jia1 = Home(120)
jia1.add_furniture(bed)
jia1.add_furniture(yigui)
jia1.add_furniture(canzhuo)
print(jia1)





