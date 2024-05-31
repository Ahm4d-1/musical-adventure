""" Alert Rule Service"""
"""_summary_
this file to write any business logic for the Alert Rules
"""
from sqlalchemy.orm import Session
from resources.alert_rules.alert_rule_schema import AlertRuleCreate, AlertRuleUpdate
from resources.alert_rules.alert_rule_dal import create_alert_rule, delete_alert_rule, get_alert_rules, update_alert_rule

def create_new_rule(rule: AlertRuleCreate, session: Session):
    return create_alert_rule(rule, session)

def get_rules(skip: int, limit: int, session: Session):
    return get_alert_rules(skip, limit, session)

def update_rule(rule_id: int, rule: AlertRuleUpdate, session: Session):
    return update_alert_rule(rule_id, rule, session)

def remove_rule(rule_id: int, session: Session):
    return delete_alert_rule(rule_id, session)
