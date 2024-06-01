from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.models.model_base import get_db
from db.models import AlertSchema
from resources.alerts.alert_service import get_alerts

router = APIRouter()

@router.get("", response_model=list[AlertSchema])
def fetch_alerts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_alerts(skip, limit, db)
