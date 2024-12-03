from typing import Optional, Dict, Any
import pandas as pd
import numpy as np
from scipy import stats

class FactorValidator:
    @staticmethod
    def check_coverage(data: pd.Series, min_coverage: float = 0.8) -> bool:
        """Check if factor has sufficient data coverage"""
        return data.notna().mean() >= min_coverage

    @staticmethod
    def check_normality(data: pd.Series) -> Dict[str, float]:
        """Test factor distribution for normality"""
        clean_data = data.dropna()
        statistic, pvalue = stats.normaltest(clean_data)
        return {
            "statistic": statistic,
            "pvalue": pvalue
        }

    @staticmethod
    def check_autocorrelation(data: pd.Series, lag: int = 1) -> float:
        """Check factor autocorrelation"""
        clean_data = data.dropna()
        return pd.Series(clean_data).autocorr(lag=lag)

    @staticmethod
    def compute_ic(factor: pd.Series, returns: pd.Series) -> Dict[str, float]:
        """Compute Information Coefficient statistics"""
        clean_data = pd.DataFrame({
            'factor': factor,
            'returns': returns
        }).dropna()
        
        ic = clean_data['factor'].corr(clean_data['returns'])
        ic_t_stat = ic * np.sqrt(len(clean_data) - 2) / np.sqrt(1 - ic**2)
        
        return {
            "ic": ic,
            "t_stat": ic_t_stat,
            "p_value": 2 * (1 - stats.t.cdf(abs(ic_t_stat), len(clean_data)-2))
        } 