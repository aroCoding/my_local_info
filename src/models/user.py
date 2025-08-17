from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class User:
    """사용자 모델"""
    username: str
    email: Optional[str] = None
    role: str = "user"
    created_at: Optional[datetime] = None
    last_login: Optional[datetime] = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
    
    def to_dict(self):
        """딕셔너리로 변환"""
        return {
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "last_login": self.last_login.isoformat() if self.last_login else None
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """딕셔너리에서 생성"""
        return cls(**data)
