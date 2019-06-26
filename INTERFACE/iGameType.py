from abc import ABC,abstractmethod


class gameType(ABC):
    @abstractmethod
    def startGame (self):
        pass

    @abstractmethod
    def endGame(self,p1,p2):
        pass
