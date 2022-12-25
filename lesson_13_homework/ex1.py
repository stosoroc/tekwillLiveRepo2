# Creati un program care va lasa utilizatorul sa introduca orice in input. 
# Apoi programul va trebui sa spuna daca ceia ce a fost introdus 
# poate fi considerat un `int`, `float` sau `string`

# Hint: Folositi mai multe `try: except` blocuri pentru a incerca dintai 
# cu `int`, apoi cu `float`, si in final decidem ca tipul este `string`.
print()
orice = input("Scrie ceva: ")

try:
    or1 = int(orice)    
    print(type(or1))
except ValueError:
    try:
        or1 = float(orice)    
        print(type(or1))
    except ValueError:
        or1 = str(orice)    
        print(type(or1))
    except Exception:
        print("Tip nedefinit")