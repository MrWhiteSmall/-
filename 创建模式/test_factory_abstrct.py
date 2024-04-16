from abc import abstractmethod

# 抽象工厂
class CharacterFactory():
    def __init__(self) -> None:
        self.init_attribute()
    @abstractmethod
    def init_attribute(self):
        ...

    @abstractmethod
    def equip_armor(self):
        ...

    @abstractmethod
    def equip_weapon(self):
        ...
    
    @abstractmethod
    def equip_pet(self):
        ...

# 抽象物品
class Armor:
    @abstractmethod
    def showInfo(self):
        ...

class Weapon:
    @abstractmethod
    def showInfo(self):
        ...

class Pet:
    @abstractmethod
    def showInfo(self):
        ...

# 具体产品
class Armor_Fire(Armor):
    def showInfo(self):
        print('炽焰套装')

class Armor_Ice(Armor):
    def showInfo(self):
        print('寒冰套装')

class Armor_Forest(Armor):
    def showInfo(self):
        print('木灵套装')

class Weapon_Fire(Weapon):
    def showInfo(self):
        print('焚魂枪')

class Weapon_Ice(Weapon):
    def showInfo(self):
        print('艳冰刃')

class Weapon_Forest(Weapon):
    def showInfo(self):
        print('刺藤鞭')

class Pet_Fire(Pet):
    def showInfo(self):
        print('炎麒麟')

class Pet_Ice(Pet):
    def showInfo(self):
        print('凌魄龙')

class Pet_Forest(Pet):
    def showInfo(self):
        print('影叶狮')

# 具体工厂
class Character_Fire(CharacterFactory):
    def init_attribute(self):
        print('''
        Name:炎龙侠
        Power:100      Speed:50
        Shield:100     Dodge:30
        ''')
    def equip_armor(self):
        return Armor_Fire()
    def equip_weapon(self):
        return Weapon_Fire()
    def equip_pet(self):
        return Pet_Fire()
class Character_Ice(CharacterFactory):
    def init_attribute(self):
        print('''
        Name:冰犀侠
        Power:90       Speed:40
        Shield:110     Dodge:10
        ''')
    def equip_armor(self):
        return Armor_Ice()
    def equip_weapon(self):
        return Weapon_Ice()
    def equip_pet(self):
        return Pet_Ice()
class Character_Forest(CharacterFactory):
    def init_attribute(self):
        print('''
        Name:飞鹰侠
        Power:80        Speed:70
        Shield:70       Dodge:50
        ''')
    def equip_armor(self):
        return Armor_Forest()
    def equip_weapon(self):
        return Weapon_Forest()
    def equip_pet(self):
        return Pet_Forest()
    
class Character():
    def __init__(self,armor,weapon,pet) -> None:
        self.armor = armor
        self.weapon = weapon
        self.pet = pet
    def showInfo(self):
        self.armor.showInfo()
        self.weapon.showInfo()
        self.pet.showInfo()
    
if __name__=='__main__':
    character = Character_Ice()
    armor_fire = character.equip_armor()
    weapon_fire = character.equip_weapon()
    pet_fire = character.equip_pet()
    c = Character(armor_fire,weapon_fire,pet_fire)
    c.showInfo()