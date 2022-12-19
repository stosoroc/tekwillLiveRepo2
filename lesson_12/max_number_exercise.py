

# max_number(1, 2) Va produce eroare, deoarece inca nu am definit functia

def max_number(a, b):
    if a > b:
        print(a)
    else:
        print(b)

result_1 = max_number(10, 15)
result_2 = max_number(30, 10)

print(result_1, result_2)

print(max(1, 20))
