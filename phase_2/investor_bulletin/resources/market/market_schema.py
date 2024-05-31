""" Market Schema """
"""_summary_
This file to abstract any validation logic for the Market
"""

from pydantic import BaseModel, Field

class MarketData(BaseModel):
    AAPL: float = Field(..., example=150.25)
    MSFT: float = Field(..., example=300.10)
    GOOG: float = Field(..., example=2800.50)
    AMZN: float = Field(..., example=3400.00)
    META: float = Field(..., example=350.75)
