# Homework

## Ex 1


### ENG

Create a python program that will take as an input a `path` in the computer: ex: `C:\Program Files\`.

The program should list all files (and only files, not other folders) inside the folder if the path provided is a folder.

If the path is not a folder, the program should show a nice error: `Provided path is not a folder.`

If the path does not exist, the program should show a nice error: `Provided path does not exist.`


### RO

Creati un program care va primi ca input o cale (path) de fisiere din calculator: ex: `C:\Program Files\`.

Programul va trebui sa afiseze o lista de toate fisierele din mapa introdusa in input (doar fisierele, si nu alte mape).

Daca calea introdusa nu este o mapa, programul trebuie sa arate urmatoarea eroare: `Calea introdusa nu este o mapa`.

Daca calea introdusa nu exista, programul va trebuie sa arate urmatoare eroare: `Calea introdusa nu exista`.


### Hints:

Use: os.path.isdir, os.path.join(), os.listdir

## Ex2 - Bulk Rename

### ENG

Using functions you have created for the exercise above (ex1.) create a program that will take as input a path to a folder.

**WARNING**: Use a test path, with files specifically created for the test purpose. Be careful as to not change something is system folders.

The program should rename all files in the folder to numbers (from 1 to n) sorted by the creation date of the file: `os.path.getctime(file_path)` - will return the date created of the file.

The program should not overwrite the extension of the file: `file.extension` - For example `some_Doc.docx` should be renamed to `1.docx`.

Also add an option to add a prefix, for example: Prefix `doc` will rename all files to `doc1.docx`, `doc2.png`, `doc3.pdf`, `doc4.docx`....


### RO:

Utilizand functiile dezvolatate in exercitiu 1 (de mai sus) creaza un program care va lua ca input un path la un folder.

**ATENTIE**: Folositi o mapa pentru test, cu fisiere incluse acolo doar pentru test, nu folositi mape personale sa nu fie afectate fisierele.

Programul va trebui sa redenumeasca toate fisierele in acea mapa in numere (de la 1 la n), ordonate dupa data de create a acelor fisiere.  `os.path.getctime(file_path)` - va intoarce data de creare a fisierului.

Programul nu trebuie sa rescrie extensia fisierului. `fisier.extensie` - De exemplu `document.docx` va trebuie sa fie re-scris ca `1.docx`. 

Adaugati optiunea de a specifica un prefix: De exemplu, prefixul `doc` va redenumi toate fisierele in urmatorul mod  `doc1.docx`, `doc2.png`, `doc3.pdf`, `doc4.docx`....


## Ex3 - Modulul Random  

[Modulul Random](https://docs.python.org/3/library/random.html)

### ENG

Using the Random Module, create a small program that will simulate 2 x 6 sided dice.

The programm should allow the user to roll the dice, and show the values on each dice, and the total sum.

### RO

Utilizand modulul random, creati un program care va simula 2 zaruri cu 6 laturi.

Utilizatorul are optinuea sa arunce zarurile.

Programul va afisa valorile pentru fiecare zar si valoarea totala.


## Ex 4 - Improve Ex 3

### ENG

Improve the exercise above to let the user pick how many sides the Dice has and how many dice there are. 

After the dice are configured, let the user roll the dice until STOP.

### RO

Imbunatatiti exercitiul de mai sus pentru a permite utilizatorului sa aleaga cate laturi va avea zarul si cate zaruri sa arunce. 

Dupa ce zarurile au fost configurate, permiteti utilizatorului sa arunce de un numar indefinit de ori (pan la STOP).