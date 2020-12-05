from unidecode import unidecode 

def isAnswerOk (askMsg, trueAnswer):
    winMsg="\tbravo\n"
    failMsg="\traté, essayes encore\n\n"
    while True:
        try:
            answer=unidecode(input(askMsg)).lower()
            if answer==trueAnswer:
                print(winMsg)
                return
        except:
            pass
        askMsg=failMsg

def quizzAnimaux():
    levelNumber=1
    
    print("\n\t*    Quizz animalier    *\n\n")

    print("\t---- Level", levelNumber, "----\n")
    isAnswerOk("\tGris, trompe\n\n", "elephant")
    levelNumber=levelNumber+1

    print("\t---- Level", levelNumber, "----\n")
    isAnswerOk("\tCheval, rayé\n\n", "zebre")
    levelNumber=levelNumber+1

    print("\t---- Level", levelNumber, "----\n")
    isAnswerOk("\tBoule, griffes\n\n", "tatou")
    levelNumber=levelNumber+1

    print("pour l'instant, c'est tout !")
