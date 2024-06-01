""" Rule Service"""
"""_summary_
this file to write any business logic for the Rules
"""
from sqlalchemy.orm import Session
from resources.alerts.alert_schema import AlertCreate
from resources.alerts.alert_dal import create_rule, get_alerts_from_db

def create_new_alert(rule: AlertCreate, session: Session):
    return create_rule(rule=rule, session=session)

def get_alerts(skip: int, limit: int, session: Session):
    return get_alerts_from_db(skip, limit, session)
