# Homework

## Ex 1

Create a customer registration form from CLI.

The user should input **First Name**, **Last Name** and **Date Of Birth** in the following format as a
string `20/01/1930`.

The program should print out `Customer First Name, Last Name has birthday in n days` where `n` is the number of days
until the customers birthday.

### RO

Creati un program care va permite inregistrarea unui client.

Utilizatorul va introduce **Numele**, **Prenumele** si **Ziua de naster** a clientului in formatul `20/01/1930`

Programul trebuie sa afiseze urmatoarea `Clientul Nume, Prenume va avea ziua de nastere in n zile` unde `n` este numarul
de zile pan la urmatoarea zi de nastere a clientului.

## Ex 2

Create a countdown application.

The application should let the user to type in a date and time in the following format as a single
string: `31/12/2023 23:59` (dd/mm/YYYY HH:MM).

The program should check if the date is not further than one year in the future. If the date is further, then show an
error message and let the user type in a new date and time.

The program should also let the user type in the event for the countdown: Example `New Iphone Releases`

After the input has been taken and validated the program should show time remaining until the desired date and time in
days, minutes and seconds: For example: `23 days 19 minutes 34 seconds left until New Iphone Releases` and should update
every second (Note:
Use `time.sleep`)

### RO

Creati un program care va numara timpul pana la un eveniment

Aplicatia trebuie sa permita utilizatorului sa introduca data si ora intr-un string conform urmatorului
format: `31/12/2023 23:59` (dd/mm/YYYY HH:MM).

Programul va verifica daca data aleasa este cu mai putin de un an innainte. Daca data este cu mai mult de un an innainte
programul va arata o eroare si va ruga utilizatorul sa introduca din nou.

De asemenea, programul va intreba de la utilizator care este evenimentul care il asteapta: Exemlu `Apare noul Iphone`

Dupa ce datele au fost introduse si validate, programul va afisa fiecare secunda (cu ajutorul la `time.sleep`) timpul
ramas pan la eveniment. Exemplu: `23 zile, 19 minute si 34 secunde au ramas pan la Apare noul Iphone`. 
