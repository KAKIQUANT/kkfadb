from ..base import BaseFactor
import pandas as pd
import numpy as np

class MomentumFactor(BaseFactor):
    def __init__(self, lookback_period: int = 20):
        super().__init__(
            name=f"momentum_{lookback_period}",
            description=f"{lookback_period}-day price momentum",
            category="technical",
            metadata={"lookback_period": lookback_period}
        )
        self.lookback_period = lookback_period

    def compute(self, data: pd.DataFrame) -> pd.Series:
        """Compute momentum factor
        
        Args:
            data: DataFrame with 'close' price column
        Returns:
            Series of momentum values
        """
        return data['close'].pct_change(self.lookback_period)

class VolumePriceFactor(BaseFactor):
    def __init__(self, window: int = 20):
        super().__init__(
            name=f"volume_price_{window}",
            description=f"{window}-day volume-price correlation",
            category="technical",
            metadata={"window": window}
        )
        self.window = window

    def compute(self, data: pd.DataFrame) -> pd.Series:
        """Compute volume-price correlation
        
        Args:
            data: DataFrame with 'close' and 'volume' columns
        Returns:
            Series of correlation values
        """
        price_ret = data['close'].pct_change()
        volume_ret = data['volume'].pct_change()
        return price_ret.rolling(self.window).corr(volume_ret) 