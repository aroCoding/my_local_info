# 상태 업데이트 및 새로고침
import streamlit as st

# 상태 변경을 통한 리렌더링
def refresh_page():
    st.session_state.region = st.session_state.region_selectbox
