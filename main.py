import random

lentele = [1, 2, 3, 4, 5, 6, 7, 8, 9]
rezultatas_x = 0
rezultatas_o = 0
rezultatas_k = 0
komp_zaidimas = False

def spausdinti_lentele():
    print("\n|", lentele[6], "|", lentele[7], "|", lentele[8], "|")
    print("|", lentele[3], "|", lentele[4], "|", lentele[5], "|")
    print("|", lentele[0], "|", lentele[1], "|", lentele[2], "|")


def ivestis():
    while True:
        pasirinkimas = input("Pasirinkite skaičių: ")
        if pasirinkimas.isdigit() and 1 <= int(pasirinkimas) <= 9:
            if lentele[int(pasirinkimas) - 1] not in ["X", "O"]:
                return int(pasirinkimas)
            else:
                print("Klaida: Ši vieta jau užimta. Bandykite kitą skaičių.")
        else:
            print("Klaida: netinkamas simbolis")


def kompiuterio_ivestis():
    while True:
        pasirinkimas = random.randint(1, 9)
        if lentele[int(pasirinkimas) - 1] not in ["X", "O"]:
            return int(pasirinkimas)


def zaidejas_x():
    print("Žaidėjas -----X-----")
    pasirinkimas = ivestis()
    lentele[pasirinkimas - 1] = "X"
    spausdinti_lentele()
    laimejimo_tikrinimas("X")


def zaidejas_o():
    print("Žaidėjas -----O-----")
    pasirinkimas = ivestis()
    lentele[pasirinkimas - 1] = "O"
    spausdinti_lentele()
    laimejimo_tikrinimas("O")


def kompiuteris_o():
    print("\nŽaidėjas -----O-----")
    pasirinkimas = kompiuterio_ivestis()
    print(f"Kompiuteris pasirinko {pasirinkimas}")
    lentele[pasirinkimas - 1] = "O"
    spausdinti_lentele()
    laimejimo_tikrinimas("O")


def laimejimo_tikrinimas(simbolis):
    global rezultatas_x, rezultatas_k, rezultatas_o, lentele, komp_zaidimas
    if (((((((lentele[0] == lentele[1] == lentele[2] == simbolis or
            lentele[3] == lentele[4] == lentele[5] == simbolis) or
            lentele[6] == lentele[7] == lentele[8] == simbolis) or
            lentele[0] == lentele[3] == lentele[6] == simbolis) or
            lentele[1] == lentele[4] == lentele[7] == simbolis) or
            lentele[2] == lentele[5] == lentele[8] == simbolis) or
            lentele[0] == lentele[4] == lentele[8] == simbolis) or
            lentele[2] == lentele[4] == lentele[6] == simbolis):
        print(f"\n-- Laimėjo -- {simbolis} -- žaidėjas! --")
        lentele = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if komp_zaidimas and simbolis == "O":
            rezultatas_k += 1
        else:
            if simbolis == "O":
                rezultatas_o += 1
            else:
                rezultatas_x += 1
        komp_zaidimas = False
    else:
        if lygiuju_tikrinimas(lentele):
            print("\n-- Žaidimas baigėsi lygiosiomis! --")
            lentele = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            komp_zaidimas = False
        else:
            if komp_zaidimas and simbolis == "X":
                kompiuteris_o()
            else:
                if simbolis == "O":
                    zaidejas_x()
                else:
                    if simbolis == "X":
                        zaidejas_o()


def lygiuju_tikrinimas(lentele):
    for langelis in lentele:
        if isinstance(langelis, int):
            return False
    return True


def rezultatas():
    print(f"REZULTATAS:\nŽaidėjas X  --> {rezultatas_x}\nŽaidėjas O  --> {rezultatas_o}\nKompiuteris --> {rezultatas_k}")


def zaidimo_pradzia():
    num = random.randint(1, 2)
    if num == 1:
        zaidejas_x()
    else:
        zaidejas_o()


print("\n-- KRYŽIUKŲ - NULIUKŲ ŽAIDIMAS --")
while True:
    try:
        pasirinkimas = int(input("\n1 - Žaisti dviems žaidėjams  \n2 - Žaisti su kompiuteriu \n3 - Rezultatas \n4 - Išeiti \n"))
        match pasirinkimas:
            case 1:
                print("Pirmasis žaidimo ėjimas \nparenkamas atsitiktine tvarka")
                spausdinti_lentele()
                zaidimo_pradzia()
            case 2:
                print("Kompiuteriui priskirtas \n-----O----- žaidėjas")
                komp_zaidimas = True
                spausdinti_lentele()
                zaidejas_x()
            case 3:
                rezultatas()
            case 4:
                break
    except ValueError:
        print("Pasirinkte skaičių 1-4)")