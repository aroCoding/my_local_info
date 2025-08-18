import requests

def getCoordinatesByCityName(city_name: str) -> tuple[float, float]:
    """
    도시 이름을 입력받아 좌표값을 반환합니다.
    """
    apiKey = "5d5261f59b3c727e66ea6bf7ab5ce1aa"

    if city_name == "경기도":
        city_name = "경기"
    elif city_name == "강원특별자치도":
        city_name = "강원"
    elif city_name == "제주특별자치도":
        city_name = "제주"

    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={apiKey}"
    
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()

    if city_name == "충청북도":
        return 36.737510, 126.790341
    elif city_name == "충청남도":
        return 36.722304, 126.798624
    elif city_name == "전북특별자치도":
        return 35.718258, 127.153027
    elif city_name == "전라남도":
        return 34.869448, 126.990737
    elif city_name == "경상북도":
        return 36.321854, 128.893088
    elif city_name == "경상남도":
        return 35.532870, 128.188550

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