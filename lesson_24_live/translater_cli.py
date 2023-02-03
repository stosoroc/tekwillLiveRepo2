import requests


def transalte(text):
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    payload = {'q': text, 'target': 'ro', 'source': 'en'}
    headers = {
        "X-RapidAPI-Key": "9fc02c456bmsh6626cffb86bc4a3p13dc03jsn476488b50c4e",
        "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    # print(response.text)
    json_data = response.json()
    print(json_data['data']['translations'][0]['translatedText'])


while True:
    transalte(input('Text in any language:'))
