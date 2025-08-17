import requests

def getCoordinatesByCityName(city_name: str) -> tuple[float, float]:
    """
    도시 이름을 입력받아 좌표값을 반환합니다.
    """
    apiKey = "5d5261f59b3c727e66ea6bf7ab5ce1aa"

    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={apiKey}"
    response = requests.get(url)
    data = response.json()

    # print(data)
    return data[0]["lat"], data[0]["lon"]


def getWeatherByCoordinates(coordinates: tuple[float, float]) -> dict:
    """
    좌표값을 입력받아 날씨 정보를 반환합니다.
    """
    apiKey = "5d5261f59b3c727e66ea6bf7ab5ce1aa"

    lat, lon = coordinates if coordinates else (None, None)

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apiKey}&lang=kr&units=metric"
    response = requests.get(url)
    data = response.json()

    currentWeather = {}

    currentWeather['main'] = data["weather"][0]["main"]
    currentWeather['description'] = data["weather"][0]["description"]
    currentWeather['temp'] = data['main']['temp']
    currentWeather['clouds'] = data['clouds']['all']

    return currentWeather

def getWeatherIconPath(currentWeatherInfo: dict) -> str:
    """
    날씨 정보를 기반으로 적절한 아이콘을 화면에 표시합니다.
    """
    icon_map = {
        'thunderstorm': 'thunderstorm.png',
        'drizzle': 'drizzle.png',
        'rain': 'rain.png',
        'snow': 'snow.png',
        'clear': 'clear_sky.png',
        'clouds': 'broken_clouds.png',
        'mist': 'mist.png',
    }

    weather_main = currentWeatherInfo.get('main', '').lower()
    clouds_percentage = currentWeatherInfo.get('clouds', 0)

    icon_file_name = ''

    if weather_main == 'clouds':
        if 0 <= clouds_percentage <= 25:
            icon_file_name = 'few_clouds.png'
        elif 26 <= clouds_percentage <= 50:
            icon_file_name = 'scattered_clouds.png'
        else:
            icon_file_name = 'broken_clouds.png'

    icon_file_name = icon_map.get(weather_main, 'clear_sky.png')    

    return f"assets/icons/{icon_file_name}"