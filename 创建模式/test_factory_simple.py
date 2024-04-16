from abc import abstractmethod

class TV:
    @abstractmethod
    def play():
        ...

class HaireTV(TV):
    def play(self):
        print('Haire电视正在播放')
class HisenseTV(TV):
    def play(self):
        print('Hisense电视正在播放')    


import re
class TVFactory:
    def produceTV(self,brandName):
        # 比较方式1：
        #   if brandName.lower()=='Haire'.lower():
        # 比较方式2:
        patterns = ['Haire','Hisense']
        for pattern in patterns:
            if re.search(pattern,brandName,re.IGNORECASE):
                print(f'{pattern}电视机成功生产')
                return HaireTV()
            if re.search(pattern,brandName,re.IGNORECASE):
                print(f'{pattern}电视机成功生产')
                return HisenseTV()
        raise Exception(f'没有这种品牌为{brandName}的电视')
            
    
if __name__=='__main__':
    factory = TVFactory()
    try:
        haireTV = factory.produceTV(brandName='Haire')
        haireTV.play()

        homeTV = factory.produceTV('Home')
        homeTV.play()
    except Exception as e:
        print(e)