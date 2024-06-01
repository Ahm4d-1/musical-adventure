""" Alert DAL"""
"""_summary_
this file is to right any ORM logic for the Alert model
"""
from sqlalchemy.orm import Session
from resources.alerts.alert_model import Alert
from resources.alerts.alert_schema import AlertCreate

def create_rule(rule: AlertCreate, session: Session):
    new_alert = Alert(
        name=rule.name,
        threshold_price=rule.threshold_price,
        symbol=rule.symbol
    )
    session.add(new_alert)
    session.commit()
    session.refresh(new_alert)
    return new_alert

def get_alerts_from_db(skip: int = 0, limit: int = 10, session: Session = None):
    return session.query(Alert).offset(skip).limit(limit).all()
