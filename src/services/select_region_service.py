import json
from models import Region

# JSON 파일 읽기
def getRegionData() -> list[dict]:
    with open('data/region_info.jsonc', 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data

# JSON 데이터에서 'nameKo' 값을 추출하여 리스트로 반환하는 함수
def extract_nameKo_list(json_data):
    return [region['nameKo'] for region in json_data]

def getRegionDescription(region_name: str) -> str:
    region_data = getRegionData()
    for region in region_data:
        if region['nameKo'] == region_name:
            return region['description']
    return ""

# st.session_state.region과 일치하는 지역 찾기
def find_region_by_nameKo(region_name: str, region_data: list[dict]) -> Region:
    for region in region_data:
        if region['nameKo'] == region_name:
            return Region.from_dict(region)
    return None
