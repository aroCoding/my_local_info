from re import S
import streamlit as st
from components import weatherInfoUI
from components import showRegionInfoUI
from components import showPopulationUI
from services import extract_nameKo_list, getRegionData
from utils import refresh_page
from services import find_region_by_nameKo

st.set_page_config(page_title="홈 - 지역 특산물", page_icon="🏠")

region_data = getRegionData()
region_list = extract_nameKo_list(region_data)



def show_home():
    with st.container(border=True):
        col1, col2 = st.columns([0.75, 0.25], vertical_alignment="center")
        with col1:
            st.subheader(f"현재 당신의 지역은 {st.session_state.region} 입니다")
        with col2:
            st.session_state.region = st.selectbox("지역 변경", region_list, index=0, key="region_selectbox", help="지역변경", on_change=refresh_page)
            # update_region()
    col1, col2 = st.columns(2, border=True)
    with col1:
        weatherInfoUI(st.session_state.region)
        
        showRegionInfoUI(st.session_state.region)
    
    with col2:
        regionInfo = find_region_by_nameKo(st.session_state.region, region_data)
        showPopulationUI(regionInfo)
        
        # showLocalSpecialityInfoUI()

