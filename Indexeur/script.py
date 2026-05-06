# DISCLAIMER : Je (Naxoméga) ne peux être tenu responsable sur l'usage que vous faites
# de cet outil, il est crée avec comme but de déduire les URLs des QR Codes sur les arrêts.
# COMMENT FONCTIONNE-IL ?
# Il utilise 3 variables qui vont s'incrémenter à chaque boucle, comme des chiffres, mais à la place,
# ce sont des lettres a-Z. Le script va charger l'url de base avec cette combinaison de 3 lettres
# et regarder si elle est valide ou pas (en vérifiant le titre du site), si elle l'est, 
# la combinaison ainsi que le nom de l'arrêt vont être affichés dans la console. Si elle ne l'est pas, l'outil continue.
# ET LES SERVEURS ALORS ?
# J'ai inutilement rallongé le code afin de laisser les serveurs souffler (mais pas le PC qui le lance :/ ) (voir lignes 39-504)
# De plus, lors de mes tests, les serveurs fonctionnaient toujours sans problèmes de temps de chargement anormalement long.
from urllib.request import urlopen



BASE_URL = "https://siv.optymo.fr/passage.php?ar="
STOP_ID_1 = "a"
STOP_ID_2 = "a"
STOP_ID_3 = "a"
FINAL_URL = None
FINISH = False
print("Scrapper Lancé !")


def request():
    global FINAL_URL
    page = urlopen(FINAL_URL)
    html = page.read().decode("utf-8")
    start_index = html.find("<title>") + len("<title>")
    end_index = html.find("</title>")
    title = html[start_index:end_index]
    return title
while True:
    FINAL_URL = BASE_URL + STOP_ID_1 + STOP_ID_2 + STOP_ID_3 + "01"
    head = request()
    if head[0:8] == "indéfini":
        pass
    else:
        print(f"{STOP_ID_1}{STOP_ID_2}{STOP_ID_3} = {head}")

    if STOP_ID_1 == "a":
        STOP_ID_1 = "b"
        continue
    elif STOP_ID_1 == "b":
        STOP_ID_1 = "c"
        continue
    elif STOP_ID_1 == "c":
        STOP_ID_1 = "d"
        continue
    elif STOP_ID_1 == "d":
        STOP_ID_1 = "e"
        continue
    elif STOP_ID_1 == "e":
        STOP_ID_1 = "f"
        continue
    elif STOP_ID_1 == "f":
        STOP_ID_1 = "g"
        continue
    elif STOP_ID_1 == "g":
        STOP_ID_1 = "h"
        continue
    elif STOP_ID_1 == "h":
        STOP_ID_1 = "i"
        continue
    elif STOP_ID_1 == "i":
        STOP_ID_1 = "j"
        continue
    elif STOP_ID_1 == "j":
        STOP_ID_1 = "k"
        continue
    elif STOP_ID_1 == "k":
        STOP_ID_1 = "l"
        continue
    elif STOP_ID_1 == "l":
        STOP_ID_1 = "m"
        continue
    elif STOP_ID_1 == "m":
        STOP_ID_1 = "n"
        continue
    elif STOP_ID_1 == "n":
        STOP_ID_1 = "o"
        continue
    elif STOP_ID_1 == "o":
        STOP_ID_1 = "p"
        continue
    elif STOP_ID_1 == "p":
        STOP_ID_1 = "q"
        continue
    elif STOP_ID_1 == "q":
        STOP_ID_1 = "r"
        continue
    elif STOP_ID_1 == "r":
        STOP_ID_1 = "s"
        continue
    elif STOP_ID_1 == "s":
        STOP_ID_1 = "t"
        continue
    elif STOP_ID_1 == "t":
        STOP_ID_1 = "u"
        continue
    elif STOP_ID_1 == "u":
        STOP_ID_1 = "v"
        continue
    elif STOP_ID_1 == "v":
        STOP_ID_1 = "w"
        continue
    elif STOP_ID_1 == "w":
        STOP_ID_1 = "x"
        continue
    elif STOP_ID_1 == "x":
        STOP_ID_1 = "y"
        continue
    elif STOP_ID_1 == "y":
        STOP_ID_1 = "z"
        continue
    elif STOP_ID_1 == "z":
        STOP_ID_1 = "A"
        continue
    elif STOP_ID_1 == "A":
        STOP_ID_1 = "B"
        continue
    elif STOP_ID_1 == "B":
        STOP_ID_1 = "C"
        continue
    elif STOP_ID_1 == "C":
        STOP_ID_1 = "D"
        continue
    elif STOP_ID_1 == "D":
        STOP_ID_1 = "E"
        continue
    elif STOP_ID_1 == "E":
        STOP_ID_1 = "F"
        continue
    elif STOP_ID_1 == "F":
        STOP_ID_1 = "G"
        continue
    elif STOP_ID_1 == "G":
        STOP_ID_1 = "H"
        continue
    elif STOP_ID_1 == "H":
        STOP_ID_1 = "I"
        continue
    elif STOP_ID_1 == "I":
        STOP_ID_1 = "J"
        continue
    elif STOP_ID_1 == "J":
        STOP_ID_1 = "K"
        continue
    elif STOP_ID_1 == "K":
        STOP_ID_1 = "L"
        continue
    elif STOP_ID_1 == "L":
        STOP_ID_1 = "M"
        continue
    elif STOP_ID_1 == "M":
        STOP_ID_1 = "N"
        continue
    elif STOP_ID_1 == "N":
        STOP_ID_1 = "O"
        continue
    elif STOP_ID_1 == "O":
        STOP_ID_1 = "P"
        continue
    elif STOP_ID_1 == "P":
        STOP_ID_1 = "Q"
        continue
    elif STOP_ID_1 == "Q":
        STOP_ID_1 = "R"
        continue
    elif STOP_ID_1 == "R":
        STOP_ID_1 = "S"
        continue
    elif STOP_ID_1 == "S":
        STOP_ID_1 = "T"
        continue
    elif STOP_ID_1 == "T":
        STOP_ID_1 = "U"
        continue
    elif STOP_ID_1 == "U":
        STOP_ID_1 = "V"
        continue
    elif STOP_ID_1 == "V":
        STOP_ID_1 = "W"
        continue
    elif STOP_ID_1 == "W":
        STOP_ID_1 = "X"
        continue
    elif STOP_ID_1 == "X":
        STOP_ID_1 = "Y"
        continue
    elif STOP_ID_1 == "Y":
        STOP_ID_1 = "Z"
        continue
    if STOP_ID_1 == "Z":
        STOP_ID_1 = "a"
        if STOP_ID_2 == "a":
            STOP_ID_2 = "b"
            continue
        elif STOP_ID_2 == "b":
            STOP_ID_2 = "c"
            continue
        elif STOP_ID_2 == "c":
            STOP_ID_2 = "d"
            continue
        elif STOP_ID_2 == "d":
            STOP_ID_2 = "e"
            continue
        elif STOP_ID_2 == "e":
            STOP_ID_2 = "f"
            continue
        elif STOP_ID_2 == "f":
            STOP_ID_2 = "g"
            continue
        elif STOP_ID_2 == "g":
            STOP_ID_2 = "h"
            continue
        elif STOP_ID_2 == "h":
            STOP_ID_2 = "i"
            continue
        elif STOP_ID_2 == "i":
            STOP_ID_2 = "j"
            continue
        elif STOP_ID_2 == "j":
            STOP_ID_2 = "k"
            continue
        elif STOP_ID_2 == "k":
            STOP_ID_2 = "l"
            continue
        elif STOP_ID_2 == "l":
            STOP_ID_2 = "m"
            continue
        elif STOP_ID_2 == "m":
            STOP_ID_2 = "n"
            continue
        elif STOP_ID_2 == "n":
            STOP_ID_2 = "o"
            continue
        elif STOP_ID_2 == "o":
            STOP_ID_2 = "p"
            continue
        elif STOP_ID_2 == "p":
            STOP_ID_2 = "q"
            continue
        elif STOP_ID_2 == "q":
            STOP_ID_2 = "r"
            continue
        elif STOP_ID_2 == "r":
            STOP_ID_2 = "s"
            continue
        elif STOP_ID_2 == "s":
            STOP_ID_2 = "t"
            continue
        elif STOP_ID_2 == "t":
            STOP_ID_2 = "u"
            continue
        elif STOP_ID_2 == "u":
            STOP_ID_2 = "v"
            continue
        elif STOP_ID_2 == "v":
            STOP_ID_2 = "w"
            continue
        elif STOP_ID_2 == "w":
            STOP_ID_2 = "x"
            continue
        elif STOP_ID_2 == "x":
            STOP_ID_2 = "y"
            continue
        elif STOP_ID_2 == "y":
            STOP_ID_2 = "z"
            continue
        elif STOP_ID_2 == "z":
            STOP_ID_2 = "A"
            continue
        elif STOP_ID_2 == "A":
            STOP_ID_2 = "B"
            continue
        elif STOP_ID_2 == "B":
            STOP_ID_2 = "C"
            continue
        elif STOP_ID_2 == "C":
            STOP_ID_2 = "D"
            continue
        elif STOP_ID_2 == "D":
            STOP_ID_2 = "E"
            continue
        elif STOP_ID_2 == "E":
            STOP_ID_2 = "F"
            continue
        elif STOP_ID_2 == "F":
            STOP_ID_2 = "G"
            continue
        elif STOP_ID_2 == "G":
            STOP_ID_2 = "H"
            continue
        elif STOP_ID_2 == "H":
            STOP_ID_2 = "I"
            continue
        elif STOP_ID_2 == "I":
            STOP_ID_2 = "J"
            continue
        elif STOP_ID_2 == "J":
            STOP_ID_2 = "K"
            continue
        elif STOP_ID_2 == "K":
            STOP_ID_2 = "L"
            continue
        elif STOP_ID_2 == "L":
            STOP_ID_2 = "M"
            continue
        elif STOP_ID_2 == "M":
            STOP_ID_2 = "N"
            continue
        elif STOP_ID_2 == "N":
            STOP_ID_2 = "O"
            continue
        elif STOP_ID_2 == "O":
            STOP_ID_2 = "P"
            continue
        elif STOP_ID_2 == "P":
            STOP_ID_2 = "Q"
            continue
        elif STOP_ID_2 == "Q":
            STOP_ID_2 = "R"
            continue
        elif STOP_ID_2 == "R":
            STOP_ID_2 = "S"
            continue
        elif STOP_ID_2 == "S":
            STOP_ID_2 = "T"
            continue
        elif STOP_ID_2 == "T":
            STOP_ID_2 = "U"
            continue
        elif STOP_ID_2 == "U":
            STOP_ID_2 = "V"
            continue
        elif STOP_ID_2 == "V":
            STOP_ID_2 = "W"
            continue
        elif STOP_ID_2 == "W":
            STOP_ID_2 = "X"
            continue
        elif STOP_ID_2 == "X":
            STOP_ID_2 = "Y"
            continue
        elif STOP_ID_2 == "Y":
            STOP_ID_2 = "Z"
            continue
        if STOP_ID_2 == "Z":
            STOP_ID_2 = "a"
            if STOP_ID_3 == "a":
                STOP_ID_3 = "b"
                continue
            elif STOP_ID_3 == "b":
                STOP_ID_3 = "c"
                continue
            elif STOP_ID_3 == "c":
                STOP_ID_3 = "d"
                continue
            elif STOP_ID_3 == "d":
                STOP_ID_3 = "e"
                continue
            elif STOP_ID_3 == "e":
                STOP_ID_3 = "f"
                continue
            elif STOP_ID_3 == "f":
                STOP_ID_3 = "g"
                continue
            elif STOP_ID_3 == "g":
                STOP_ID_3 = "h"
                continue
            elif STOP_ID_3 == "h":
                STOP_ID_3 = "i"
                continue
            elif STOP_ID_3 == "i":
                STOP_ID_3 = "j"
                continue
            elif STOP_ID_3 == "j":
                STOP_ID_3 = "k"
                continue
            elif STOP_ID_3 == "k":
                STOP_ID_3 = "l"
                continue
            elif STOP_ID_3 == "l":
                STOP_ID_3 = "m"
                continue
            elif STOP_ID_3 == "m":
                STOP_ID_3 = "n"
                continue
            elif STOP_ID_3 == "n":
                STOP_ID_3 = "o"
                continue
            elif STOP_ID_3 == "o":
                STOP_ID_3 = "p"
                continue
            elif STOP_ID_3 == "p":
                STOP_ID_3 = "q"
                continue
            elif STOP_ID_3 == "q":
                STOP_ID_3 = "r"
                continue
            elif STOP_ID_3 == "r":
                STOP_ID_3 = "s"
                continue
            elif STOP_ID_3 == "s":
                STOP_ID_3 = "t"
                continue
            elif STOP_ID_3 == "t":
                STOP_ID_3 = "u"
                continue
            elif STOP_ID_3 == "u":
                STOP_ID_3 = "v"
                continue
            elif STOP_ID_3 == "v":
                STOP_ID_3 = "w"
                continue
            elif STOP_ID_3 == "w":
                STOP_ID_3 = "x"
                continue
            elif STOP_ID_3 == "x":
                STOP_ID_3 = "y"
                continue
            elif STOP_ID_3 == "y":
                STOP_ID_3 = "z"
                continue
            elif STOP_ID_3 == "z":
                STOP_ID_3 = "A"
                continue
            elif STOP_ID_3 == "A":
                STOP_ID_3 = "B"
                continue
            elif STOP_ID_3 == "B":
                STOP_ID_3 = "C"
                continue
            elif STOP_ID_3 == "C":
                STOP_ID_3 = "D"
                continue
            elif STOP_ID_3 == "D":
                STOP_ID_3 = "E"
                continue
            elif STOP_ID_3 == "E":
                STOP_ID_3 = "F"
                continue
            elif STOP_ID_3 == "F":
                STOP_ID_3 = "G"
                continue
            elif STOP_ID_3 == "G":
                STOP_ID_3 = "H"
                continue
            elif STOP_ID_3 == "H":
                STOP_ID_3 = "I"
                continue
            elif STOP_ID_3 == "I":
                STOP_ID_3 = "J"
                continue
            elif STOP_ID_3 == "J":
                STOP_ID_3 = "K"
                continue
            elif STOP_ID_3 == "K":
                STOP_ID_3 = "L"
                continue
            elif STOP_ID_3 == "L":
                STOP_ID_3 = "M"
                continue
            elif STOP_ID_3 == "M":
                STOP_ID_3 = "N"
                continue
            elif STOP_ID_3 == "N":
                STOP_ID_3 = "O"
                continue
            elif STOP_ID_3 == "O":
                STOP_ID_3 = "P"
                continue
            elif STOP_ID_3 == "P":
                STOP_ID_3 = "Q"
                continue
            elif STOP_ID_3 == "Q":
                STOP_ID_3 = "R"
                continue
            elif STOP_ID_3 == "R":
                STOP_ID_3 = "S"
                continue
            elif STOP_ID_3 == "S":
                STOP_ID_3 = "T"
                continue
            elif STOP_ID_3 == "T":
                STOP_ID_3 = "U"
                continue
            elif STOP_ID_3 == "U":
                STOP_ID_3 = "V"
                continue
            elif STOP_ID_3 == "V":
                STOP_ID_3 = "W"
                continue
            elif STOP_ID_3 == "W":
                STOP_ID_3 = "X"
                continue
            elif STOP_ID_3 == "X":
                STOP_ID_3 = "Y"
                continue
            elif STOP_ID_3 == "Y":
                STOP_ID_3 = "Z"
                continue
            if STOP_ID_3 == "Z":
                break



