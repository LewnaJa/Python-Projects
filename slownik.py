import mysql.connector

def wyszukaj():
    selectLang = input("Znajdź słowo 1 - angielski, 2 - polski: ")
    if selectLang == "2":
        polish = input("Podaj polskie słówko, którego szukasz w słowniku: ")
        query = f"SELECT PolskieSlowo, AngielskieSlowo FROM slowa WHERE PolskieSlowo = '{polish}'"
        myCursor.execute(query)
        myResult = myCursor.fetchall()
        if len(myResult) != 0:
            print(myResult[0][0], " - ", myResult[0][1])
        else:
            print("Nie ma takiego słowka")
    elif selectLang == "1":
        english = input("Podaj angielskie słówko, które jest szukane: ")
        query = f"SELECT PolskieSlowo, AngielskieSlowo FROM slowa WHERE AngielskieSlowo = '{english}'"
        myCursor.execute(query)
        myResult = myCursor.fetchall()
        if len(myResult) != 0:
            print(myResult[0][0], " - ", myResult[0][1])
        else:
            print("Nie ma takiego słowka")
    else:
        print("Błąd")

def dodaj():
    polish = input("Podaj słowo polskie do dodania: ")
    english = input("Podaj słowo angielskie do dodania: ")
    query = f"INSERT INTO slowa (PolskieSlowo, AngielskieSlowo) VALUES ('{polish}', '{english}')"
    myCursor.execute(f"SELECT * FROM slowa WHERE AngielskieSlowo = '{english}' AND PolskieSlowo = '{polish}'")
    results = myCursor.fetchall()
    if len(results) == 0:
        myCursor.execute(query)
        connect.commit()
    else:
        print("Mamy już takie słowo")

def usun():
    selectLang = input("Podaj język w którym chcesz usunąć słowo (1 - Angielski 2 - Polski): ")
    if selectLang == "1":
        english = input("Angielskie słowo: ")
        myCursor.execute(f"SELECT * FROM slowa WHERE AngielskieSlowo = '{english}'")
        res = myCursor.fetchall()
        if len(res) != 0:
            query = f"DELETE FROM slowa WHERE AngielskieSlowo = '{english}'"
            myCursor.execute(query)
            connect.commit()
        else:
            print("Nie ma takiego słowa")
    elif selectLang == "2":
        polish = input("Polskie słowo: ")
        myCursor.execute(f"SELECT * FROM slowa WHERE PolskieSlowo = '{polish}'")
        res = myCursor.fetchall()
        if len(res) != 0:
            query = f"DELETE FROM slowa WHERE PolskieSlowo = '{polish}'"
            myCursor.execute(query)
            connect.commit()
        else:
            print("Nie ma takiego słowa")
    else:
        print("Błąd")

def pokazslownik():
    print("POLSKI   ANGIELSKI")
    query = "SELECT PolskieSlowo, AngielskieSlowo FROM slowa"
    myCursor.execute(query)
    myResults = myCursor.fetchall()
    for x in myResults:
        print(x[0], "-", x[1])

def polaczenie():
    connect.close()
    exit()

while True:
    connect = mysql.connector.connect(host="localhost", user="root", password="", database="slownik")
    myCursor = connect.cursor()

    while True:
        print("""
Opcje do wybrania:
1. Wyszukaj słówko w słowniku
2. Dodaj słówko do słownika
3. Usuń słówko w słowniku
4. Wyświetl zawartość słownika
5. Wyjście
        """)

        opcja = input("Wybierz opcję: ")

        if opcja == "1":
            wyszukaj()
        elif opcja == "2":
            dodaj()
        elif opcja == "3":
            usun()
        elif opcja == "4":
            pokazslownik()
        elif opcja == "5":
            polaczenie()
        else:
            print("Nie ma takiej opcji. Wybierz ponownie...")
