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
class person():
    def __init__(self,name,weigh):
        self.name=name
        self.weigh=weigh
        print(f"{self.name}体重{self.weigh}公斤")
    # def __str__(self):
    #     return f"{self.name}爱跑步，{self.name}爱吃东西"

    def run(self):
        # print(f"{self.name}体重{self.weigh}公斤")
        self.weigh-=0.5
        print(f"每次跑步后的体重为{self.weigh}")

    def eat(self):
        self.weigh+=1
        print(f"每次吃完东西的体重是{self.weigh}")
xiaoming=person("小明",75)
xiaoming.run()
xiaoming.eat()
xiaomei=person("小美",45.0)






