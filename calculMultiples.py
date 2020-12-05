def intInput(msg, f, condition, errorMsg):
    while True:
        try:
            val=f(input(msg))
            if condition(val):
                return val
        except:
            pass
        msg=errorMsg
def calculMultiples():
    askPrimalValue="\tEntrez la table de multiplication pour laquelle vous voulez voir les 20 premier termes\n"
    askSecondValue="\tEntrez le nombre duquel vous voulez voir les multiples\n"
    errorIntValue="\tN'utilisez que des chiffres ou nombres entiers supérieurs à 0\n"
    b=1
    print("\n\t*    Calcul de Multiples    *\n")
    a, c=intInput(askPrimalValue, int, lambda x: 0 < x, errorIntValue), intInput(askSecondValue, int, lambda x: 0 < x, errorIntValue)
    ans=b*a
    while b<=20:
        if b==20 and ans%c==0:
            print("\t", a, "x", b, "=", ans, "(Multiple de", c, ")\n")
        elif b==20 and ans%c!=0:
            print("\t", a, "x", b, "=", ans, "\n")
        elif ans%c==0:
            print("\t", a, "x", b, "=", ans, "(Multiple de", c, ")")
        elif ans%c!=0:
            print("\t", a, "x", b, "=", ans)
        b=b+1
        ans=b*a