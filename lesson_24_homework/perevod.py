import requests
import json

def get_api_key(name):
    with open('apikey.json', 'r') as f:
        keydata = json.load(f)
        for api in keydata:
            if name in api:
                return api[name]['key']

def perevod(text, to_language):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    payload = "target="+to_language+"&q="+text
    
    headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": get_api_key("google-translate"),
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }
    parsed_data = requests.request("POST", url, data=payload, headers=headers)
    parsed_data = json.loads(parsed_data.text)
    return parsed_data["data"]["translations"][0]["translatedText"]


def translate_file(path, to_language):
    with open(path, 'r') as file:
        text = file.read()
    return perevod(text, to_language)

def main():
    print()
    popular_languages = {"Spaniola": "es", 
                          "Germana": "de", 
                         "Franceza": "fr", 
                             "Rusa": "ru", 
                         "Italiana": "it"}

    print("Alege limba dupa numar:")
    for i, language in enumerate(popular_languages.keys()):
        print(f"{i + 1}. {language}")
    selected_language = int(input("Aleg numar: ")) - 1
    language_name = list(popular_languages.keys())[selected_language]
    to_language = popular_languages[language_name]
    print()
    input_type = input("Alege 1 pentru text sau 2 pentru file: ")
    if input_type == '1':
        text = input("Scrie text: ")
        result = perevod(text, to_language)
        print()
        print(f"Traducerea in {language_name}: {result}")
        print()
    elif input_type == '2':
        path = input("Calea spre fisier: ")
        result = translate_file(path, to_language)
        print()
        print(f"Traducerea in {language_name}: {result}")
        print()
    else:
        print()
        print("Alegerea incorecta.")

if __name__ == "__main__":
    main()



#print("Trad: " + perevod())