
import pytest
from src.services.location_weather_service import getCoordinatesByCityName
from src.services.location_weather_service import getWeatherByCoordinates
from src.services.location_weather_service import getWeatherIconPath
from src.models.region import Region
from src.models.population import Population
from src.services.select_region_service import getRegionData

def test_getCoordinatesByCityName():
    lat, lon = getCoordinatesByCityName("Seoul")
    weatherInfo = getWeatherByCoordinates((lat, lon))

    assert lat == 37.5666791
    assert lon == 126.9782914

    iconPath = getWeatherIconPath(weatherInfo)

    print(iconPath)
    assert iconPath == "assets/icons/broken_clouds.png"


    
def test_population_model():
    json_data = {
        "total": 9323492,
        "age_groups": {
            "teens": 721320,
            "twenties": 1283295,
            "thirties": 1453915,
            "forties": 1370576,
            "fifties_plus": 4025570,
            "centenarians": 1483
        },
        "rank": {
            "total": 1,
            "teens": 1,
            "twenties": 1,
            "thirties": 1,
            "forties": 1,
            "fifties_plus": 1,
            "centenarians": 1
        }
    }

    population = Population.from_dict(json_data)

    assert population.total == 9323492
    assert population.age_groups['teens'] == 721320
    assert population.age_groups['twenties'] == 1283295
    assert population.age_groups['thirties'] == 1453915
    assert population.age_groups['forties'] == 1370576
    assert population.age_groups['fifties_plus'] == 4025570
    assert population.age_groups['centenarians'] == 1483
    assert population.rank['total'] == 1
    assert population.rank['teens'] == 1
    assert population.rank['twenties'] == 1
    assert population.rank['thirties'] == 1

def test_region_model():
    json_data = {
        "level": "province",
        "nameEn": "Seoul",
        "nameKo": "서울특별시",
        "nameJa": "ソウル",
        "code": "KR-11",
        "population": {
            "total": 9323492,
            "age_groups": {
                "teens": 721320,
                "twenties": 1283295,
                "thirties": 1453915,
                "forties": 1370576,
                "fifties_plus": 4025570,
                "centenarians": 1483
            },
            "rank": {
                "total": 1,
                "teens": 1,
                "twenties": 1,
                "thirties": 1,
                "forties": 1,
                "fifties_plus": 1,
                "centenarians": 1
            }
        }
    }

    region = Region.from_dict(json_data)

    assert region.nameEn == "Seoul"
    assert region.nameKo == "서울특별시"
    assert region.nameJa == "ソウル"
    assert region.code == "KR-11"
    assert region.population.total == 9323492
    assert region.population.age_groups['teens'] == 721320
    assert region.population.age_groups['twenties'] == 1283295


def get_region_name_list():
    region_data = getRegionData()
    region_name_list = [region['nameKo'] for region in region_data]

    assert region_name_list is type(list)
    assert region_name_list[0] == "서울특별시"
    assert region_name_list[1] == "부산광역시"
    assert region_name_list[2] == "대구광역시"
    assert region_name_list[3] == "인천광역시"
    assert region_name_list[4] == "광주광역시"
    assert region_name_list[5] == "대전광역시"
    assert region_name_list[6] == "울산광역시"
    assert region_name_list[7] == "세종특별자치시"
    assert region_name_list[8] == "경기도"