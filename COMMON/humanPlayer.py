from PigGame.INTERFACE.iPlayer import action
from random import randint
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


class human(action):

    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,name=None):
        if(name==None):
            self.__name=self.declareHuman()
        else:
            self.__name=name
        log.printLog(data["i"], data["take name"] + self.__name)

    @property
    def TempScore(self):
        return self.__tempScore
    @TempScore.setter
    def TempScore(self,tempscore):
        self.__tempScore=tempscore

    @property
    def FinalScore(self):
        return self.__finalScore

    @FinalScore.setter
    def FinalScore(self, finalScore):
        self.__finalScore = finalScore

    def declareHuman(self):
        self.__name= input(data["take name"])
        log.printLog(data["i"],data["take name"]+self.__name)
        return self.__name

    def choice(self,playername):
        self.__choicevalue = input(playername+' '+data["roll or hold"])
        log.printLog(data["i"], data["roll or hold"] + self.__choicevalue)
        if(self.__choicevalue.lower() in ('r','h')):
            return self.__choicevalue
        else:
            print("\n"+data["wrong roll hold"])
            log.printLog(data["w"],data["wrong roll hold"])
            return 'h'


    def role(self):
        self.__x= randint(0,19)
        if (self.__x==0 ):
            print(data["human scored"],self.__x)
            log.printLog(data["i"], data["human scored"]+str(self.__x))
            print(data["human chance over"])
            log.printLog(data["i"],data["human chance over"])
            return False

        elif(self.__x>6):
            self.__x=self.__x%6
            print(data["human scored"], self.__x)
            log.printLog(data["i"], data["human scored"]+str(self.__x))
            return self.__x

        else:
            print(data["human scored"], self.__x)
            log.printLog(data["i"], data["human scored"]+str(self.__x))
            return self.__x

    def hold(self):
        print(data["human hold chance"])
        log.printLog(data["i"],data["human hold chance"])
        return 1

