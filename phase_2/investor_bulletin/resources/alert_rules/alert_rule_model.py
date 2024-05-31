""" Alert Rule Model """
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from db.models.model_base import Base

class AlertRule(Base):
    __tablename__ = "alert_rules"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    threshold_price = Column(Float)
    symbol = Column(String)

    alerts = relationship("Alert", back_populates="alert_rule")
