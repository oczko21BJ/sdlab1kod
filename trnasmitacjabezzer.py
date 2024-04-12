# -*- coding: utf-8 -*-

import numpy as np

def kryterium_hurwitza(wspolczynniki):
    n = len(wspolczynniki)
    if n == 2:
        # Sprawdzenie warunków na stabilność
        D1 = wspolczynniki[0]
        D2 = wspolczynniki[1]

        if D1 > 0 and D2 > 0:
            return "stabilny asymptotycznie"
        elif D1 * D2 == 0:
            return "na granicy stabilności"
        else:
            return "niestabilny"
    else:
        return "Niepoprawna długość wektora współczynników"

def main():
    # Wprowadzenie współczynników transmitancji przez użytkownika
    print("Podaj współczynniki transmitancji G(s):")
    b0 = float(input("Podaj współczynnik b0: "))
    b1 = float(input("Podaj współczynnik b1: "))
    b2 = float(input("Podaj współczynnik b2: "))
    a1 = float(input("Podaj współczynnik a1: "))
    a2 = float(input("Podaj współczynnik a2: "))

    # Obliczenie współczynników macierzy Hurwitza
    D1 = b1
    D2 = b0*a1 - b1*a2
    print("Współczynniki macierzy Hurwitza:")
    print("D1 =", D1)
    print("D2 =", D2)

    # Analiza stabilności za pomocą kryterium Hurwitza
    wynik = kryterium_hurwitza([D1, D2])
    print("Wynik analizy stabilności układu:", wynik)

if __name__ == "__main__":
    main()
