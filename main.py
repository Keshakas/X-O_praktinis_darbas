lentele = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def Spausdinti_lentele():
    print("\n|", lentele[0], "|", lentele[1], "|", lentele[2], "|")
    print("|", lentele[3], "|", lentele[4], "|", lentele[5], "|")
    print("|", lentele[6], "|", lentele[7], "|", lentele[8], "|")


def ivestis():
    while True:
        pasirinkimas = input("Pasirinkite skaičių: ")
        if pasirinkimas.isdigit() and 1 <= int(pasirinkimas) <= 9:
            return int(pasirinkimas)
        else:
            print("Klaida: bandykite dar kartą")


def Zaidejas_x():
    print("Žaidėjas -----X-----")
    pasirinkimas = ivestis()
    match pasirinkimas:
        case 1: lentele[0] = "X"
        case 2: lentele[1] = "X"
        case 3: lentele[2] = "X"
        case 4: lentele[3] = "X"
        case 5: lentele[4] = "X"
        case 6: lentele[5] = "X"
        case 7: lentele[6] = "X"
        case 8: lentele[7] = "X"
        case 9: lentele[8] = "X"

    Spausdinti_lentele()
    Tikrinimas_x()


def Zaidejas_o():
    print("Žaidėjas -----O-----")
    pasirinkimas = ivestis()
    match pasirinkimas:
        case 1: lentele[0] = "O"
        case 2: lentele[1] = "O"
        case 3: lentele[2] = "O"
        case 4: lentele[3] = "O"
        case 5: lentele[4] = "O"
        case 6: lentele[5] = "O"
        case 7: lentele[6] = "O"
        case 8: lentele[7] = "O"
        case 9: lentele[8] = "O"

    Spausdinti_lentele()
    Tikrinimas_o()


def Tikrinimas_x():
    if (((((((lentele[0] == lentele[1] == lentele[2] == "X" or
            lentele[3] == lentele[4] == lentele[5] == "X") or
            lentele[6] == lentele[7] == lentele[8] == "X") or
            lentele[0] == lentele[3] == lentele[6] == "X") or
            lentele[1] == lentele[4] == lentele[7] == "X") or
            lentele[2] == lentele[5] == lentele[8] == "X") or
            lentele[0] == lentele[4] == lentele[8] == "X") or
            lentele[2] == lentele[4] == lentele[6] == "X"):
        print("\n-- Laimėjo -X- žaidėjas! --")
    else:
        lygiuju_tikrinimas(lentele)
        if lygiuju_tikrinimas(lentele):
            print("\n-- Lygiosios! --")
        else:
            Zaidejas_o()


def Tikrinimas_o():
    if (((((((lentele[0] == lentele[1] == lentele[2] == "O" or
            lentele[3] == lentele[4] == lentele[5] == "O") or
            lentele[6] == lentele[7] == lentele[8] == "O") or
            lentele[0] == lentele[3] == lentele[6] == "O") or
            lentele[1] == lentele[4] == lentele[7] == "O") or
            lentele[2] == lentele[5] == lentele[8] == "O") or
            lentele[0] == lentele[4] == lentele[8] == "O") or
            lentele[2] == lentele[4] == lentele[6] == "O"):
        print("\n-- Laimėjo -O- žaidėjas! --")

    else:
        lygiuju_tikrinimas(lentele)
        if lygiuju_tikrinimas(lentele):
            print("\n-- Lygiosios! --")
        else:
            Zaidejas_x()


def lygiuju_tikrinimas(lentele):
    for langelis in lentele:
        if isinstance(langelis, (int, float)):
            return False
    return True


Spausdinti_lentele()
Zaidejas_x()