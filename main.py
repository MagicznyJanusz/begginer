def oblicz_srednie(liczby):
    suma = sum(liczby)
    srednia_arytmetyczna = suma / len(liczby)
    srednia_harmoniczna = len(liczby) / sum(1 / x for x in liczby)
    return srednia_arytmetyczna, srednia_harmoniczna


def main():
    liczby = []

    while True:
        liczba = input("Podaj liczbę rzeczywistą lub wpisz 'koniec' aby zakończyć: ")
        if liczba.lower() == "koniec":
            break
        try:
            liczba = float(liczba)
            liczby.append(liczba)
        except ValueError:
            print("To nie jest prawidłowa liczba. Spróbuj jeszcze raz.")

    if not liczby:
        print("Nie podano żadnych liczb.")
        return

    srednia_arytmetyczna, srednia_harmoniczna = oblicz_srednie(liczby)

    print("Podane liczby to:", liczby)
    print("Średnia arytmetyczna: {:.2f}".format(srednia_arytmetyczna))
    print("Średnia harmoniczna: {:.2f}".format(srednia_harmoniczna))

    print("Liczby większe od średniej arytmetycznej:")
    for liczba in liczby:
        if liczba > srednia_arytmetyczna:
            print(liczba, end=" ")

    print("\nLiczby większe od średniej harmonicznej:")
    for liczba in liczby:
        if liczba > srednia_harmoniczna:
            print(liczba, end=" ")


if __name__ == "__main__":
    main()