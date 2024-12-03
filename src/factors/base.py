from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Any, Optional, List
import pandas as pd
import numpy as np

class BaseFactor(ABC):
    """Base class for all factors"""
    
    def __init__(
        self,
        name: str,
        description: str,
        category: str,
        version: str = "1.0.0",
        metadata: Optional[Dict[str, Any]] = None
    ):
        self.name = name
        self.description = description
        self.category = category
        self.version = version
        self.metadata = metadata or {}
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @abstractmethod
    def compute(self, data: pd.DataFrame) -> pd.Series:
        """Compute factor values from input data"""
        pass

    def validate(self, data: pd.Series) -> bool:
        """Validate factor computation results"""
        if data.isnull().all():
            return False
        if np.isinf(data).any():
            return False
        return True

    def to_dict(self) -> Dict[str, Any]:
        """Convert factor to dictionary representation"""
        return {
            "name": self.name,
            "description": self.description,
            "category": self.category,
            "version": self.version,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BaseFactor':
        """Create factor instance from dictionary"""
        factor = cls(
            name=data["name"],
            description=data["description"],
            category=data["category"],
            version=data.get("version", "1.0.0"),
            metadata=data.get("metadata", {})
        )
        factor.created_at = datetime.fromisoformat(data["created_at"])
        factor.updated_at = datetime.fromisoformat(data["updated_at"])
        return factor 