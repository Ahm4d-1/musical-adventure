from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.model_base import get_db
from resources.alert_rules.alert_rule_service import create_new_rule, get_rules, remove_rule, update_rule
from resources.alert_rules.alert_rule_schema import AlertRuleCreate, AlertRuleUpdate
from db.models import RuleSchema
router = APIRouter()

@router.post("", response_model=RuleSchema)
def create_alert_rule(rule: AlertRuleCreate, db: Session = Depends(get_db)):
    return create_new_rule(rule, db)

@router.get("", response_model=list[RuleSchema])
def read_alert_rules(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_rules(skip, limit, db)

@router.patch("/{id}", response_model=RuleSchema)
def update_alert_rule(id: int, rule: AlertRuleUpdate, db: Session = Depends(get_db)):
    db_rule = update_rule(id, rule, db)
    if db_rule is None:
        raise HTTPException(status_code=404, detail="Rule not found")
    return db_rule

@router.delete("/{id}", response_model=RuleSchema)
def delete_alert_rule(id: int, db: Session = Depends(get_db)):
    db_rule = remove_rule(id, db)
    if db_rule is None:
        raise HTTPException(status_code=404, detail="Rule not found")
    return db_rule
