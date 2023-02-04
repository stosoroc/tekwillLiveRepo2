url = "http://api.openweathermap.org/geo/1.0/direct"


def find_coord_for_city(city):
    params = {
        'q': city,
        'appid': 'f41891f4e00281944de24eeae3d3efd4',
    }

    import requests

    response = requests.get(url, params=params)

    if response.status_code == 200:
        print(response.json())
        return dict(lat=response.json()[0]['lat'], lon=response.json()[0]['lon'])
    else:
        print('Request failed with status', response.status_code)
        return None
