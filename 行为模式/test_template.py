# 抽象模板  定义各个抽象方法，以及执行顺序
# 具体模板  实现上述抽象方法
# 更关注某一类事情的处理流程，不关注具体实现
# 例子
#   1，银行     取号->叫号->process(存款/取款/贷款)->离开
#   2，连接数据库   连接某个DB 自行选择->打开连接->增删改查 自行实现->关闭连接
#   3，游戏 开始界面->初始化地图->初始化人物->play->结束游戏
#   4，VUE 使用slot建立模板文件
#   5，生命周期调用函数，hook() 钩子函数！

class Template:
    def step1(self):
        ...
    def step2(self):
        ...
    def step3(self):
        ...
    def process(self):
        self.step1()
        self.step2()
        self.step3()

class MyTemplate(Template):
    def step1(self):
        print('第一步')
    def step2(self):
        print('第二步')
    def step3(self):
        print('第三步')

if __name__=='__main__':
    t = MyTemplate()
    t.process()