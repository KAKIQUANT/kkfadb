import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Optional

class FactorVisualizer:
    """Visualization tools for factor analysis"""
    
    @staticmethod
    def plot_factor_returns(
        factor_data: pd.Series,
        title: Optional[str] = None,
        figsize: tuple = (12, 6)
    ) -> None:
        """Plot factor returns over time"""
        plt.figure(figsize=figsize)
        plt.plot(factor_data.index, factor_data.values)
        plt.title(title or 'Factor Returns Over Time')
        plt.xlabel('Date')
        plt.ylabel('Returns')
        plt.grid(True)
        plt.show()
        
    @staticmethod
    def plot_factor_correlation(
        factors_data: pd.DataFrame,
        figsize: tuple = (10, 8)
    ) -> None:
        """Plot correlation matrix between factors"""
        plt.figure(figsize=figsize)
        corr = factors_data.corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
        plt.title('Factor Correlation Matrix')
        plt.show()
        
    @staticmethod
    def plot_factor_distribution(
        factor_data: pd.Series,
        bins: int = 50,
        figsize: tuple = (10, 6)
    ) -> None:
        """Plot factor value distribution"""
        plt.figure(figsize=figsize)
        factor_data.hist(bins=bins)
        plt.title('Factor Value Distribution')
        plt.xlabel('Factor Value')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show() 