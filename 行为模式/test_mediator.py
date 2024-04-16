# colleague mediator
# colleague 实现send，receive方法
#           A send B时，A的send()调用mediator，mediator调用B的receive()
# mediator 维护一张关于所有colleague的dict
# mediator 是超级交际花
# 例子：游戏的世界频道，私聊频道
#       QQ等聊天软件
class Player:
    def __init__(self,name,channel) -> None:
        self.name = name
        self.channel = channel
    def send_all(self,msg):
        self.channel.send_all(from_who=self.name,msg=msg)
    def send_who(self,to,msg):
        self.channel.send_who(from_who=self.name,to=to,msg=msg)
    def receive(self,msg,from_who=''):
        if from_who=='':
            print(f'世界频道>{self.name}收到消息：{msg}')
        else:
            print(f'{from_who}和您私聊：{msg}')
class Channel:
    def __init__(self) -> None:
        self.players = {}
    def register(self,player:Player):
        self.players[player.name]=player
    def send_all(self,from_who,msg):
        for key in self.players:
            if key!=from_who:
                self.players[key].receive(msg=msg)
    def send_who(self,from_who,to,msg):
        self.players[to].receive(msg=msg,from_who=from_who)

if __name__=='__main__':
    channel = Channel()
    player1 = Player('张三',channel)
    player2 = Player('李四',channel)
    player3 = Player('王五',channel)
    player4 = Player('陆六',channel)

    channel.register(player1)
    channel.register(player2)
    channel.register(player3)
    channel.register(player4)

    player1.send_all('大家好，我是傻逼')
    player1.send_who('李四','你好你好，我是傻逼，交个朋友吧！')
    player2.send_who('张三','好啊好，一起做傻逼')