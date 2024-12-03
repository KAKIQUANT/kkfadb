from typing import Dict, List, Optional, Type
from .base import BaseFactor
from datetime import datetime
import json

class FactorRegistry:
    """Registry for managing and storing factors"""
    
    def __init__(self):
        self.factors: Dict[str, BaseFactor] = {}
        
    def register(self, factor: BaseFactor) -> None:
        """Register a new factor"""
        if factor.name in self.factors:
            raise ValueError(f"Factor {factor.name} already exists")
        self.factors[factor.name] = factor
        
    def get_factor(self, name: str) -> Optional[BaseFactor]:
        """Retrieve a factor by name"""
        return self.factors.get(name)
        
    def list_factors(self, category: Optional[str] = None) -> List[str]:
        """List all registered factors, optionally filtered by category"""
        if category:
            return [name for name, factor in self.factors.items() 
                   if factor.category == category]
        return list(self.factors.keys())
        
    def remove_factor(self, name: str) -> None:
        """Remove a factor from the registry"""
        if name in self.factors:
            del self.factors[name]
            
    def export_factors(self, filepath: str) -> None:
        """Export factors to JSON file"""
        data = {name: factor.to_dict() for name, factor in self.factors.items()}
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
            
    def import_factors(self, filepath: str) -> None:
        """Import factors from JSON file"""
        with open(filepath, 'r') as f:
            data = json.load(f)
        for name, factor_data in data.items():
            self.factors[name] = BaseFactor.from_dict(factor_data) 