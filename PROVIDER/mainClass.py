from PigGame.COMMON.tournamentGame import tournament
from PigGame.COMMON.challengeGame import challenge
from PigGame.COMMON.humanPlayer import human
from PigGame.COMMON.computerPlayer import computer
from PigGame.COMMON.finalScore import finalScore
from PigGame.COMMON.tempScore import tempScore
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

class game:
    def startMainGame(self):
        log.printLog(data["i"], data["starting game"])
        # #taking user input for game type
        try:
            self.__gameType = " ".join(input(data["select game"]).split())
            log.printLog(data["i"], data["select game"])
            log.printLog(data["i"], self.__gameType)
            if(self.__gameType.lower() in ('t','c')):

                ###Creating game Object depending upon the input
                if (self.__gameType.lower() == 't'):
                    log.printLog(data["i"], data["tournament"])
                    self.__gt = tournament()
                else:
                    log.printLog(data["i"], data["challenge"])
                    self.__gt = challenge()

                ###taking user input for no of players
                self.__noOfPlayers =int(input(data["no of player"]))
                log.printLog(data["i"],data["no of player"])
                log.printLog(data["i"],str(self.__noOfPlayers))
                try:
                    if(self.__noOfPlayers in(1,2)):
                        i=1
                        s=data["take name"]
                        if (self.__noOfPlayers==2):
                            self.__p1=human()
                            name = " ".join(input(s.format(i)).split())
                            try:
                                if (len(name) != 0):
                                    self.__p1.Name= name
                                    log.printLog(data["i"], s.format(i))
                                    log.printLog(data["i"], self.__p1.Name)
                                else:
                                    raise NameError
                            except NameError as ne:
                                print(data["name null"])
                                log.printLog(data["e"], data["name null"])
                                sys.exit()

                            i+=1
                            self.__p2=human()
                            name = " ".join(input(s.format(i)).split())
                            try:
                                if (len(name) != 0):
                                    self.__p2.Name = name
                                    log.printLog(data["i"], s.format(i))
                                    log.printLog(data["i"], self.__p2.Name)
                                else:
                                    raise NameError
                            except NameError as ne:
                                print(data["name null"])
                                log.printLog(data["e"], data["name null"])
                                sys.exit()

                        else:
                            self.__p1 = human()
                            name = " ".join(input(s.format(i)).split())
                            try:
                                if (len(name) != 0):
                                    self.__p1.Name = name
                                    log.printLog(data["i"], s.format(i))
                                    log.printLog(data["i"], self.__p1.Name)
                                else:
                                    raise NameError
                            except NameError as ne:
                                print(data["name null"])
                                log.printLog(data["e"],data["name null"])
                                sys.exit()

                            self.__p2 = computer()
                            self.__p2.Name="COMPUTER"

                        self.__gt.startGame(self.__p1, self.__p2)

                    else:
                            raise ValueError
                except ValueError as ve:
                    print(data["wrong input"])
                    log.printLog(data["e"], data["wrong no of players"])

            else:
                raise ValueError
        except ValueError:
            print(data["wrong input"])
            log.printLog(data["e"], data["wrong game type"])

class customGame:

    winScore=100

    def createGame(self,gameType):
        if gameType.lower()=='t':
            gameObject=tournament()
            return gameObject
        elif gameType.lower()=='c':
            gameObject=challenge()
            return gameObject
        else:
            return False

    def createPlayer(self,noOfPlayers):
        if noOfPlayers==1:
            humanPlayer=human()
            computerPlayer=computer()
            return humanPlayer,computerPlayer

        elif noOfPlayers==2:
            humanPlayer1=human()
            humanPlayer2=human()
            return humanPlayer1,humanPlayer2
        else:
            return False

    def createHumanPlayer(self):
        return human()

    def createComputerPlayer(self):
        return computer()

    def setHumanPlayer(self,humanObject,name:str,tempScore=0,finalScore=0):
        humanObject.Name=name
        humanObject.TempScore=tempScore
        humanObject.FinalScore=finalScore

    def setComputerPlayer(self,computerObject,tempScore=0,finalScore=0):
        computerObject.Name="COMPUTER"
        computerObject.TempScore=tempScore
        computerObject.FinalScore=finalScore


    def humanPlayOption(self,player):
        playerChoice=" ".join(input(player.Name+' '+data["roll or hold"]).split())
        if (playerChoice.lower()=='r'):
            return 'r'
        else:
            return 'h'

    def Roll(self,player):
        return player.role()

    def Hold(self,player):
        return player.hold()

    def Score(self,player):
        return player.TempScore

    def CheckWinner(self,player1,player2):
        if (player1.FinalScore >=winScore):
            return player1.Name

        elif (player2.FinalScore >= winScore):
            return player2.Name

        else:
            return False

    def FinalScore(self,playerObject):
        __fs=finalScore()
        playerObject.FinalScore=__fs.calculateScore(playerObject.FinalScore,playerObject.TempScore)
        return playerObject.FinalScore

    def GameConfiguration(self,WinningScore):
        winScore=WinningScore
        return True




g=game()
g.startMainGame()