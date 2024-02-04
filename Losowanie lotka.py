import random

def losowanie_lotka():
    wylosowane_liczby = random.sample(range(1, 50), 6)
    return wylosowane_liczby

def typowanie_liczb():
    typowane_liczby = []
    for i in range(6):
        while True:
            typowana_liczba = input(f"Podaj {i+1} liczbę z zakresu 1-49: ")
            try:
                typowana_liczba = int(typowana_liczba)
                if typowana_liczba < 1 or typowana_liczba > 49:
                    print("Liczba musi być z przedziału 1-49")
                elif typowana_liczba in typowane_liczby:
                    print("Liczba już była podana")
                else:
                    typowane_liczby.append(typowana_liczba)
                    break
            except ValueError:
                print("Nieprawidłowy format liczby")
    return typowane_liczby

trafione_liczby = []

def porownanie_liczb(wylosowane_liczby, typowane_liczby):
    for element in wylosowane_liczby:
        if element in typowane_liczby:
            trafione_liczby .append(element)
    return trafione_liczby

while True:
    print("\nWitaj w programie TOTOLOTKA")
    print("Wybierz jedną z opcji:\n1. Losuj liczby\n2. Wyjdź z programu")
    wybor = input("Twój wybór: ")
    if wybor == "1":
        wylosowane_liczby = losowanie_lotka()
        typowane_liczby = typowanie_liczb()
        trafione_liczby = porownanie_liczb(wylosowane_liczby, typowane_liczby)
        print(f"Wylosowane liczby: {wylosowane_liczby}")
        print(f"Twoje typy: {typowane_liczby}")
        print(f"Liczby trafione: {trafione_liczby}")
    elif wybor == "2":
        print("Dziękujemy za skorzystanie z programu TOTOLOTKA")
        break
    else:
        print("Nieprawidłowy wybór")