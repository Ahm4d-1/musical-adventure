from fastapi import APIRouter
from resources.market.market_service import get_market_data
from resources.market.market_schema import MarketData
router = APIRouter()

@router.get('', response_model=MarketData)
def get_market_data_route():
    return get_market_data()
