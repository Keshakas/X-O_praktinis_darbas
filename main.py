import random

lentele = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def spausdinti_lentele():
    print("\n|", lentele[0], "|", lentele[1], "|", lentele[2], "|")
    print("|", lentele[3], "|", lentele[4], "|", lentele[5], "|")
    print("|", lentele[6], "|", lentele[7], "|", lentele[8], "|")


def ivestis():
    while True:
        pasirinkimas = input("Pasirinkite skaičių (1-9): ")
        if pasirinkimas.isdigit() and 1 <= int(pasirinkimas) <= 9:
            if lentele[int(pasirinkimas) - 1] not in ["X", "O"]:
                return int(pasirinkimas)
            else:
                print("Klaida: Ši vieta jau užimta. Bandykite kitą skaičių.")
        else:
            print("Klaida: netinkamas simbolis")


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


def tikrinimas_x():
    if (((((((lentele[0] == lentele[1] == lentele[2] == "X" or
            lentele[3] == lentele[4] == lentele[5] == "X") or
            lentele[6] == lentele[7] == lentele[8] == "X") or
            lentele[0] == lentele[3] == lentele[6] == "X") or
            lentele[1] == lentele[4] == lentele[7] == "X") or
            lentele[2] == lentele[5] == lentele[8] == "X") or
            lentele[0] == lentele[4] == lentele[8] == "X") or
            lentele[2] == lentele[4] == lentele[6] == "X"):
        print("\n-- Laimėjo -- X -- žaidėjas! --")
    else:
        lygiuju_tikrinimas(lentele)
        if lygiuju_tikrinimas(lentele):
            print("\n-- Žaidimas baigėsi lygiosiomis! --")
        else:
            zaidejas_o()


def tikrinimas_o():
    if (((((((lentele[0] == lentele[1] == lentele[2] == "O" or
            lentele[3] == lentele[4] == lentele[5] == "O") or
            lentele[6] == lentele[7] == lentele[8] == "O") or
            lentele[0] == lentele[3] == lentele[6] == "O") or
            lentele[1] == lentele[4] == lentele[7] == "O") or
            lentele[2] == lentele[5] == lentele[8] == "O") or
            lentele[0] == lentele[4] == lentele[8] == "O") or
            lentele[2] == lentele[4] == lentele[6] == "O"):
        print("\n-- Laimėjo -- O -- žaidėjas! --")

    else:
        lygiuju_tikrinimas(lentele)
        if lygiuju_tikrinimas(lentele):
            print("\n-- Žaidimas baigėsi lygiosiomis! --")
        else:
            zaidejas_x()


def lygiuju_tikrinimas(lentele):
    for langelis in lentele:
        if isinstance(langelis, int):
            return False
    return True


def zaidimo_pradzia():
    num = random.randint(1, 2)
    if num == 1:
        zaidejas_x()
    else:
        zaidejas_o()


print("\n-- Kryžiukų - nuliukų žaidimas --")
spausdinti_lentele()
zaidimo_pradzia()