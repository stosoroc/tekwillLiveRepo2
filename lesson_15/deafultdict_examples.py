from collections import defaultdict

lista_generala = ['apa', 'paine', 'ciocolata', 'carne', 'lapte', 'cascaval']

comanda_1 = [('apa', 10), ('paine', 20)]
comanda_2 = [('ciocolata', 10), ('carne', 20)]
comanda_3 = [('paine', 10), ('paine', 20)]
comanda_4 = [('apa', 10), ('ciocolata', 20)]

lista_de_comanda = defaultdict(Decimal)

for produs, cantitate in comanda_4 + comanda_3 + comanda_2 + comanda_1:
    lista_de_comanda[produs] += cantitate

print(lista_de_comanda)
