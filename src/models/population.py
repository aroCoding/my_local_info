from dataclasses import dataclass
from typing import Dict

@dataclass
class Population:
    """인구 모델"""
    total: int
    age_groups: Dict[str, int]
    rank: Dict[str, int]

    def to_dict(self):
        return {
            "total": self.total,
            "age_groups": self.age_groups,
            "rank": self.rank
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            total=data['total'],
            age_groups=data['age_groups'],
            rank=data['rank']
        )