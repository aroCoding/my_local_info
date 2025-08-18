# 지역 정보 시스템

이 프로젝트는 사용자 위치에 기반하여 *지역 특산물, 날씨, 인구 정보*를 제공하는 시스템으로, Python을 기반으로 개발되었습니다.

## 🏗️ 프로젝트 구조

- **src**: 주요 소스 코드가 포함된 디렉토리
  - **components**: 지역 특산물, 인구 정보, 날씨 정보 관련 컴포넌트
  - **models**: 데이터 모델 정의
  - **pages**: 웹 페이지 구성 요소
  - **utils**: 유틸리티 함수 및 데이터 로더
- **data**: JSON 및 JSONC 형식의 지역 정보 데이터
- **tests**: 테스트 코드

## 🚀 실행 방법

1. **의존성 설치**:
   ```bash
   pip install -r requirements.txt
   ```

2. **애플리케이션 실행**:
   ```bash
   python src/main.py
   ```

## 📁 파일 구조

```
my_local_info/
├── assets/
│   └── icons/
├── data/
│   └── region_info.jsonc
├── src/
│   ├── components/
│   │   ├── local_speciality_info.py
│   │   ├── population_info.py
│   │   ├── region_info.py
│   │   └── weather_info.py
│   ├── models/
│   │   ├── population.py
│   │   └── region.py
│   ├── pages/
│   │   └── home.py
│   ├── services/
│   │   ├── get_rank_service.py
│   │   ├── location_weather_service.py
│   │   └── select_region_service.py
│   └── utils/
│   │   └── update_state.py
├── tests/
└── README.md
```

## 🎨 주요 기능
- **지역 정보 제공**: 다양한 지역의 정보 제공
- **날씨 정보 제공**: 현재 위치 기반의 날씨 정보 표시
- **인구 정보 제공**: 지역별 인구 랭킹 및 통계 제공

## 🔧 기술 스택
- **프론트엔드**: Streamlit
- **백엔드**: Python
- **배포**: Streamlit
- **데이터베이스**: JSON

## 🌟 특징
- **지역 선택 시 관련 정보 제공**
- **사용자 맞춤형 정보 제공**

## 배포 링크
https://mylocal.streamlit.app/