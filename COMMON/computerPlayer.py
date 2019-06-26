from PigGame.INTERFACE.iPlayer import action
from random import randint
import json
from PigGame.COMMON.Logs import logPrint
import json,os,sys,locale


###choosing the language
language=locale.setlocale(locale.LC_ALL, '')
language=language[0:2]
###choosing the json for selected language
path="../DTO/res_"+language+".json"
####setting the path of json file
absfilepath=os.path.abspath(__file__)
fileDir = os.path.dirname(absfilepath)
filename = os.path.join(fileDir, path)
filename = os.path.abspath(os.path.realpath(filename))
readJson=open(filename, "r")
data = json.load(readJson)
log = logPrint()


class computer(action):

    @property
    def Name(self):
        return self.__name

    @Name.setter
    def Name(self,name):
        name="COMPUTER"
        self.__name =name
        log.printLog(data["i"], data["take name"] + self.__name)

    @property
    def TempScore(self):
        return self.__tempScore

    @TempScore.setter
    def TempScore(self, tempscore):
        self.__tempScore = tempscore

    @property
    def FinalScore(self):
        return self.__finalScore

    @FinalScore.setter
    def FinalScore(self, finalScore):
        self.__finalScore = finalScore


    def role(self):
        self.__x = randint(0,45)
        if (self.__x==0 ):
            print(data["computer chance over"])
            log.printLog(data["i"],data["computer chance over"])
            return self.__x

        ###hold logic for computer
        elif(self.__x in(7,14,21,28,30,29,45,44,41,40,39)):
            print(data["computer hold chance"])
            log.printLog(data["i"],data["computer hold chance"])
            return "hold"

        else:
            if(self.__x>7 and self.__x<12):
                self.__x=self.__x%6
            elif(self.__x>12 and self.__x<21):
                self.__x=self.__x%6
            else:
                self.__x=6
            print(data["computer scored"],self.__x)
            log.printLog(data["i"],data["computer scored"]+str(self.__x))
            return self.__x

    ###not in used, just to define as with out hold will throw exception
    def hold(self):
        print(data["computer hold chance"])
        log.printLog(data["i"], data["computer hold chance"])
        return "hold"

