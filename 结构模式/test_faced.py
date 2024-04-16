#       Faced
# Sys1  Sys2    Sys3
# 
# 例子 Java的JDBC封装了关于Connection的打开和关闭，以及关于状态、查询的处理，coder只需要和JDBC交互就可以了
# 例子 宏，每个宏都可以包含不同的操作，比如以下操作“输入默认代码->格式化->保存”存为一个宏
#           游戏宏：闪身出去 + 打开倍镜 + 自动瞄准 + 射击 + 闪身回来
#                   技能全交 + 打开商城 + 购买金身 + 关闭商城 + 点击金身
#           用户无需操作每个系统，只需要从宏管理中选择某一个宏执行，此处的【宏管理器】就是【外观】，每个宏都是一个子系统
# 
# 外观模式：用户无需与子系统直接接触，外观器提供使用的接口
# **与适配器类似，编码时，为了简化调用过程，我们会下意识地开始封装一些类，使得调用更加方便

class Sys1():
    def do(self):
        ...
class Sys2():
    def do(self):
        ...
class Sys3():
    def do(self):
        ...
class Faced():
    def __init__(self) -> None:
        self.sys1 = Sys1()
        self.sys2 = Sys2()
        self.sys3 = Sys3()
    def doxxx1(self):
        self.sys1.do()
        self.sys2.do()
    def doxxx2(self):
        self.sys2()
        self.sys3()
