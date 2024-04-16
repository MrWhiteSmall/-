# Momento Originator Caretaker
# Momento       用于存储数据，不提供更改其内容的方法
# Originator    用于访问Momento，实现save，restore方法
# Caretaker     用于存放originator保存的momento，提供push/pop或者set/get方法
# 例子：游戏存档
class GameStatus():
    def __init__(self,game_time,game_progress,character_attribute) -> None:
        self.game_time      = game_time
        self.game_progress  = game_progress
        self.character_attribute = {}
        for k in character_attribute:
            self.character_attribute[k]=character_attribute[k]

import math
from datetime import datetime
def getTime():
    t = datetime.now()
    format_t = t.strftime('%Y-%m-%d %H:%M:%S')
    return format_t

class Player:
    def __init__(self) -> None:
        self.game_time      = None
        self.game_progress  = None
        self.character_attribute=None
    def start_game(self):
        self.game_time = getTime()
        self.game_progress = '0%'
        self.character_attribute = {
            'level':1,
            'hp':100,'mp':100,
            'power':20,'defense':15,
            'speed':15,'dodge':10
        }
    def playing(self):
        game_progress = int(self.game_progress[:-1])+10
        self.game_progress = f'{game_progress}%'
        self.game_time = getTime()
        # 玩了1秒，不然运行时间太短，看不到回溯效果
        import time
        time.sleep(1)
    def level_up(self):
        for key in self.character_attribute:
            if key=='level':
                self.character_attribute[key]+=1
            else:
                value = math.ceil(self.character_attribute[key]*1.1)
                self.character_attribute[key] = value
    def save(self):
        self.game_time = getTime()
        return GameStatus(self.game_time,self.game_progress,self.character_attribute)
    def restore(self,gameStatus):
        self.game_time      = gameStatus.game_time
        self.game_progress  = gameStatus.game_progress
        for k in self.character_attribute:
            self.character_attribute[k] = gameStatus.character_attribute[k]
    
    def __str__(self) -> str:
        return f'''
        Player
        LEVEL : {self.character_attribute['level']}
        HP : {self.character_attribute['hp']}       MP : {self.character_attribute['hp']}
        POWER : {self.character_attribute['hp']}    DEFENSE : {self.character_attribute['hp']}
        SPEED : {self.character_attribute['hp']}    DODGE : {self.character_attribute['hp']}
        游戏时间 : {self.game_time}
        游戏进度 : {self.game_progress}
        '''
            
class GameManager:
    def __init__(self) -> None:
        self.history_saved_point = []
    def push(self,gameStatus):
        self.history_saved_point.append(gameStatus)
    def pop(self):
        try:
            gameStatus = self.history_saved_point.pop()
            return gameStatus
        except IndexError:
            return None
        
if __name__=='__main__':
    player = Player()
    gameManager = GameManager()

    # 开始游戏 
    player.start_game()

    # 正在游玩 + 保存进度
    player.playing()
    gameManager.push(player.save())
    print(player)

    # 玩 + 玩 + 升级 
    player.playing()
    player.playing()
    player.level_up()
    print(player)

    # 回退进度
    lastStatus=gameManager.pop()
    if lastStatus is not None:
        player.restore(lastStatus)
        print(player)