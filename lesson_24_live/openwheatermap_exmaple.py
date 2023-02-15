def find_coord_for_city(city):
    url = "http://api.openweathermap.org/geo/1.0/direct"
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


def get_weather(position_info: dict):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        **position_info,
        'appid': 'f41891f4e00281944de24eeae3d3efd4',
        'units': 'metric'
    }

    import requests

    response = requests.get(url, params=params)

    print(response.request.url)

    if response.status_code == 200:
        print(response.json())
        data = response.json()
        return dict(
            weather=data['weather'][0]['main'],
            temp=data['main']['temp'],
        )
    else:
        print('Request failed with status', response.status_code)


coord = find_coord_for_city(input('City Name'))
print(get_weather(coord))
