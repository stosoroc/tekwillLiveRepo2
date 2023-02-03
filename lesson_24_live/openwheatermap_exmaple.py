from lesson_24_live.find_coord_for_ciry import find_coord_for_city

url = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(position_info: dict):
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
