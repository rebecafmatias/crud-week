from sqlalchemy.orm import Session
from typing import Any

def create_record(db: Session, model_class: Any, db_value: dict):
    db_to_add = model_class(**db_value)

    db.add(db_to_add)
    db.commit()
    db.refresh(db_to_add)

    return db_to_add

def update_record(db: Session, model_class: Any, id: int, db_value: dict):
    db_to_update = db.query(model_class).filter(model_class.id == id).first()

    if db_to_update:
        for key,value in db_value.items():
            setattr(db_to_update,key,value)
            
            db.commit()
            db.refresh(db_to_update)

        else:
            print(f"This id {id} was not found.")
            return None
    
    return db_to_update