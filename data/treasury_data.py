"""
niv/data/treasury_data.py

Fetches and caches U.S. Treasury and FRED data for NIV experiments.
"""

import os
import pandas as pd
from datetime import datetime
from pandas_datareader import data as web


class TreasuryData:
    def __init__(self, cache_dir="data/fred_cache"):
        self.cache_dir = cache_dir
        os.makedirs(self.cache_dir, exist_ok=True)

    def fetch(self, start="2010-01-01", end=None):
        """Download and cache key economic time series from FRED."""
        end = end or datetime.now().strftime("%Y-%m-%d")

        series = {
            "GDP": "GDP",               # Gross Domestic Product
            "CPI": "CPIAUCSL",          # Consumer Price Index
            "DEBT": "GFDEBTN",          # Federal Debt
            "RATE_10Y": "DGS10",        # 10-Year Treasury Constant Maturity Rate
            "UNEMP": "UNRATE"           # Unemployment Rate
        }

        df = pd.DataFrame()
        for name, code in series.items():
            local_path = os.path.join(self.cache_dir, f"{name}.csv")

            # Use cached file if it exists
            if os.path.exists(local_path):
                data = pd.read_csv(local_path, index_col=0, parse_dates=True)
            else:
                try:
                    data = web.DataReader(code, "fred", start, end)
                    data.to_csv(local_path)
                except Exception as e:
                    print(f"⚠️ Failed to fetch {code}: {e}")
                    continue

            df[name] = data[code]

        # Basic normalization (to relative index)
        df = df.fillna(method="ffill")
        for col in df.columns:
            df[col] = df[col] / df[col].iloc[0]
        return df

    def normalize(self, df):
        """Normalize numeric columns between 0–1 for comparative analysis."""
        numeric = df.select_dtypes(include="number")
        return (numeric - numeric.min()) / (numeric.max() - numeric.min())
