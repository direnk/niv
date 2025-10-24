import pandas as pd
from pandas_datareader import data as web
from pathlib import Path

class TreasuryData:
    """Handles FRED data retrieval and local caching."""

    def __init__(self, cache_dir="data/fred_cache"):
        self.cache_path = Path(cache_dir)
        self.cache_path.mkdir(parents=True, exist_ok=True)

    def fetch(self, start="2010-01-01"):
        """Fetch Treasury yields from FRED with fallback to local cache."""
        try:
            series = ["DGS1MO", "DGS1", "DGS10"]
            df = pd.concat({s: web.DataReader(s, "fred", start) for s in series}, axis=1)
            df.columns = ["1M", "1Y", "10Y"]
            df["spread"] = df["10Y"] - df["1Y"]
            df.to_csv(self.cache_path / "treasury_yields.csv")
        except Exception:
            df = pd.read_csv(self.cache_path / "treasury_yields.csv", index_col=0, parse_dates=True)
        return df.dropna()

    def normalize(self, df):
        """Map Treasury data to NIV state proxies."""
        df["X_t"] = 1 - (df["spread"] / df["spread"].max())   # idle capacity
        df["F_t"] = (df["spread"] / df["spread"].max())       # friction
        df["P_t"] = df["1Y"] / df["10Y"]                      # regeneration
        return df
