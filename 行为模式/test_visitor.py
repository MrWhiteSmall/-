# Element   Visitor
# Object Structure 包含多个Element
# 每个Element都能接受Visitor，并执行访问者的方法
# Object Structure 能够遍历element并执行其方法
# Object Structure 像一个大房子，里面有很多的element，允许访问者到访，element依次与visitor交谈
# 例子：
#   五行角色 承伤 五行伤害

class ElementHarm:
    def __init__(self,harm) -> None:
        self.harm = harm
class GoldenHarm(ElementHarm):
    def __init__(self, harm) -> None:
        super().__init__(harm)
        self.attribute = '金'
class WoodHarm(ElementHarm):
    def __init__(self, harm) -> None:
        super().__init__(harm)
        self.attribute = '木'
class WaterHarm(ElementHarm):
    def __init__(self, harm) -> None:
        super().__init__(harm)
        self.attribute = '水'
class FireHarm(ElementHarm):
    def __init__(self, harm) -> None:
        super().__init__(harm)
        self.attribute = '火'
class SoilHarm(ElementHarm):
    def __init__(self, harm) -> None:
        super().__init__(harm)
        self.attribute = '土'

class Player:
    def __init__(self,name) -> None:
        self.name = name
        self.element_restraint = {
            '金':'木',
            '木':'水',
            '水':'火',
            '火':'土',
            '土':'金',
        }
    def injury(self,elementHarm:ElementHarm):
        ...
class GoldenPlayer(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.element = '金'
    def injury(self, elementHarm: ElementHarm):
        print(f'{self.name} {self.element} 受到 {elementHarm.attribute} 属性伤害')
        if elementHarm.attribute == self.element_restraint[self.element]:
            print(f'{self.name} 属性克制：受到伤害*2！')
class WoodPlayer(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.element = '木'
    def injury(self, elementHarm: ElementHarm):
        print(f'{self.name} {self.element} 受到 {elementHarm.attribute} 属性伤害')
        if elementHarm.attribute == self.element_restraint[self.element]:
            print(f'{self.name} 属性克制：受到伤害*2！')
class WaterPlayer(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.element = '水'
    def injury(self, elementHarm: ElementHarm):
        print(f'{self.name} {self.element} 受到 {elementHarm.attribute} 属性伤害')
        if elementHarm.attribute == self.element_restraint[self.element]:
            print(f'{self.name} 属性克制：受到伤害*2！')
class FirePlayer(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.element = '火'
    def injury(self, elementHarm: ElementHarm):
        print(f'{self.name} {self.element} 受到 {elementHarm.attribute} 属性伤害')
        if elementHarm.attribute == self.element_restraint[self.element]:
            print(f'{self.name} 属性克制：受到伤害*2！')
class SoilPlayer(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.element = '土'
    def injury(self, elementHarm: ElementHarm):
        print(f'{self.name} {self.element} 受到 {elementHarm.attribute} 属性伤害')
        if elementHarm.attribute == self.element_restraint[self.element]:
            print(f'{self.name} 属性克制：受到伤害*2！')


class Players:
    def __init__(self) -> None:
        self.players = []
    def add_player(self,player:Player):
        self.players.append(player)
    def injury(self,elementHarm):
        for player in self.players:
            player.injury(elementHarm)

if __name__=='__main__':
    p1 = GoldenPlayer('玩家1')
    p2 = WoodPlayer('玩家2')
    p3 = WaterPlayer('玩家3')
    p4 = FirePlayer('玩家4')
    p5 = SoilPlayer('玩家5')

    team_players = Players()
    team_players.add_player(p1)
    team_players.add_player(p2)
    team_players.add_player(p3)
    team_players.add_player(p4)
    team_players.add_player(p5)

    aoe = GoldenHarm(20)
    team_players.injury(aoe)
    aoe = FireHarm(20)
    team_players.injury(aoe)