# module A module B
# B要使用A的功能（部分或全部）
# B不想修改A的内容
# B设计Adapter，让它来做调解工作
# 
# Adapter类型：
#   类Adapter（通过继承）
#   组合Adapter（self.A = A）
# 
# 例子：
#   1 第三方库的二次包装
#   2 js，对原生axios进行包装
#   3 java对文件流读写包装fileUtil
# 在不经意间，为了方便使用，简化操作，我们已经学会Adapter
# 本次例子：
#   游戏：人、兽
#   兽人化：兽调用人的部分攻击特性
#   拟兽化：人调用兽的部分攻击特性

from abc import abstractmethod
class BaseOperation:
    @abstractmethod
    def attack():
        ...
    @abstractmethod
    def move():
        ...
    @abstractmethod
    def skill():
        ...

class Animal:
    def angry(self):
        print('狂暴化：Power X 2 Speed X 2！持续时间1min！')
    def attack(self):
        print('攻击：猛兽扑击！！！')
    def move(self):
        print('游走：兽隐潜行...')
    def skill(self):
        print('技能：杀气震慑~~！')

class Person:
    def calm(self):
        print('强制冷静，Hp +100 Dodge X 2！持续时间1min！')
    def attack(self):
        print('攻击：截击技！！！')
    def move(self):
        print('游走：迷踪步...')
    def skill(self):
        print('技能：弱点识破~~！')
    
# 兽人化适配器
class AnimalAdapter1(Animal):
    def orcify_attack(self):
        super().attack()
    def orcify_move(self):
        super().move()    
class AnimalAdapter2():
    def __init__(self) -> None:
        self.Animal = Animal()
    def orcify_attack(self):
        self.Animal.attack()
    def orcify_move(self):
        self.Animal.move()
# 拟兽化适配器 zoomorphism
class PersonAdapter1(Person):
    def zoomorphism_attack(self):
        super().attack()
    def zoomorphism_move(self):
        super().move()    
class PersonAdapter2():
    def __init__(self) -> None:
        self.Person = Person()
    def zoomorphism_attack(self):
        self.Person.attack()
    def zoomorphism_move(self):
        self.Person.move()

# 半兽人
class Orcs(Person):
    def __init__(self,orcify_adapter) -> None:
        self.orcify = False
        self.orcify_adapter = orcify_adapter
    def orcifying(self):
        self.orcify = True
        print('兽化！！！')
    def calm(self):
        super().calm()
    def attack(self):
        self.orcify_adapter.attack() if self.orcify else super().attack()
    def move(self):
        self.orcify_adapter.move() if self.orcify else super().move()
    def skill(self):
        super().skill()
    
if __name__=='__main__':
    adapter = AnimalAdapter1()
    orc = Orcs(adapter)
    orc.attack()
    orc.move()
    orc.skill()
    orc.orcifying()
    orc.attack()
    orc.move()
    orc.skill()
    