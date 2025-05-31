# tests/test_finance.py
import pandas as pd
import pandas_ta as ta
import numpy as np  # Explicit import for NaN

def test_technical_indicators():
    """Test pandas_ta technical indicators"""
    prices = pd.Series([90.0, 92.5, 91.8, 94.2, 93.5])
    
    # Calculate RSI
    rsi = ta.rsi(prices, length=3)
    
    # Validate results
    assert len(rsi) == len(prices)
    assert not np.isnan(rsi.iloc[-1])  # Use np.isnan instead of pd.isna