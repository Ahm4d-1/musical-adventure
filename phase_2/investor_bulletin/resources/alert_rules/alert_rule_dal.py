""" Alert Rule  DAL"""
"""_summary_
this file is to right any ORM logic for the Alert Rule model
"""
from sqlalchemy.orm import Session
from resources.alert_rules.alert_rule_schema import AlertRuleCreate, AlertRuleUpdate
from db.models import Rule

def create_alert_rule(rule: AlertRuleCreate, session):
    new_rule = Rule(
        name=rule.name,
        threshold_price=rule.threshold_price,
        symbol=rule.symbol
    )
    session.add(new_rule)
    session.commit()
    session.refresh(new_rule)
    return new_rule

def get_alert_rule_by_id(rule_id: int, session: Session):
    return session.query(Rule).filter(Rule.id == rule_id).first()

def get_alert_rules(skip: int = 0, limit: int = 10, session: Session = None):
    return session.query(Rule).offset(skip).limit(limit).all()

def update_alert_rule(rule_id: int, rule: AlertRuleUpdate, session: Session):
    db_rule = get_alert_rule_by_id(rule_id, session)
    if db_rule:
        db_rule.name = rule.name
        db_rule.threshold_price = rule.threshold_price
        db_rule.symbol = rule.symbol
        session.commit()
        session.refresh(db_rule)
        return db_rule
    return None

def delete_alert_rule(rule_id: int, session: Session):
    db_rule = get_alert_rule_by_id(rule_id, session)
    if db_rule:
        session.delete(db_rule)
        session.commit()
        return db_rule
    return None
