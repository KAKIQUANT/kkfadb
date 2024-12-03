from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from ..factors.base import BaseFactor
import pandas as pd

class FactorStorage(ABC):
    @abstractmethod
    def save_factor(self, factor: BaseFactor) -> None:
        """Save factor definition and metadata"""
        pass

    @abstractmethod
    def load_factor(self, name: str) -> Optional[BaseFactor]:
        """Load factor by name"""
        pass

    @abstractmethod
    def save_factor_data(self, name: str, data: pd.DataFrame) -> None:
        """Save computed factor data"""
        pass

    @abstractmethod
    def load_factor_data(self, name: str, start_date: Optional[str] = None, 
                        end_date: Optional[str] = None) -> pd.DataFrame:
        """Load factor data for given period"""
        pass

    @abstractmethod
    def list_factors(self, category: Optional[str] = None) -> List[str]:
        """List available factors"""
        pass 