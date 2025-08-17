from dataclasses import dataclass

from .population import Population

@dataclass
class Region:
    """지역 모델"""
    nameEn: str
    nameKo: str
    nameJa: str
    code: str
    population: Population

    def to_dict(self):
        return {
            "nameEn": self.nameEn,
            "nameKo": self.nameKo,
            "nameJa": self.nameJa,
            "code": self.code,
            "population": self.population.to_dict()
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            nameEn=data['nameEn'],
            nameKo=data['nameKo'],
            nameJa=data['nameJa'],
            code=data['code'],
            population=Population.from_dict(data['population'])
        )

