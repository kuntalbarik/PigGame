from PigGame.INTERFACE.iScore import score


class tempScore(score):
    def calculateScore(self,tempscore):
        self.__tempscore = tempscore
        return self.__tempscore