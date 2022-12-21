## Ex 1

### RO
Creati un program care va lasa utilizatorul sa introduca orice in input. Apoi programul va trebui sa spuna daca ceia ce a fost introdus poate fi considerat un `int`, `float` sau `string`

Hint: Folositi mai multe `try: except` blocuri pentru a incerca dintai cu `int`, apoi cu `float`, si in final decidem ca tipul este `string`.

### ENG
Create a python program or function that will let the user type anything in a console, and the program should tell the user if what he typed is an integer, a float or a string.

Hint: Try to convert to integer, if that doesn't work, try to convert to float, if that doesn't work, it means that the input is a string.

## Ex 2

### RO

Definiți o funcție numită `plane_ride_cost` care primește ca intrare un string, `city`. 
Funcția ar trebui să returneze un preț diferit în funcție de oraşul-destinaţie al călătoriei. Daca destinatia nu a fost gasita, se va produce o exceptie `InvalidDestinationError`.

Datele pentru preturi sunt urmatoarele, le puteti stoca intr-un dict:

*  "Pittsburgh": 222 euro
*  "Los Angeles": 475 euro
*  "Ohio": 183 euro
*  "Chisinau": 300 euro


### ENG

Define a function named `plane_ride_cost` that will have one argument `city` of type `string`.
The function will have to return the price of the ride to a destination from the dict below. If the destination was not found, the function should result in an `InvalidDestinationException`

Datele pentru preturi sunt urmatoarele, le puteti stoca intr-un dict:

*  "Pittsburgh": 222 euro
*  "Los Angeles": 475 euro
*  "Ohio": 183 euro
*  "Chisinau": 300 euro


## Ex 3

### RO

Adaugati functionalitate exercitiului de mai sus, astefl incat utilizatorul, sa aiba capabilitatea sa introduca destinatii noi.

Programul trebuie sa ruleze continuu si sa aiba urmatoarele functionalitati (folositi un while):

1. Verifica pretul la destinatie.
2. Adauga o destinatie noua.
3. Modifica pretul la o destinatie.
4. Stop (Opereste executarea programului)

Fiecare functionalitate trebuie sa aiba functia sa. Stocarea informatiei se va face intr-un `dict`.

**Incercati sa adaugati functionalitati proprii acestui program, inbunatatindul cum considerati mai bine**. Exemplu: adaugati optiunea de a sterge o destinatie, sau in cazul cand nu exista pret la destinatie, oferiti optiunea de al adauga, etc...

### ENG

Improve the exercise above, adding some more functinality to it by making it possible for the user to add new destinations.

The program should run endlessly (until instructed otherwise): Hint: you can use `while`.

The program should have the following capabilities:

1. Check price for destination
2. Add new destination
3. Change destination price
4. Stop (Program ends here)

Each option should have it's own function. You can store the information in a `dict`.

**Feel free to add your own ideas into this program, and improve it the best you can**. For example: add option to delete a destination, or if a destination does not exist, ask the user to input the price, etc...
