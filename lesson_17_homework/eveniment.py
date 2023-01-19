# Creati un program care va numara timpul pana la un eveniment
# Aplicatia trebuie sa permita utilizatorului sa introduca data si ora intr-un string conform urmatorului
# format: `31/12/2023 23:59` (dd/mm/YYYY HH:MM).
# Programul va verifica daca data aleasa este cu mai putin de un an innainte. Daca data este cu mai mult de un an innainte
# programul va arata o eroare si va ruga utilizatorul sa introduca din nou.
# De asemenea, programul va intreba de la utilizator care este evenimentul care il asteapta: Exemlu `Apare noul Iphone`
# Dupa ce datele au fost introduse si validate, programul va afisa fiecare secunda (cu ajutorul la `time.sleep`) timpul
# ramas pan la eveniment. Exemplu: `23 zile, 19 minute si 34 secunde au ramas pan la Apare noul Iphone`. 
from datetime import datetime,date,time
import time 


def zile_in_an():
    a = date(date.today().year, 1, 1)
    b = date(date.today().year, 12, 31)
    return (b-a).days + 1

def zile_ramase(eveniment):
    now = datetime.now()
    evn = datetime(eveniment.year, eveniment.month, eveniment.day)
    bb = (evn - now.today()).days + 1
    return bb

def secunde_ramase(eveniment):
    n = datetime.now()
    now = datetime(n.year, n.month, n.day, n.hour, n.minute, n.second)
    evn = datetime(now.year, eveniment.month, eveniment.day, eveniment.hour, eveniment.minute, eveniment.second)
    bb = (evn - now)
    return bb

def event1():
    print("format: `31/12/2023 23:59` (dd/mm/YYYY HH:MM)")
    data_si_ora = input("Data si ora: ")
    dd = datetime.strptime(data_si_ora, "%d/%m/%Y %H:%M")
    return dd


    
if __name__ == '__main__':
    nume = input("Nume eveniment: ")
    while True:
        eveniment = event1()
        bb = zile_ramase(eveniment)
        if bb >= 0:
            if bb < zile_in_an():
                while True:
                    dd = str(secunde_ramase(eveniment))
                    print(f"{bb} zile, {dd[13:-3]} minute si {dd[-2:]} secunde au ramas pan la {nume}")
                    time.sleep(1)
            
                
            