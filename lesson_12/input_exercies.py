

def input_getter(intrebarea, ori):
    lista_de_respunsuri = []
    for i in range(ori):
        lista_de_respunsuri.append(input(intrebarea))
    return lista_de_respunsuri    

def number_input_getter(intrebarea, ori):
    lista_de_respunsuri = []
    for i in range(ori):
        lista_de_respunsuri.append(int(input(intrebarea)))
    return lista_de_respunsuri    

def smart_number_input_getter(intrebarea, ori):
    lista_de_respunsuri = []
    n = 0
    while n < ori:
        potential_number = input(intrebarea)
        if not potential_number.isnumeric(): 
            print('Vreau numar intreg nu altceva')
            continue
        lista_de_respunsuri.append(int(potential_number))
        n += 1
    return lista_de_respunsuri

# # print(input_getter('Da-mi un numar: ', 5))
# result = number_input_getter('Un numar te rog: ', 3)
# print(result)

# result = smart_number_input_getter('Un numar intreg:', 5)

# print(result)

# smart_number_input_getter(ori=5, intrebarea='Da-mi un numar') #Valid
# smart_number_input_getter('Da-mi un numar', ori=4) # Valid
# smart_number_input_getter('Intrebarea', ori=10) # Valid
# smart_number_input_getter(10, 'Da-mi un numar') # Invalid
# smart_number_input_getter(10, intrebarea='Da-mi un numar') # Invalid

def custom_multiple_input(prompts: list, number_of_times: int = 1):
    responses = []
    for a in range(number_of_times):
        response = dict()
        for prompt in prompts:
            response[prompt] = input(prompt.capitalize())
        responses.append(response)
    return responses
    
    
# list_of_usesr = custom_multiple_input(['name', 'age', 'sex'], 5)
# print(list_of_usesr)