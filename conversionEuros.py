def inputFloatOk(msg, errorMsg):
        while True:
            try:
                val=float(input(msg))
                return val
            except:
                pass
            msg=errorMsg
def conversionEuros():
    
    tauxDollars=1.1861
    tauxLivres=0.9101
    tauxYen=124.3937
    print("\n\t*    Convertisseur d'Euros    *\n")

    euro=inputFloatOk("\tEntrez une valeur en Euros\n", "Entrez une valeur numérique (utilisez un point (.) pour les décimales)\n")

    dollars=euro*tauxDollars
    livres=euro*tauxLivres
    yen=euro*tauxYen

    print("\t", euro, "€  = ", dollars, "$")
    print("\t", euro, "€  = ", livres, "£")
    print("\t", euro, "€  = ", yen, "¥")