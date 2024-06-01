from sqlalchemy.orm import Session
from db.models.model_base import SessionLocal, engine
from db.models.models import Alert, Rule

# Define your seed data
seed_alert_rules = [
    Rule(name="AAPL Drop Rule", threshold_price=150.00, symbol="AAPL"),
    Rule(name="MSFT High Rule", threshold_price=300.00, symbol="MSFT"),
    Rule(name="GOOG Drop Rule", threshold_price=2500.00, symbol="GOOG"),
    Rule(name="AMZN High Rule", threshold_price=3500.00, symbol="AMZN"),
    Rule(name="META Drop Rule", threshold_price=350.00, symbol="META")
]

def seed_data(session: Session):
    # Insert alert rules
    session.bulk_save_objects(seed_alert_rules)
    session.commit()

    # Fetch all alert rules to use their IDs
    alert_rules = session.query(Rule).all()

    # Create alerts based on the alert rules
    seed_alerts = [
        Alert(name=f"Alert for {rule.symbol}", threshold_price=rule.threshold_price, symbol=rule.symbol, alert_rule_id=rule.id)
        for rule in alert_rules
    ]

    # Insert alerts
    session.bulk_save_objects(seed_alerts)
    session.commit()

if __name__ == "__main__":
    # Create the database tables
    Rule.__table__.create(bind=engine, checkfirst=True)
    Alert.__table__.create(bind=engine, checkfirst=True)

    # Create a new database session
    db = SessionLocal()

    try:
        # Seed the data
        seed_data(db)
        print("Database seeded successfully!")
    except Exception as e:
        print(f"Error seeding database: {e}")
    finally:
        db.close()
