import json

# JSON 데이터에서 'nameKo' 값을 추출하여 리스트로 반환하는 함수
def extract_nameKo_list(json_data):
    return [region['nameKo'] for region in json_data]

# JSON 파일 읽기

def getRegionData() -> list[dict]:
    with open('data/region_info.jsonc', 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data