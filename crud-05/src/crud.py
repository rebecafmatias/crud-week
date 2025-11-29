from sqlalchemy.orm import Session
from sqlalchemy import insert
from typing import Any

def get_all(db: Session, model_class: Any):
    result = db.query(model_class).all()

    return result

def get_by_id(db: Session, model_class: Any, id: int):
    result = db.query(model_class).filter(model_class.id==id).first()

    return result

def create_record(db: Session, model_class: Any, data_value: dict):
    result = model_class(**data_value)

    db.add(result)
    db.commit()
    db.refresh(result)
    