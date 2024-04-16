#   Component
# Leaf      Composite
#           List<Component>
# 举例：文件夹-文件
from abc import abstractmethod
class Component:
    @abstractmethod
    def showTree(self):
        ...

class File(Component):
    def __init__(self,filename) -> None:
        super().__init__()
        self.filename = filename
    def showTree(self):
        print(self.filename)

class Folder(Component):
    def __init__(self,foldername) -> None:
        super().__init__()
        self.files_included = []
        self.foldername = foldername
        self.depth = 1
    def addComponent(self,f):
        self.files_included.append(f)
        if isinstance(f,Folder):
            f.depth+=self.depth
    def showTree(self):
        print(self.foldername)
        for f in self.files_included:
            print('\t'*self.depth,end='')
            f.showTree()

if __name__=='__main__':
    file1 = File('file1')
    file2 = File('file2')
    file3 = File('file3')
    folder1 = Folder('folder1')
    folder2 = Folder('folder2')
    folder3 = Folder('folder3')
    
    folder1.addComponent(file1)
    folder1.addComponent(folder2)
    folder1.addComponent(file3)
    folder2.addComponent(file2)
    folder2.addComponent(folder3)
    folder2.addComponent(file1)
    folder3.addComponent(file3)

    folder1.showTree()