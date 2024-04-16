# Strategy  Context
#           Context包含Strategy
# 可以手动指定Strategy，Strategy不包含Context，这也是与State模式不同的地方
# State模式自动切换状态并执行当下状态的动作，Strategy模式需要手动指定策略然后执行该策略下的动作
# 例子：
# 1 美团满减策略：
#       买月卡送无门槛券
#       使用每日满减券
#       购买门店优惠券
# 2 游戏同一技能的不同效果
#       扣血增伤
#       扣蓝加盾
#       减速提抗
class SkillEffect:
    def effect(self,attribute):
        ...
class Effect_harm(SkillEffect):
    def effect(self, attribute):
        print('System : HP -10 POWER +30 !')
        attribute.hp    -= 10
        attribute.power += 30
        print(attribute)
class Effect_shield(SkillEffect):
    def effect(self, attribute):
        print('System : MP -10 SHIELD +20 !')
        attribute.mp    -= 10
        attribute.shield += 20
        print(attribute)
class Effect_dodge(SkillEffect):
    def effect(self, attribute):
        print('System : SPEED -5 dodge +15 !')
        attribute.speed -= 5
        attribute.dodge += 15
        print(attribute)

class CharacterAttribute:
    def __init__(self) -> None:
        self.hp = 50
        self.mp = 50
        self.power = 20
        self.defense = 15
        self.speed = 20
        self.dodge = 10
        self.shield = 0
        self.hp_icon = '❤'
        self.mp_icon = '💙'
        self.shield_icon = '🤍'
    def __str__(self) -> str:
        return f'''
        HP:{self.hp_icon*self.hp}{self.shield_icon*self.shield}
        MP:{self.mp_icon*self.mp}
        power:{self.power}        defense:{self.defense}
        speed:{self.speed}        dodge:{self.dodge}
        '''

class Skill:
    def __init__(self,skill_effect) -> None:
        self.skill_effect = skill_effect
    def emit(self,attribute):
        self.skill_effect.effect(attribute)

if __name__=='__main__':
    attribute = CharacterAttribute()
    print('初始状态:')
    print(attribute)

    # skill_effect  = Effect_harm()
    # skill_effect  = Effect_shield()
    skill_effect  = Effect_dodge()
    skill = Skill(skill_effect)
    skill.emit(attribute)