# Creati un program care va permite inregistrarea unui client.
# Utilizatorul va introduce **Numele**, **Prenumele** si **Ziua de naster** a clientului in formatul `20/01/1930`
# Programul trebuie sa afiseze urmatoarea `Clientul Nume, Prenume va avea ziua de nastere in n zile` 
# unde `n` este numarul de zile pan la urmatoarea zi de nastere a clientului.

from datetime import datetime,date


def data_nastere():
    day = int(input('Zi? [DD]: '))
    month = int(input('Luna [MM]: '))
    year = int(input('Anul [YY]: '))
    return datetime(year,month,day)

def zile_ramase(birthyday):
    now = datetime.now()
    birthday = datetime(now.year, birthyday.month, birthyday.day)
    bb = (birthday - now.today()).days + 1
    if bb >= 0:
        return bb
    return bb + zile_in_an()

def zile_in_an():
    a = date(date.today().year, 1, 1)
    b = date(date.today().year, 12, 31)
    return (b-a).days + 1

if __name__ == '__main__':       
    nume = input("Nume: ")
    pren = input("Prenume: ")
    bd = data_nastere()
    zr = zile_ramase(bd)
    if zr == 0:
        print(f"{nume} {pren} - La multi ani!")
    else:
        print(f"Clientul {nume} {pren} va avea ziua de nastere in {zr} zile")
    # now = datetime.now()
    # print((now.today().year))
    # print(zile_in_an())
    