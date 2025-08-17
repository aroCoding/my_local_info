import altair as alt
import pandas as pd
import streamlit as st

def showPopulationUI():
    st.markdown("##### 인구 랭킹")

    st.warning("""
    🥇 **10대 인구 전국 1위**  
    🥈 **20대 인구 전국 2위**  
    🥉 **100세 이상 전국 3위**
    """)

    data = pd.DataFrame({
        "지역": ["경기도", "서울시", "경상도"],
        "인구수": [90, 100, 50]
    })

    # Altair chart
    chart = (
        alt.Chart(data)
        .mark_bar(
            width=30,  # 막대 너비 줄이기
        )
        .encode(
            x=alt.X("지역", sort=None, axis=alt.Axis(title=None)),   # 카테고리 순서대로
            y=alt.Y("인구수", scale=alt.Scale(domain=[0, 100]), axis=alt.Axis(title=None, tickMinStep=10)),  # tickMinStep을 20으로 늘려 세로 눈금 간격 늘림
            tooltip=["지역", "인구수"],
            color=alt.condition(
                alt.datum.지역 == "서울시", 
                alt.value('#FF0000'),  # 서울시는 빨간색
                alt.value('#2E86C1')   # 나머지는 파란색
            )
        )
        .properties(height=220)  # 차트 높이를 250px로 제한
    )

    # Add text labels above bars
    text = chart.mark_text(
        align='center',
        baseline='bottom',
        dy=-5  # Adjust position above the bar
    ).encode(
        text='인구수:Q'
    )

    st.altair_chart(chart + text, use_container_width=True)
