from sqlalchemy.orm import Session
from typing import Any

def get_all_data(db: Session, model_class: Any):
    result = db.query(model_class).all()

    return result

def get_data_by_id(db: Session, model_class: Any, id: int):
    result = db.query(model_class).filter(model_class.id==id).first()

    return result
