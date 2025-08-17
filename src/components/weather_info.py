import streamlit as st

def weatherInfoUI():

    # Weather API 호출

    # Weather API 응답 파싱

    # 현재 날씨 정보 표시
    st.markdown("##### 현재 날씨")
    st.info("""
    **22°C**  
    맑음 • 습도 65% • 바람 3m/s
    """)


def get_current_location() -> tuple[float, float]:
    """현재 위치 정보(좌표값) 가져오기"""
    pass