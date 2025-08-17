import streamlit as st

def showLocalSpecialityInfoUI():

    # 지역특산물 json 데이터 가져오기

    # 지역특산물 데이터 파싱

    # 지역특산물 데이터 표시
    st.markdown("##### 지역 특산물")
    
    # 3개 특산물을 컬럼으로 배치
    spec_col1, spec_col2, spec_col3 = st.columns(3)
    
    with spec_col1:
        st.image("https://picsum.photos/100/100", width=100, use_container_width=False)
        st.caption("기장미역")
    
    with spec_col2:
        st.image("https://picsum.photos/100/100", width=100, use_container_width=False)
        st.caption("곰장어")
    
    with spec_col3:
        st.image("https://picsum.photos/100/100", width=100, use_container_width=False)
        st.caption("철마당근")