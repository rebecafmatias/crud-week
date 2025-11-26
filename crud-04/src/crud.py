from sqlalchemy.orm import Session
from typing import Any

def create_record(db: Session, model_class: Any, db_value: dict):
    db_to_add = model_class(**db_value)

    db.add(db_to_add)
    db.commit()
    db.refresh(db_to_add)

    return db_to_add

