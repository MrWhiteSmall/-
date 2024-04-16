# Context       State 
#            S1  S2  S3
# Context包含State，存储当前的状态
# State包含Context，在State编写处理逻辑&处理完以后，可以更新Context中的当前状态
# 用户只需要创建Context对象，无需管理其中的State

from abc import abstractmethod

class Character:
    def __init__(self) -> None:
        self.state = StateHealth()
        self.hp = 60
        self.param_hurt = 10
        self.param_recover = 10
        self.min_bound_health = 60
        self.min_bound_wounded = 30
    def hurt(self):
        self.hp -= self.param_hurt
        if self.hp < self.min_bound_wounded:
            self.state = StateDying()
            print('濒死状态:','💛'*self.hp)
        elif self.hp < self.min_bound_health:
            self.state = StateWounded()
            print('受伤状态:','🧡'*self.hp)
        else:
            print('健康状态:','🖤'*self.hp)
    def recover(self):
        self.hp += self.param_recover
        if self.hp >= self.min_bound_health:
            self.state = StateHealth()
            print('健康状态:','🖤'*self.hp)
        elif self.hp >= self.min_bound_wounded:
            self.state = StateWounded()
            print('受伤状态:','🧡'*self.hp)
        else:
            print('濒死状态:','💛'*self.hp)


class Character2:
    def __init__(self) -> None:
        self.state = StateHealth()
        self.hp = 60
        self.param_hurt = 10
        self.param_recover = 10
        self.min_bound_health = 60
        self.min_bound_wounded = 30
    def hurt(self):
        self.hp -= self.param_hurt
        self.state.hurt(self)
    def recover(self):
        self.hp += self.param_recover
        self.state.recover(self)



class State:
    @abstractmethod
    def hurt(self,context):
        ...
    @abstractmethod
    def recover(self,context):
        ...

class StateHealth(State):
    def hurt(self, context):
        hp  = context.hp
        if context.hp < context.min_bound_health:
            context.state = StateWounded()
            print('受伤状态:','🧡'*hp)
        else:
            print('健康状态:','🖤'*hp)
    def recover(self, context):
        hp  = context.hp
        print('健康状态:','🖤'*hp)

class StateWounded(State):
    def hurt(self, context):
        hp  = context.hp
        if context.hp < context.min_bound_wounded:
            context.state = StateDying()
            print('濒死状态:','💛'*hp)
        else:
            print('受伤状态:','🧡'*hp)
    def recover(self, context):
        hp  = context.hp
        if context.hp >= context.min_bound_health:
            context.state = StateHealth()
            print('健康状态:','🖤'*hp)
        else:
            print('受伤状态:','🧡'*hp)
    

class StateDying(State):
    def hurt(self, context):
        hp  = context.hp
        print('濒死状态:','💛'*hp)
    def recover(self, context):
        hp  = context.hp
        if context.hp >=context.min_bound_wounded:
            context.state = StateWounded()
            print('受伤状态:','🧡'*hp)
        else:
            print('濒死状态:','💛'*hp)
    
if __name__=='__main__':
    # 错误示例1（正常运行）
    '''
    character = Character()
    for _ in range(5):
        character.hurt() 
    for _ in range(6):
        character.recover() 
    '''

    character = Character2()
    for _ in range(5):
        character.hurt() 
    for _ in range(6):
        character.recover() 
    