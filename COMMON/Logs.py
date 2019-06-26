from PigGame.INTERFACE.iLog import logger
from datetime import datetime
import os



class logPrint(logger):
    def openLog(self,):
        self.now = datetime.now()
        self.date=str(self.now)
        if (os.path.exists("d:\\Pig Game Log") == False):
            os.mkdir("d:\\Pig Game Log")
        self.filepath = 'D:\\Pig Game Log\\log_' + self.date[0:11] + '.txt'
        self.fileObject=open(self.filepath,"a+")
        return self.fileObject

    def printLog(self,logType:str,message:str):
        self.fileo=l.openLog()
        self.logType=logType
        self.message=message
        self.now =datetime.now()
        self.datei=str(self.now)
        self.fileo.write('['+self.datei+']-['+self.logType+']-'+self.message+'\n')
        l.closeLog(self.fileo)

    def closeLog(self,fileo):
        self.fileo=fileo
        self.fileo.close()

l=logPrint()