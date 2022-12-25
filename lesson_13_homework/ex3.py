# Adaugati functionalitate exercitiului de mai sus, astefl incat utilizatorul, 
# sa aiba capabilitatea sa introduca destinatii noi.

# Programul trebuie sa ruleze continuu si sa aiba urmatoarele functionalitati (folositi un while):

# 1. Verifica pretul la destinatie.
# 2. Adauga o destinatie noua.
# 3. Modifica pretul la o destinatie.
# 4. Stop (Opereste executarea programului)

# Fiecare functionalitate trebuie sa aiba functia sa. Stocarea informatiei se va face intr-un `dict`.

# **Incercati sa adaugati functionalitati proprii acestui program, inbunatatindul cum considerati mai bine**. 
# Exemplu: adaugati optiunea de a sterge o destinatie, sau in cazul cand nu exista pret la destinatie, 
# oferiti optiunea de al adauga, etc...

dict_city = {
    "Pittsburgh": 222,
    "Los Angeles": 475,
    "Ohio": 183,
    "Chisinau": 300
}

class InvalidDestinationError(Exception):
    pass

def plane_ride_cost(city):
    if city not in dict_city:
        raise InvalidDestinationError(f'Oras {city} nu avem in lista')
    return dict_city[city]

def lista_preturi():
    for i, (oras, pret) in enumerate(dict_city.items()):
        print(f"{i+1}. {oras}: {pret} euro")
    print()
   
def sterge_oras():
    print()
    print("Stergem oras, stop pentru a opri")
    city = cere_oras()
    if city == 'stop':
        print("Stop: sterge oras")
        return city
    # print(city)
    # print(type(city))
    dict_city.pop(city) 
    print()
    print("Lista modificata")
    lista_preturi()

def schimba_pretul():
    print()
    print("Schimbam pret la oras, stop pentru a opri")
    city = cere_oras()
    if city == 'stop':
        print("Stop: schimba pret")
        return city
    pret_nou = cere_pret()
    dict_city[city] = pret_nou
    print()
    print("Lista cu preturi noi")
    lista_preturi()
    
def oras_nou():
    print()
    print("Adaugam oras, stop pentru a opri")
    city = input("Oras nou: ")
    if city in dict_city:
        while True:
            city = input(f"{city} deja avem in lista, alt oras: ")
            if city not in dict_city:
                break
    if city == 'stop':
        print("Stop: oras nou")
        return city
    pret = cere_pret()
    dict_city[city] = pret
    print("Lista cu oras nou")
    lista_preturi()
    
def cere_oras():
    oras = input("Care oras: ")
    if oras == 'stop':
        return(oras)
    if oras not in dict_city:
        while True:
            oras = input(f"{oras} nu este in lista, alt oras: ")
            if oras in dict_city:
                break
    #print(type(oras))
    return(oras)

def cere_pret():
    while True:
            try:
                pret_nou = int(input("Introducetin numar intreg la pret nou: "))
                break
            except ValueError:
                print("Numar introdus nu este intreg!")
    return(pret_nou)


print()
executarea = "" #variabila care ne ajuta sa iesim din subprogram si din while principal o data
while True:
    if executarea == 'stop':
        break

    print(" 1. Toata lista.")
    print(" 2. Verifica pretul la destinatie.")
    print(" 3. Adauga o destinatie noua.")
    print(" 4. Modifica pretul la o destinatie.")
    print(" 5. Sterge o destinatie.")
    print(" 0. stop - Opereste executarea programului.")
    optiune = input("Numar din lista: ")
    if optiune == '0' or optiune == 'stop':
        break
        
    # 1. Toata lista.
    if optiune == '1':
        print()
        lista_preturi()

    # 2. Verifica pretul la destinatie.
    if optiune == '2':
        print()
        oras = cere_oras()
        pret = plane_ride_cost(oras)
        print(f"Pretul calatorieri in oras {oras}, este de {pret} euro")
        print()

    # 3. Adauga o destinatie noua.
    if optiune == '3':
        executarea = oras_nou()

    # 4. Modifica pretul la o destinatie.
    if optiune == '4':
        executarea = schimba_pretul()
    
    # 5. Sterge o destinatie.
    if optiune == '5':
        executarea = sterge_oras()

    
