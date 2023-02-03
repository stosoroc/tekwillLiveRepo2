import requests

url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"
querystring = {"lat": "47.0105", "lon": "28.8638"}

headers = {
    "X-RapidAPI-Key": "9fc02c456bmsh6626cffb86bc4a3p13dc03jsn476488b50c4e",
    "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
