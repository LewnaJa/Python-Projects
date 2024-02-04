import random

# Funkcja do wybierania losowego słowa z pliku
def wybierz_losowe_slowo(nazwa_pliku):
    with open(nazwa_pliku, "r") as plik:
        slowa = plik.readlines()
    return random.choice(slowa).strip()

# Funkcja do rysowania wisielca
def rysuj_wisielca(bledy):
    wisielec = [
        "  ________",
        "  |     |",
        "  |     " + ("O" if bledy >= 1 else ""),
        "  |    " + ("/|\\" if bledy >= 3 else ("|" if bledy >= 2 else "")),
        "  |     " + ("/\\" if bledy >= 5 else ("/" if bledy >= 4 else "")),
        "__|__"
    ]
    for linia in wisielec:
        print(linia)

# Funkcja do ukrywania słowa
def ukryj_slowo(slowo, odgadniete_litery):
    ukryte = ""
    for litera in slowo:
        if litera in odgadniete_litery:
            ukryte += litera
        else:
            ukryte += "_"
    return ukryte

def graj():
    nazwa_pliku = "zgadnij.txt"
    slowo = wybierz_losowe_slowo(nazwa_pliku)
    odgadniete_litery = []
    bledy = 0

    print("Witaj w grze Wisielec!")
    print(ukryj_slowo(slowo, odgadniete_litery))

    while True:
        litera = input("Podaj literę: ").lower()

        if litera.isalpha() and len(litera) == 1:
            if litera in odgadniete_litery:
                print("Ta litera została już odgadnięta.")
            elif litera in slowo:
                odgadniete_litery.append(litera)
                print("Dobra robota! Odgadłeś literę.")
            else:
                odgadniete_litery.append(litera)
                bledy += 1
                print("Nie ma takiej litery.")
                rysuj_wisielca(bledy)

            ukryte = ukryj_slowo(slowo, odgadniete_litery)
            print(ukryte)

            if ukryte == slowo:
                print("Gratulacje! Odgadłeś słowo:", slowo)
                break

            if bledy >= 6:
                print("Przegrałeś! Słowo to:", slowo)
                break
        else:
            print("Podaj poprawną literę.")

if __name__ == "__main__":
    graj()