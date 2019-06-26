from PigGame.INTERFACE.iGameType import  gameType
from PigGame.COMMON.finalScore import finalScore
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


class tournament(gameType):

    def startGame(self,p1,p2):
        self.__fs = finalScore()
        self.__turn = 0
        self.__condition = True
        self.__t=tournament()
        self.__p1=p1
        self.__p2=p2
        self.__p1.FinalScore=self.__p1.TempScore=self.__p2.FinalScore=self.__p2.TempScore=0
        #########Tournament with single player (checking whether 2nd player is human or computer )
        if (self.__p2.Name =="COMPUTER"):
            while (self.__condition):
                ####human player  turn
                if (self.__turn == 0):
                    ###taking human input whether want to hold or role
                    self.__playerchoice =self.__p1.choice(self.__p1.Name)
                    ####to continue game if anything except r/R is entered, chance will be hold
                    if (self.__playerchoice.lower()=='r'):
                        self.__score =p1.role()
                        if (self.__score == False):
                            turn = 1
                            self.__p1.TempScore=self.__p1.FinalScore=0
                        else:
                            self.__p1.TempScore =self.__score
                            self.__p1.FinalScore=self.__fs.calculateScore(self.__p1.FinalScore,self.__p1.TempScore)
                    ####human player hold the chance
                    else:
                        self.__turn = self.__p1.hold()
                    print(data["palyer 1 final score"],self.__p1.FinalScore)
                    log.printLog(data["i"],data["palyer 1 final score"]+str(self.__p1.FinalScore))
                    print(data["computer final score"],self.__p2.FinalScore)
                    log.printLog(data["i"],data["computer final score"]+str(self.__p2.FinalScore))
                    print("-------------------------------------------------------------------")
                ####computer  turn
                else:
                    self.__score =self.__p2.role()
                    if (self.__score == 0):
                        self.__p2.TempScore=self.__p2.FinalScore=0
                        self.__turn = 0
                    elif (self.__score == "hold"):
                        self.__turn = 0
                    else:
                        self.__p2.TempScore =self.__score
                        self.__p2.FinalScore =self.__fs.calculateScore(self.__p2.FinalScore,self.__p2.TempScore)

                    print(data["computer final score"],self.__p2.FinalScore)
                    log.printLog(data["i"], data["computer final score"]+str(self.__p2.FinalScore))
                    print("-------------------------------------------------------------------")

                self.__condition =self.__t.endGame(self.__p1, self.__p2)
        #########Tournament with multiple player
        else:
            while (self.__condition):
                ####player 1 turn
                if (self.__turn == 0):
                    ###taking palyer 1 input whether want to hold or role
                    self.__playerchoice = self.__p1.choice(self.__p1.Name)
                    ####to continue game if anything except r/R is entered, chance will be hold
                    if (self.__playerchoice.lower()=='r'):
                        self.__score =self.__p1.role()
                        if (self.__score == False):
                            self.__turn = 1
                            self.__p1.TempScore=self.__p1.FinalScore=0
                        else:
                            self.__p1.TempScore =self.__score
                            self.__p1.FinalScore =self.__fs.calculateScore(self.__p1.FinalScore,self.__p1.TempScore)
                    ####player 1 hold the chance
                    else:
                        self.__turn = self.__p1.hold()
                    print(data["palyer 1 final score"],self.__p1.FinalScore)
                    log.printLog(data["i"],data["palyer 1 final score"]+str(self.__p1.FinalScore))
                    print(self.__p2.Name+data["palyer 2 final score"],self.__p2.FinalScore)
                    log.printLog(data["i"],self.__p2.Name+data["palyer 2 final score"]+str(self.__p2.FinalScore))
                    print("-------------------------------------------------------------------")
                ####player 2 turn
                else:
                    ###taking palyer 2 input whether want to hold or role
                    self.__playerchoice = self.__p2.choice(self.__p2.Name)
                    ####to continue game if anything except r/R is entered, chance will be hold
                    if (self.__playerchoice.lower()=='r'):
                        self.__score =self.__p1.role()
                        if (self.__score == False):
                            self.__turn = 0
                            self.__p2.TempScore =self.__p2.FinalScore = 0
                        else:
                            self.__p2.TempScore =self.__score
                            self.__p2.FinalScore =self.__fs.calculateScore(self.__p2.FinalScore,self.__p2.TempScore)
                    ####player 2 hold the chance
                    else:
                        self.__turn = 0
                    print(data["palyer 1 final score"],self.__p2.FinalScore)
                    log.printLog(data["i"], data["palyer 1 final score"] + str(self.__p2.FinalScore))
                    print(self.__p1.Name+data["palyer 2 final score"], self.__p1.FinalScore)
                    log.printLog(data["i"], self.__p1.Name+data["palyer 2 final score"] + str(self.__p1.FinalScore))
                    print("-------------------------------------------------------------------")

                condition =self.__t.endGame(self.__p1, self.__p2)

    def endGame(self, p1, p2):
        self.__p1=p1
        self.__p2= p2
        self.__s = data["win format"]

        if (self.__p1.FinalScore >= 50):
            # print(data["win format1"], self.p1name,data["win format2"])
            print(self.__s.format(self.__p1.Name))
            log.printLog(data["i"], self.__s.format(self.__p1.Name))
            return False

        elif (self.__p2.FinalScore >= 50):
            # print(data["win format1"], self.p2name,data["win format2"])
            print(self.__s.format(self.__p2.Name))
            log.printLog(data["i"], self.__s.format(self.__p2.Name))
            return False
        else:
            return True



