from celery import Celery

from core.messaging import publish_event
from db.models.model_base import get_db
from resources.alert_rules.alert_rule_service import get_rules
from resources.market.market_service import get_market_data

def create_celery_app():
    return Celery('tasks', broker='pyamqp://guest@localhost//')

celery_app = create_celery_app()

@celery_app.task
def check_market_data_and_rules():

    # Fetch the latest market data
    market_data = get_market_data()

    db = next(get_db())

    # Fetch all user rules
    user_rules = get_rules(0, 0, db)

    # Process the data
    alerts = []
    for rule in user_rules:
        symbol = rule.symbol
        threshold_price = rule.threshold_price
        market_price = market_data.get(symbol)
        if symbol in market_data and market_price and float(market_price) < threshold_price:
            alert_message = f"Alert: {symbol} has fallen below {threshold_price}"
            alerts.append(alert_message)

            # Publish THRESHOLD_ALERT event
            event = {
                "type": "THRESHOLD_ALERT",
                "message": alert_message,
                "name": f"Price Drop Alert for {symbol}",
                "threshold_price": threshold_price,
                "symbol": symbol
            }
            publish_event(event)

    return alerts
