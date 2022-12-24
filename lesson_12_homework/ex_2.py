def palindrom(string):
    return string == string[::-1]


def palindrom_checker():
    input_text = 'Introdu un cuvant pentru verificare sau stop:'
    text = input(input_text)
    while text != 'stop':
        if palindrom(text):
            print('Este palindrom')
        else:
            print("Nu este palindrom")
        text = input(input_text)


if __name__ == '__main__': # Pentru executarea codului
    palindrom_checker()
