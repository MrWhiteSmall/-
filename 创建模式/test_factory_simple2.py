from abc import abstractmethod

class User:
    def updateInfo(self):
        print('修改个人资料')
    @abstractmethod
    def permission(self):
        ...

class Boss(User):
    def __init__(self) -> None:
        super().__init__()
        print('创建大老板！')
    def permission(self):
        print('大老板有一票否决权！')
class Manager(User):
    def __init__(self) -> None:
        super().__init__()
        print('创建经理!')
    def permission(self):
        print('经理有权限审批假条！')
class Employee(User):
    def __init__(self) -> None:
        super().__init__()
        print('创建员工！')
    def permission(self):
        print('员工有权利打假条')

class UserFactory():
    def getUser(self,permission):
        if permission==1:
            return Employee()
        if permission==2:
            return Manager()
        if permission==3:
            return Boss()
        raise Exception(f'没有这种权限的人物:{permission}')


import random
class PermissionCheck:
    def check(self,username,pwd):
        # 处理用户权限，返回权限值
        # 70%概率返回正常权限【1-3】 其他情况返回其他权限，比如4
        rand = random.random()
        return random.choice(list(range(1,4)))  if rand<0.7  else 4
    
if __name__=='__main__':
    username = 'lsj'
    pwd = '123'
    permissionCheck = PermissionCheck()
    permission = permissionCheck.check(username,pwd)

    userFactory = UserFactory()
    try:
        for i in range(5):
            user = userFactory.getUser(permission)
            user.permission()
    except Exception as e:
        print(e)