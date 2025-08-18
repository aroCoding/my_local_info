import streamlit as st
from services import getRegionDescription

def showRegionInfoUI(region_name: str):

    # 지역 조회
    # json 파일 읽기
    region_description = getRegionDescription(region_name)


    # 지역정보 표시
    st.markdown("##### 지역 정보")
    st.success(region_description)