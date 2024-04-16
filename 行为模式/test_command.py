# Command       Invoker     Receiver
# ConcreteCommand
# Invoker   处于中间，接收Command，然后执行Command就好     
# Command   只需要专注自己的命令对应什么功能，然后调用Receiver对应的功能，主要实现execute
# Receiver  只需关注自己能有哪些功能，并依次实现即可
# 
# Command包含Receiver Receiver类似于一个功能文档
# Invoker包含抽象Command，只需将这个Command执行即可
# Client 关注设置什么Command即可
# 
# 例子：vim编辑器，输入的指令通过解释器得到一个Command，设置这个Command，然后执行
class Command:
    def execute(self):
        ...

class ConcreteCommand1(Command):
    def __init__(self,receiver) -> None:
        super().__init__()
        self.receiver = receiver
    def execute(self):
        self.receiver.do_command1()
class ConcreteCommand2(Command):
    def __init__(self,receiver) -> None:
        super().__init__()
        self.receiver = receiver
    def execute(self):
        self.receiver.do_command2()
    
class Invoker:
    def __init__(self,receiver) -> None:
        self.command = None
    def send_command(self,command):
        self.command = command
    def execute(self):
        if self.command:
            self.command.execute()
        else:
            print('请先设置指令')

class Receiver:
    def do_command1(self):
        print('执行指令1')
    def do_command2(self):
        print('执行指令2')