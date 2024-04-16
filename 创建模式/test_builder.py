from abc import abstractmethod
from pprint import pprint
import random
def random_point(bound):
    return random.choice(list(range(bound))),random.choice(list(range(bound)))

class Map:
    def __init__(self,size=10) -> None:
        self.icon = '⬜'
        self.map = [[self.icon for _ in range(size)] for _ in range(size)]
    def show_map(self):
        pprint(self.map)

# 抽象建造者：只声明要建造的对象map，和建造的蓝图，不做具体实现
class MapBuilder:
    def __init__(self):
        self.__map_size=None
        self.__map = None
        self.__pitfall=None
        self.__obstacle=None
        self.__resource=None
    @abstractmethod
    def build_pitfall(self):
        ...
    @abstractmethod
    def build_obstacle(self):
        ...
    @abstractmethod
    def build_resource(self):
        ...
    @abstractmethod
    def get_map(self):
        ...
    @abstractmethod
    def show_map(self):
        ...

# 具体建造者
class MapEasyBuilder(MapBuilder):
    def __init__(self,):
        super().__init__()
        self.__map_size=10
        self.__map = Map(self.__map_size)
        self.__pitfall=2
        self.__obstacle=2
        self.__resource=2
        self.icon_pitfall = '💣'
        self.icon_obstacle='🈲'
        self.icon_resource='📦'
    def build_pitfall(self):
        count = 0
        while count!=self.__pitfall:
            x,y=random_point(self.__map_size)
            if self.__map.map[x][y]==self.__map.icon:
                self.__map.map[x][y]=self.icon_pitfall
                count+=1
    def build_obstacle(self):
        count = 0
        while count!=self.__obstacle:
            x,y=random_point(self.__map_size)
            if self.__map.map[x][y]==self.__map.icon:
                self.__map.map[x][y]=self.icon_obstacle
                count+=1
    def build_resource(self):
        count = 0
        while count!=self.__resource:
            x,y=random_point(self.__map_size)
            if self.__map.map[x][y]==self.__map.icon:
                self.__map.map[x][y]=self.icon_resource
                count+=1
    def get_map(self):
        return self.__map
    def show_map(self):
        self.__map.show_map()

class MapNormalBuilder(MapBuilder):
    def __init__(self,):
        super().__init__()
        self.__map_size=10
        self.__map = Map(self.__map_size)
        self.__pitfall=4
        self.__obstacle=4
        self.__resource=4
        self.icon_pitfall = '💣'
        self.icon_obstacle='🈲'
        self.icon_resource='📦'
    def build_pitfall(self):
        count = 0
        while count!=self.__pitfall:
            x,y=random_point(self.__map_size)
            if self.__map.map[x][y]==self.__map.icon:
                self.__map.map[x][y]=self.icon_pitfall
                count+=1
    def build_obstacle(self):
        count = 0
        while count!=self.__obstacle:
            x,y=random_point(self.__map_size)
            if self.__map.map[x][y]==self.__map.icon:
                self.__map.map[x][y]=self.icon_obstacle
                count+=1
    def build_resource(self):
        count = 0
        while count!=self.__resource:
            x,y=random_point(self.__map_size)
            if self.__map.map[x][y]==self.__map.icon:
                self.__map.map[x][y]=self.icon_resource
                count+=1
    def get_map(self):
        return self.__map
    def show_map(self):
        self.__map.show_map()

class MapHardBuilder(MapBuilder):
    def __init__(self,):
        super().__init__()
        self.__map_size=10
        self.__map = Map(self.__map_size)
        self.__pitfall=10
        self.__obstacle=10
        self.__resource=6
        self.icon_pitfall = '💣'
        self.icon_obstacle='🈲'
        self.icon_resource='📦'
    def build_pitfall(self):
        count = 0
        while count!=self.__pitfall:
            x,y=random_point(self.__map_size)
            if self.__map.map[x][y]==self.__map.icon:
                self.__map.map[x][y]=self.icon_pitfall
                count+=1
    def build_obstacle(self):
        count = 0
        while count!=self.__obstacle:
            x,y=random_point(self.__map_size)
            if self.__map.map[x][y]==self.__map.icon:
                self.__map.map[x][y]=self.icon_obstacle
                count+=1
    def build_resource(self):
        count = 0
        while count!=self.__resource:
            x,y=random_point(self.__map_size)
            if self.__map.map[x][y]==self.__map.icon:
                self.__map.map[x][y]=self.icon_resource
                count+=1
    def get_map(self):
        return self.__map
    def show_map(self):
        self.__map.show_map()


class GameMap():
    def __init__(self,map_builder:MapBuilder) -> None:
        self.map_builder = map_builder
    def construct(self):
        self.map_builder.build_pitfall()
        self.map_builder.build_obstacle()
        self.map_builder.build_resource()
        

if __name__=='__main__':
    # easy_map = MapEasyBuilder()
    # normal_map = MapNormalBuilder()
    hard_map = MapHardBuilder()
    game_map = GameMap(hard_map)
    game_map.construct()
    hard_map.show_map()