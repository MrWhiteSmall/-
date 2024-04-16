#          Base
# A1    A2  BaseD<include Base>
#           D1      D2
# （D区别于A，D无法初始就获得，必须依附A）
# 
# 举例：
# 游戏角色，基础职业，转职，主业副业    Base 职业 A 基础职业 D 转职职业     
#                   转职职业无法初始获得，必须依附基础职业
# 游戏武器，基础属性，附魔，二次附魔    Base 武器属性 A 基础属性 D 附魔属性
#                   附魔属性无法初始获得，必须依附基础属性
# 
# 装饰器：在不改变原A的情况下，提供额外的功能，类似于新增装备

# Base 抽象职业
class Career:
    def permission(self):
        ...
# A 具体职业
class Career_warrior(Career):
    def permission(self):
        print('飞檐走壁，近身格挡')
class Career_assassinate(Career):
    def permission(self):
        print('隐秘身形，一击必杀')
class Career_mage(Career):
    def permission(self):
        print('秘法千门，山火林风')
# BaseD 抽象装饰器
class Career_auxiliary(Career):
    def __init__(self,career_main) -> None:
        super().__init__()
        self.career_main = career_main
    def permission(self):
        self.career_main.permission()
        ...
# D 具体装饰器
class Career_merchant(Career_auxiliary):
    def permission(self):
        super().permission()
        print('副业加成：察言观色，巧言令色，低买高卖')  
class Career_dancer(Career_auxiliary):
    def permission(self):
        super().permission()
        print('副业加成：魅影迷魂，俘虏人心，动人恻隐')
class Career_thief(Career_auxiliary):
    def permission(self):
        super().permission()
        print('副业加成：探囊取物，手眼合一，悄无声息')

if __name__=='__main__':
    assassinate = Career_assassinate() 
    career_auxiliary = Career_thief(assassinate)
    career_auxiliary.permission()
