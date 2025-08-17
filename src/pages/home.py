import streamlit as st
import pandas as pd
import altair as alt
from components import weatherInfoUI
from components import showRegionInfoUI
from components import showPopulationUI
from components import showLocalSpecialityInfoUI

st.set_page_config(page_title="홈 - 지역 특산물", page_icon="🏠")

region = "seoul"

def show_home():
    with st.container(border=True):
        col1, col2 = st.columns([0.75, 0.25], vertical_alignment="center")
        with col1:
            st.subheader(f"현재 당신의 지역은 {region} 입니다")
        with col2:
            st.selectbox("지역 변경", ["seoul", "busan", "daegu"], index=1, key="region_selectbox", help="지역변경")
    col1, col2 = st.columns(2, border=True)
    with col1:
        weatherInfoUI(region)
        
        showRegionInfoUI()
    
    with col2:
        showPopulationUI()
        
        showLocalSpecialityInfoUI()

