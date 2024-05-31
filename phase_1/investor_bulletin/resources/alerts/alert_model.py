""" Alert Model """
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from db.models.model_base import Base

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    threshold_price = Column(Float)
    symbol = Column(String)
    alert_rule_id = Column(Integer, ForeignKey('alert_rules.id'))

    alert_rule = relationship("AlertRule", back_populates="alerts")
