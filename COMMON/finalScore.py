from PigGame.INTERFACE.iScore import score

class finalScore(score):
    def calculateScore (self,finalscore,tempscore):
        self.__finalscore=finalscore
        self.__tempscore=tempscore

        if(self.__tempscore==0):
            return 0
        else:
            return (self.__finalscore+self.__tempscore)