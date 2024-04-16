# Iterator          Aggregate
# ConcreteIterator ConcreteAggregate
# iterator(data) data由Aggregate提供
# iterator  主要实现len，next两个方法
# aggregate 主要实现create_iterator这个方法
# 举例：dataloader
from abc import abstractmethod
class Dataloader:
    def __init__(self) -> None:
        self.index = 0
    @abstractmethod
    def isFirst(self):
        ...
    @abstractmethod
    def isLast(self):
        ...
    @abstractmethod
    def next(self):
        ...
    @abstractmethod
    def previous(self):
        ...
    @abstractmethod
    def item(self):
        ...
class MyDataloader(Dataloader):
    def __init__(self,dataset,batch) -> None:
        super().__init__()
        self.data = dataset
        self.batch = batch
    def isFirst(self):
        return self.index==0
    def isLast(self):
        return self.index == len(self.data)-1
    def next(self):
        if not self.isLast():
            self.index += self.batch
            if self.index >= len(self.data)-1:
                self.index = len(self.data)-1
        # else:
        #     self.index = 0
    def previous(self):
        if not self.isFirst() and self.index-self.batch > 0:
            self.index -= self.batch
        else:
            self.index = len(self.data)-1
    def item(self):
        return self.data[self.index:self.index+self.batch]
    
class Dataset:
    @abstractmethod
    def create_loader(self,batch):
        ...

class MyDataset(Dataset):
    def __init__(self) -> None:
        self.data = []
    def add_item(self,item):
        self.data.append(item)
    def create_loader(self,batch):
        return MyDataloader(self.data,batch)
    
if __name__=='__main__':
    dataset = MyDataset()
    dataset.data = [i for i in range(100)]
    dataloader = dataset.create_loader(batch=25)
    while not dataloader.isLast():
        print(dataloader.item())
        dataloader.next()
