'''
原型：提供克隆，例子：游戏小兵，文件夹复制
'''
class Soldier:
    def __init__(self,type='siege soldier',icon='🤖',hp=30,power=5,shield=5,speed=10,dodge=0) -> None:
        self.type = type
        self.icon = icon
        self.hp = hp
        self.power = power
        self.shield = shield
        self.speed = speed
        self.dodge = dodge
    def __str__(self) -> str:
        return f'soldier type:{self.type} {self.icon}\n' + \
                f'\tsoldier hp:'+'❤'*self.hp + '\n' + \
                f'\tpower : {self.power} \t shield : {self.shield} \n' + \
                f'\tspeed : {self.speed} \t dodge : {self.dodge} \n'    
    def clone(self):
        return Soldier(self.type,self.icon,self.hp,self.power,self.shield,self.speed,self.dodge)

soldier_siege = Soldier()
print(soldier_siege)

soldier_sword = soldier_siege.clone()
soldier_sword.type = 'sword soldier'
soldier_sword.icon = '🗡'
print(soldier_sword)

