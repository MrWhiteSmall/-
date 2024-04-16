# Handler
# ConcreteHandler
# Handler包含nextHandler
# H能处理则自行处理，不能则让nextHandler处理，直到某一个H处理为止
# 例子：
#   1，向上审批（公司）请假事宜
#   2，向下PUA（公司）层层洗脑
#   3，游戏技能（被动）触发
#       受到伤害 >= 当前血量+护盾 免除致命伤
#               >= 1/2 HP 激发一次忍耐，免伤80%
#               护盾 > 0 先扣护盾
#               hp   > 0 再扣血
#               触发死亡机制
class Attribute:
    def __init__(self) -> None:
        self.max_hp = 100
        self.hp = 80
        self.shield = 10
class WoundedMechanism:
    def process(self,attribute:Attribute,harm):
        ...
# 受到伤害 >= 当前血量+护盾 免除致命伤
class Mechanism_survive(WoundedMechanism):
    def __init__(self,next_mechanism:WoundedMechanism=None) -> None:
        super().__init__()
        self.next_mechanism = next_mechanism
        self.only_one = True
    def process(self,attribute:Attribute, harm):
        if harm >= attribute.hp+attribute.shield and self.only_one:
            print('致命伤！触发免死！（一局游戏触发一次）')
            self.only_one = False
        elif self.next_mechanism:
            self.next_mechanism.process(attribute,harm)
# >= 1/2 HP 激发一次忍耐，免伤80%
class Mechanism_endure(WoundedMechanism):
    def __init__(self,next_mechanism:WoundedMechanism=None) -> None:
        super().__init__()
        self.next_mechanism = next_mechanism
        self.only_one = True
    def process(self,attribute:Attribute, harm):
        if harm >= 0.5*attribute.hp and self.only_one:
            print('过半伤害！触发技能:忍耐！减伤80%（一局游戏触发一次）')
            harm = int(harm*0.2)
            self.only_one = False
        if self.next_mechanism:
            self.next_mechanism.process(attribute,harm)
# 护盾 > 0 先扣护盾
class Mechanism_crack(WoundedMechanism):
    def __init__(self,next_mechanism:WoundedMechanism=None) -> None:
        super().__init__()
        self.next_mechanism = next_mechanism
    def process(self,attribute:Attribute, harm):
        if attribute.shield > 0:
            attribute.shield -= harm
            if attribute.shield < 0:
                harm = -attribute.shield
                attribute.shield = 0
            else:
                harm = 0
            print(f'护盾抗伤!当前护盾量：{attribute.shield}，溢出伤害：{harm}')
        if harm and self.next_mechanism:
            self.next_mechanism.process(attribute,harm)
# hp   > 0 再扣血
class Mechanism_blood(WoundedMechanism):
    def __init__(self,next_mechanism:WoundedMechanism=None) -> None:
        super().__init__()
        self.next_mechanism = next_mechanism
    def process(self,attribute:Attribute, harm):
        if attribute.hp > 0:
            attribute.hp -= harm
            if attribute.hp < 0:
                harm = -attribute.hp
                attribute.hp = 0
            else:
                harm = 0
            print(f'肉体抗伤!当前血量:{attribute.hp}，溢出伤害：{harm}')
        if attribute.hp==0 and self.next_mechanism:
            self.next_mechanism.process(attribute,harm)
# hp   > 0 再扣血
class Mechanism_die(WoundedMechanism):
    def __init__(self,next_mechanism:WoundedMechanism=None) -> None:
        super().__init__()
        self.next_mechanism = next_mechanism
    def process(self,attribute:Attribute, harm):
        print(f'死亡!当前血量:{attribute.hp}！')
        print('惩罚：等级-1，金币-100，经验-1000！')
        print('奖励：免死+1，技能：忍耐+1，24h经验翻倍*1。获得成就：复仇之心！')
        if self.next_mechanism:
            self.next_mechanism.process(attribute,harm)

if __name__=='__main__':
    m1_survive = Mechanism_survive()
    m2_endure = Mechanism_endure()
    m3_crack = Mechanism_crack()
    m4_blood = Mechanism_blood()
    m5_die = Mechanism_die()

    m1_survive.next_mechanism = m2_endure
    m2_endure.next_mechanism = m3_crack
    m3_crack.next_mechanism = m4_blood
    m4_blood.next_mechanism = m5_die

    attribute = Attribute()

    print('输入伤害值:',end='')
    harm = int(input())
    m1_survive.process(attribute,harm)
    print('输入伤害值:',end='')
    harm = int(input())
    m1_survive.process(attribute,harm)
