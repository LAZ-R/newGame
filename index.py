import quizzAnimaux
import morseEncode
import calculMultiples
import calculVolume
import conversionEuros

def menuValueIsTrue(condition):
    menuAskMsg = "\t1 : Quizz Animalier\n\t2 : Encodeur Morse\n\t3 : Calcul de Multiples\n\t4 : Volume d'un Parrallélépipède Rectangle\n\t5 : Convertisseur d'Euros\n\n\t0 : Quitter\n\n"
    menuValueErrorMsg = "Merci de n'utiliser que les caractères proposés.\n"
    while True:
        try:
            val=(input(menuAskMsg))
            if val=="<3":
                print("<3")
                pass
            else:
                val=float(val)
                if condition(val):
                    return val
        except:
            pass
        menuAskMsg=menuValueErrorMsg
def index():
    print("\n\t*    Menu    *\n")

    menuValue=menuValueIsTrue(lambda x: 0<= x<= 5)

    if menuValue==1:
        quizzAnimaux.quizzAnimaux()
        index()

    elif menuValue==2:
        morseEncode.morseEncode()
        index()
    elif menuValue==3:
        calculMultiples.calculMultiples()
        index()
    elif menuValue==4:
        calculVolume.calculVolume()
        index()
    elif menuValue==5:
        conversionEuros.conversionEuros()
        index()

    else :
        print("Au Revoir")
index()