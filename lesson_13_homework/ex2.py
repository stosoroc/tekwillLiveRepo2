# Definiți o funcție numită `plane_ride_cost` care primește 
# ca intrare un string, `city`. 
# Funcția ar trebui să returneze un preț diferit în funcție 
# de oraşul-destinaţie al călătoriei. Daca destinatia nu a fost gasita, 
# se va produce o exceptie `InvalidDestinationError`.

# Datele pentru preturi sunt urmatoarele, le puteti stoca intr-un dict:

# *  "Pittsburgh": 222 euro
# *  "Los Angeles": 475 euro
# *  "Ohio": 183 euro
# *  "Chisinau": 300 euro

class InvalidDestinationError(Exception):
    pass

def plane_ride_cost(city):
    if city not in dict_city:
        raise InvalidDestinationError(f'Oras {city} nu avem in lista')
    return dict_city[city]
        
dict_city = {
    "Pittsburgh": 222,
    "Los Angeles": 475,
    "Ohio": 183,
    "Chisinau": 300
}

#ver1
#print(plane_ride_cost(input("In care oras: ")), "euro")

#ver2
print()
oras = input("In care oras: ")
pret = plane_ride_cost(oras)
if pret:
    print(f"Pretul calatorieri in oras {oras}, este de {pret} euro")
print()