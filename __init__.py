class importing:
    def imports(self):
        from PigGame.COMMON.tournamentGame import tournament
        from PigGame.COMMON.challengeGame import challenge
        from PigGame.COMMON.humanPlayer import human
        from PigGame.COMMON.computerPlayer import computer
        from PigGame.COMMON.finalScore import finalScore
        from PigGame.COMMON.tempScore import tempScore
        from PigGame.COMMON.Logs import logPrint
        import json, os, sys, locale

        ###choosing the language
        language = locale.setlocale(locale.LC_ALL, '')
        language = language[0:2]
        ###choosing the json for selected language
        path = "../DTO/res_" + language + ".json"
        ####setting the path of json file
        absfilepath = os.path.abspath(__file__)
        fileDir = os.path.dirname(absfilepath)
        filename = os.path.join(fileDir, path)
        filename = os.path.abspath(os.path.realpath(filename))
        readJson = open(filename, "r")
        data = json.load(readJson)
        log = logPrint()
