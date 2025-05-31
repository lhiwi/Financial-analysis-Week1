# tests/test_finance.py
import pandas as pd
import pandas_ta as ta  # If using alternative

def test_technical_indicators():
    prices = pd.Series([90.0, 92.5, 91.8, 94.2, 93.5])
    rsi = ta.rsi(prices)
    assert len(rsi) == len(prices)
    assert not pd.isna(rsi.iloc[-1])