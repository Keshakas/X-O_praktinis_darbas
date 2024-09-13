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
    tikrinimas_x()


def zaidejas_o():
    print("Žaidėjas -----O-----")
    pasirinkimas = ivestis()
    lentele[pasirinkimas - 1] = "O"

    spausdinti_lentele()
    tikrinimas_o()


def komoiuteris_o():
    print("\nŽaidėjas -----O-----")
    pasirinkimas = kompiuterio_ivestis()
    print(f"Kompiuteris pasirinko {pasirinkimas}")
    lentele[pasirinkimas - 1] = "O"

    spausdinti_lentele()
    tikrinimas_o()


def tikrinimas_x():
    global rezultatas_x, lentele, komp_zaidimas
    if (((((((lentele[0] == lentele[1] == lentele[2] == "X" or
            lentele[3] == lentele[4] == lentele[5] == "X") or
            lentele[6] == lentele[7] == lentele[8] == "X") or
            lentele[0] == lentele[3] == lentele[6] == "X") or
            lentele[1] == lentele[4] == lentele[7] == "X") or
            lentele[2] == lentele[5] == lentele[8] == "X") or
            lentele[0] == lentele[4] == lentele[8] == "X") or
            lentele[2] == lentele[4] == lentele[6] == "X"):
        print("\n-- Laimėjo -- X -- žaidėjas! --")
        rezultatas_x += 1
        lentele = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        komp_zaidimas = False
    else:
        if lygiuju_tikrinimas(lentele):
            print("\n-- Žaidimas baigėsi lygiosiomis! --")
            lentele = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            if komp_zaidimas:
                komoiuteris_o()
            else:
                zaidejas_o()


def tikrinimas_o():
    global rezultatas_o, lentele, rezultatas_k, komp_zaidimas
    if (((((((lentele[0] == lentele[1] == lentele[2] == "O" or
            lentele[3] == lentele[4] == lentele[5] == "O") or
            lentele[6] == lentele[7] == lentele[8] == "O") or
            lentele[0] == lentele[3] == lentele[6] == "O") or
            lentele[1] == lentele[4] == lentele[7] == "O") or
            lentele[2] == lentele[5] == lentele[8] == "O") or
            lentele[0] == lentele[4] == lentele[8] == "O") or
            lentele[2] == lentele[4] == lentele[6] == "O"):
        print("\n-- Laimėjo -- O -- žaidėjas! --")
        lentele = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if komp_zaidimas:
            rezultatas_k += 1
        else:
            rezultatas_o += 1
        komp_zaidimas = False
    else:
        if lygiuju_tikrinimas(lentele):
            print("\n-- Žaidimas baigėsi lygiosiomis! --")
            lentele = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            zaidejas_x()


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
        pasirinkimas = int(input("\n1 - Žaisti dviems  \n2 - Žaisti su kompiuteriu \n3 - Rezultatas \n4 - Išeiti \n"))
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
        print("Pasirinkte skaičių 1-3)")