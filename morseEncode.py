from unidecode import unidecode


def morseEncode():
    # liste en morse
    space = "    "
    a = "• ▬"
    b = "▬ • • •"
    c = "▬ • ▬ •"
    d = "▬ • •"
    e = "•"
    f = "• • ▬ •"
    g = "▬ ▬ •"
    h = "• • • •"
    i = "• •"
    j = "• ▬ ▬ ▬"
    k = "▬ • ▬"
    l = "• ▬ • •"
    m = "▬ ▬"
    n = "▬ •"
    o = "▬ ▬ ▬"
    p = "• ▬ ▬ •"
    q = "▬ ▬ • ▬"
    r = "• ▬ •"
    s = "• • •"
    t = "▬"
    u = "• • ▬"
    v = "• • • ▬"
    w = "• ▬ ▬"
    x = "▬ • • ▬"
    y = "▬ • ▬ ▬"
    z = "▬ ▬ • •"
    zero = "▬ ▬ ▬ ▬ ▬"
    one = "• ▬ ▬ ▬ ▬"
    two = "• • ▬ ▬ ▬"
    three = "• • • ▬ ▬"
    four = "• • • • ▬"
    five = "• • • • •"
    six = "▬ • • • •"
    seven = "▬ ▬ • • •"
    eight = "▬ ▬ ▬ • •"
    nine = "▬ ▬ ▬ ▬ •"
    multiplier = 0
    print("\n\t*    Encodeur Morse    *\n")
    print('\tCaractères autorisés: Alphabet Latin & Chiffres\n\t(tout autre caractère amènera à une conversion en "#")\n')
    finalUserInput = unidecode(
        input('\tEntrez le texte à encoder:\n\n')).lower()
    print("\n\tTexte encodé en Morse:\n")
    strLenght = len(finalUserInput)
    while multiplier < strLenght:
        if finalUserInput[multiplier] == " ":
            print(space, end="")
        elif finalUserInput[multiplier] == "a":
            print(a, end="   ")
        elif finalUserInput[multiplier] == "b":
            print(b, end="   ")
        elif finalUserInput[multiplier] == "c":
            print(c, end="   ")
        elif finalUserInput[multiplier] == "d":
            print(d, end="   ")
        elif finalUserInput[multiplier] == "e":
            print(e, end="   ")
        elif finalUserInput[multiplier] == "f":
            print(f, end="   ")
        elif finalUserInput[multiplier] == "g":
            print(g, end="   ")
        elif finalUserInput[multiplier] == "h":
            print(h, end="   ")
        elif finalUserInput[multiplier] == "i":
            print(i, end="   ")
        elif finalUserInput[multiplier] == "j":
            print(j, end="   ")
        elif finalUserInput[multiplier] == "k":
            print(k, end="   ")
        elif finalUserInput[multiplier] == "l":
            print(l, end="   ")
        elif finalUserInput[multiplier] == "m":
            print(m, end="   ")
        elif finalUserInput[multiplier] == "n":
            print(n, end="   ")
        elif finalUserInput[multiplier] == "o":
            print(o, end="   ")
        elif finalUserInput[multiplier] == "p":
            print(p, end="   ")
        elif finalUserInput[multiplier] == "q":
            print(q, end="   ")
        elif finalUserInput[multiplier] == "r":
            print(r, end="   ")
        elif finalUserInput[multiplier] == "s":
            print(s, end="   ")
        elif finalUserInput[multiplier] == "t":
            print(t, end="   ")
        elif finalUserInput[multiplier] == "u":
            print(u, end="   ")
        elif finalUserInput[multiplier] == "v":
            print(v, end="   ")
        elif finalUserInput[multiplier] == "w":
            print(w, end="   ")
        elif finalUserInput[multiplier] == "x":
            print(x, end="   ")
        elif finalUserInput[multiplier] == "y":
            print(y, end="   ")
        elif finalUserInput[multiplier] == "z":
            print(z, end="   ")
        elif finalUserInput[multiplier] == "0":
            print(zero, end="   ")
        elif finalUserInput[multiplier] == "1":
            print(one, end="   ")
        elif finalUserInput[multiplier] == "2":
            print(two, end="   ")
        elif finalUserInput[multiplier] == "3":
            print(three, end="   ")
        elif finalUserInput[multiplier] == "4":
            print(four, end="   ")
        elif finalUserInput[multiplier] == "5":
            print(five, end="   ")
        elif finalUserInput[multiplier] == "6":
            print(six, end="   ")
        elif finalUserInput[multiplier] == "7":
            print(seven, end="   ")
        elif finalUserInput[multiplier] == "8":
            print(eight, end="   ")
        elif finalUserInput[multiplier] == "9":
            print(nine, end="   ")
        else:
            print("#", end="   ")
        multiplier = multiplier+1
    print("\n")
