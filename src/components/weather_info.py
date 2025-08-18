import streamlit as st
import time
from services import getCoordinatesByCityName, getWeatherByCoordinates, getWeatherIconPath

def weatherInfoUI(city_name: str):

    # Weather API 호출
    # Weather API 응답 파싱
    lat, lon = getCoordinatesByCityName(city_name)

    if lat or lon is Exception:
        with st.spinner("Wait for it...", show_time=True):
            time.sleep(2)
        return st.error("날씨 정보를 가져오는데 실패했습니다.")

    weatherInfo = getWeatherByCoordinates((lat, lon))
    iconPath = getWeatherIconPath(weatherInfo)





    # 현재 날씨 정보 표시
    col1, col2 = st.columns([0.3, 0.7], vertical_alignment="center")
    with col1:
        st.image(iconPath, width=100)
    with col2:
        st.markdown("현재 날씨는 **{}** 이며,  \n현재 온도는 :red[**{}°C**] 입니다".format(weatherInfo['description'], weatherInfo['temp']))


def get_current_location() -> tuple[float, float]:
    """현재 위치 정보(좌표값) 가져오기"""
    pass