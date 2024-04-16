# Subject           Observer
# ConcreteSubject   ConcreteObserver
# Subject   维护一系列Observer对象，在更新时，notify每个Observer
# Subject   提供attach detach notify方法
# Observer  提供update方法
# 例子：
#   1，按钮监听事件
#   2，组队游戏击杀通知
#       5V5 A队 A1~A5 B队 B1~B5
#       A1 attach同队的其他四个队友，attach敌人五个
#       A1击杀B1时，分队伍通知这其他玩家
# 举例 3V3游戏
class Player:
    def __init__(self) -> None:
        self.ally = []
        self.enemy = []
    def attach_ally(self,player):
        ...
    def attach_enemy(self,player):
        ...
    def detach_ally(self,player):
        ...
    def detach_enemy(self,player):
        ...

    def notify_ally(self,msg):
        ...
    def notify_enemy(self,msg):
        ...

    def system_info(self,msg):
        print(f'{self.name} 收到系统消息：{msg}')
class APlayer(Player):
    def __init__(self,name) -> None:
        super().__init__()
        self.name = name
    def attach_ally(self, player):
        self.ally.append(player)
    def attach_enemy(self, player):
        self.enemy.append(player)
    def kill(self,enemy):
        self.notify_ally(f'恭喜！您的队友 {self.name} 击杀敌人 {enemy}!')
        self.notify_enemy(f'警告！您的队友 {enemy} 被敌人 {self.name} 击杀!')
    def notify_ally(self,msg):
        for p in self.ally:
            p.system_info(msg)
    def notify_enemy(self,msg):
        for p in self.enemy:
            p.system_info(msg)
class BPlayer(Player):
    def __init__(self,name) -> None:
        super().__init__()
        self.name = name
    def attach_ally(self, player):
        self.ally.append(player)
    def attach_enemy(self, player):
        self.enemy.append(player)
    def kill(self,enemy):
        self.notify_ally(f'恭喜！您的队友 {self.name} 击杀敌人 {enemy}!')
        self.notify_enemy(f'警告！您的队友 {enemy} 被敌人 {self.name} 击杀!')
    def notify_ally(self,msg):
        for p in self.ally:
            p.system_info(msg)
    def notify_enemy(self,msg):
        for p in self.enemy:
            p.system_info(msg)

if __name__=='__main__':
    # 创建玩家
    # 玩家既是观察者Observer，又是主题Subject
    a1 = APlayer('玩家1')
    a2 = APlayer('玩家2')
    a3 = APlayer('玩家3')
    b1 = BPlayer('玩家4')
    b2 = BPlayer('玩家5')
    b3 = BPlayer('玩家6')
    
    A = [a1,a2,a3]
    B = [b1,b2,b3]

    # 添加监听
    for player in A:
        for ally in A:
            if player!=ally:
                player.attach_ally(ally)
        for enemy in B:
            player.attach_enemy(enemy)
    for player in B:
        for ally in B:
            if player!=ally:
                player.attach_ally(ally)
        for enemy in A:
            player.attach_enemy(enemy)
    
    # print("\033[31mThis is red text\033[0m")
    print('\033[31mA1 击杀 B1\033[0m')
    a1.kill(b1.name)
    print("\033[31mB2 击杀 A2\033[0m")
    b2.kill(a2.name)