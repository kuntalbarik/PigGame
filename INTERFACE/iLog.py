from abc import ABC,abstractmethod

class logger:

    @abstractmethod
    def openLog(self):
        pass

    @abstractmethod
    def printLog(self,logType,message):
        pass

    @abstractmethod
    def closeLog(self):
        pass
