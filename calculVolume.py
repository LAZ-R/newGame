def positiveFloatIsTrue(Ask):
    positiveFloatErrorMsg = "\nEntrez une valeur valide\n(Chiffre ou nombre supérieur à 0, utilisez un point (.) pour les décimales)\n"
    while True:

        try:
            value = float(input(Ask))
            if value > 0 :
                return value
        except:
            pass
        print(positiveFloatErrorMsg)

def calculVolume():    

    print("\n\t*    Volume d'un Parallélépipède Rectangle    *\n")

    longueur = positiveFloatIsTrue("\tLongueur ?\n")
    largeur = positiveFloatIsTrue("\tLargeur ?\n")
    hauteur = positiveFloatIsTrue("\tHauteur ?\n")
    volume = longueur*largeur*hauteur

    print("\n\tVolume =\n\n       ",volume,"U**3\n")