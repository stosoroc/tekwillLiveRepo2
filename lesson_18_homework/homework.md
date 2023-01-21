# Homework

## Ex 1

Write a Python program to find palindromes in a given list of strings using Lambda. Orginal list of strings:
`['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']`
List of palindromes:
`['php', 'aaa']`.

Note: You can use the `filter` function in python to filer a list using a function.

### RO

Creati un program python cu ajutorul careia vor fi gasite toate elementele dintr-o lista de string-uri care sunt
palindroame. Avand lista `['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']`
rezultatul va fi `['php', 'aaa']`.

Note: Puteti folosi functia `filter` pentru a filtra elementele unei colectii.

## Ex 2

Create a decorator that checks if the result of the function it decorates is always a number

The decorator should be called "validate_numeric" and should raise ValueError when the result of function it decorates
is not numeric.

### RO

Creati un decorator care verifica daca valoare returnata de functia care o decoreaza mereu e un numar.

Functia trebuie sa fie numita `validate_numeric` si va produce `ValueError` cand functia nu intoarce valoare numerica.

## Ex 3

Create a decorator that will count the time that it took for a function to complete.

The decorator should be called `benchmark_time` and should show at the end of every function call of the function that
it decorates, the ammount in seconds of the time it took to complete.

Bonus points if you can also print the name of the function being called (decorated).

### RO

Creati un decorator numit `benchmark_time` care va calcula timpul executiei fiecarei functii care o decoreaza.

Decoratorul va afisa la consola in secunde timpul in care a fost executat functia care este decorata.

Bonus points daca gasiti o metoda de a afisa si numele functiei care a fost executata.
