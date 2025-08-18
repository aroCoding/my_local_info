import altair as alt
import pandas as pd
import streamlit as st
from models import Region
from services import get_rank

def showPopulationUI(region_info: Region):
    region_name = region_info.nameKo
    region_population = region_info.population.total
    region_age_groups = region_info.population.age_groups
    region_rank = region_info.population.rank

    # 총인구 랭크 1~3위 추출
    total_rank = get_rank(region_rank['total'])
    teens_rank = get_rank(region_rank['teens'])
    twenties_rank = get_rank(region_rank['twenties'])
    thirties_rank = get_rank(region_rank['thirties'])
    forties_rank = get_rank(region_rank['forties'])
    fifties_plus_rank = get_rank(region_rank['fifties_plus'])
    centenarians_rank = get_rank(region_rank['centenarians'])

    st.markdown("##### 인구 랭킹")

    # 총인구 순위 표시
    showTotalRankUI(total_rank)
    showAgeGroupRankUI(teens_rank, "teens")
    showAgeGroupRankUI(twenties_rank, "twenties")
    showAgeGroupRankUI(thirties_rank, "thirties")
    showAgeGroupRankUI(forties_rank, "forties")
    showAgeGroupRankUI(fifties_plus_rank, "fifties_plus")
    showAgeGroupRankUI(centenarians_rank, "centenarians")

    # 위젯 사이 공간
    st.container(height=50, border=False)


    default_regions = ["경기도", "서울특별시", "부산광역시"]
    default_populations = [13_715_016, 9_323_492, 3_251_625]

    if region_name != "서울특별시" and region_name != "부산광역시" and region_name != "경기도":
        default_regions.insert(0, region_name)
        default_populations.insert(0, region_population)
    
    print(default_regions)
    print(default_populations)

    data = pd.DataFrame({
        "지역": default_regions,
        "인구수": default_populations
    })

    # Altair chart
    chart = (
        alt.Chart(data)
        .mark_bar(
            width=30,  # 막대 너비 줄이기
        )
        .encode(
            x=alt.X("지역", sort=None, axis=alt.Axis(title=None)),   # x축 제목 제거
            y=alt.Y("인구수", scale=alt.Scale(domain=[0, 15_000_000]), axis=alt.Axis(title=None, labels=False, tickMinStep=500_000)),  # y축 제목 제거 및 눈금 숫자 숨기기
            tooltip=["지역", "인구수"],
            color=alt.condition(
                alt.datum.지역 == region_name, 
                alt.value('#FF7E5F'),
                alt.value('#85E5B0') 
            )
        )
        .properties(height=350, title=alt.TitleParams(text="지역별 전체 인구수(만명)", align='center', anchor='middle', dy=-10))  # y축 단위 (만명)을 위쪽에 추가
    )

    # Add text labels above bars
    text = chart.mark_text(
        align='center',
        baseline='bottom',
        dy=-5  # Adjust position above the bar
    ).encode(
        text=alt.Text('인구수:Q', format=',')  # 인구수를 천 단위로 콤마 표시
    )

    st.altair_chart(chart + text, use_container_width=True)


def showTotalRankUI(total_rank: int):
    if total_rank == 1:
        st.badge("전국 인구 1위", icon="🥇", color="orange")
    elif total_rank == 2:
        st.badge("전국 인구 2위", icon="🥈", color="grey")
    elif total_rank == 3:
        st.badge("전국 인구 3위", icon="🥉", color="green")
    else:
        pass

def showAgeGroupRankUI(age_group_rank: int, age_group_name: str):
    if age_group_name == "teens":
        st.badge("전국 10대 인구 1위", icon="🥇", color="orange") if age_group_rank == 1 else st.badge("전국 10대 인구 2위", icon="🥈", color="grey") if age_group_rank == 2 else st.badge("전국 10대 인구 3위", icon="🥉", color="green") if age_group_rank == 3 else None
    elif age_group_name == "twenties":
        st.badge("전국 20대 인구 1위", icon="🥇", color="orange") if age_group_rank == 1 else st.badge("전국 20대 인구 2위", icon="🥈", color="grey") if age_group_rank == 2 else st.badge("전국 20대 인구 3위", icon="🥉", color="green") if age_group_rank == 3 else None
    elif age_group_name == "thirties":
        st.badge("전국 30대 인구 1위", icon="🥇", color="orange") if age_group_rank == 1 else st.badge("전국 30대 인구 2위", icon="🥈", color="grey") if age_group_rank == 2 else st.badge("전국 30대 인구 3위", icon="🥉", color="green") if age_group_rank == 3 else None
    elif age_group_name == "forties":
        st.badge("전국 40대 인구 1위", icon="🥇", color="orange") if age_group_rank == 1 else st.badge("전국 40대 인구 2위", icon="🥈", color="grey") if age_group_rank == 2 else st.badge("전국 40대 인구 3위", icon="🥉", color="green") if age_group_rank == 3 else None
    elif age_group_name == "fifties_plus":
        st.badge("전국 50대 이상 인구 1위", icon="🥇", color="orange") if age_group_rank == 1 else st.badge("전국 50대 이상 인구 2위", icon="🥈", color="grey") if age_group_rank == 2 else st.badge("전국 50대 이상 인구 3위", icon="🥉", color="green") if age_group_rank == 3 else None
    elif age_group_name == "centenarians":
        st.badge("전국 100세 이상 인구 1위", icon="🥇", color="orange") if age_group_rank == 1 else st.badge("전국 100세 이상 인구 2위", icon="🥈", color="grey") if age_group_rank == 2 else st.badge("전국 100세 이상 인구 3위", icon="🥉", color="green") if age_group_rank == 3 else None
    else:
        None

