def sprawdz_poprawnosc(symboly):
    stos = []

    otwarte_symbole = ['(', '[', '{']
    zamkniete_symbole = [')', ']', '}']

    for symbol in symboly:
        if symbol in otwarte_symbole:
            stos.append(symbol)
        elif symbol in zamkniete_symbole:
            if not stos:
                return False

            ostatni_symbol = stos.pop()
            indeks_zamknietego = zamkniete_symbole.index(symbol)
            indeks_otwartego = otwarte_symbole.index(ostatni_symbol)

            if indeks_zamknietego != indeks_otwartego:
                return False

    return len(stos) == 0


symboly1 = "({[]})"
print(sprawdz_poprawnosc(symboly1))

symboly2 = "({[)}"
print(sprawdz_poprawnosc(symboly2))
