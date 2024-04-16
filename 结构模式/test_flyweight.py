#       flyweight
# concreteFW    factoryFW
#               dict()存储concreteFW
# flyweight 内部状态 不更改
#           外部状态 更改
# 举例 黑白棋
#       内部状态 颜色
#       外部状态 位置
# 好处，节省存储空间，假设10*10的棋盘，棋子对象=1k，矩阵大小=A，不适用享元  => 100k + A
#                                                               使用享元 => 2k + A
# 举例 共享网站
#       内部状态 网站的源码
#       外部状态 访问者/cookie
class Chess:
    def fall_chess(self,position):
        ...

class ChessColor(Chess):
    def __init__(self,color) -> None:
        super().__init__()
        self.color = color
        self.position = None
    def fall_chess(self, position):
        self.position = position
        print(f'{self.color}棋落子 行{position[0]}列{position[1]}')

class ChessFactory:
    def __init__(self) -> None:
        self.chesses = dict()
    def get_chess(self,chess):
        if chess not in self.chesses:
            self.chesses[chess] = ChessColor(color = chess)
            print(f'创建新子，颜色为{chess}')
        return self.chesses[chess]

if __name__=='__main__':
    chess_factory = ChessFactory()
    black = chess_factory.get_chess('黑')
    black.fall_chess([3,2])
    white = chess_factory.get_chess('白')
    white.fall_chess([4,2])    
    black = chess_factory.get_chess('黑')
    black.fall_chess([2,2])
