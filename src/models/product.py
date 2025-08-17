from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class Product:
    """상품 모델"""
    uuid: str
    name: str
    description: Optional[str] = None
    category: str = "food_agriculture"
    location_code: str = ""
    images: List[str] = None
    thumbnail: str = ""
    video_url: str = ""
    lang: str = "ko"
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    
    def __post_init__(self):
        if self.images is None:
            self.images = []
        if self.created_at is None:
            self.created_at = datetime.now()
        if self.updated_at is None:
            self.updated_at = datetime.now()
    
    def to_dict(self):
        """딕셔너리로 변환"""
        return {
            "uuid": self.uuid,
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "location_code": self.location_code,
            "images": self.images,
            "thumbnail": self.thumbnail,
            "video_url": self.video_url,
            "lang": self.lang,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """딕셔너리에서 생성"""
        return cls(**data)
