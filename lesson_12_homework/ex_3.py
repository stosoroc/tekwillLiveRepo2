def is_prime(number: int):
    for a in range(2, number):
        if number % a == 0:
            return False
    return True


if __name__ == '__main__': # Pentru executarea codului
    var = int(input('Numarul pentru verificare'))
    print(is_prime(var))
