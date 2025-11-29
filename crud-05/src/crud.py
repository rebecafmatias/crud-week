from sqlalchemy.orm import Session
from sqlalchemy import insert
from typing import Any

def get_all(db: Session, model_class: Any):
    result = db.query(model_class).all()

    return result

def get_by_id(db: Session, model_class: Any, id: int):
    result = db.query(model_class).filter(model_class.id==id).first()

    if not result:
        print(f'\nID {id} not found!')
        return None

    return result

def create_record(db: Session, model_class: Any, data_value: dict):
    result = model_class(**data_value)

    db.add(result)
    db.commit()
    db.refresh(result)

    return result

def create_batch_record(db: Session, model_class: Any, data_value: list[dict]):
    result = insert(model_class).values(data_value)

    db.execute(result)
    db.commit()
    
    print(f"Batch insert finalizado com sucesso!")
    
    return len(data_value) 

def update_record(db: Session, model_class: Any, id: int, data_value: dict):
    result = db.query(model_class).filter(model_class.id==id).first()

    if not result:
        print(f'\nID {id} not found!')
        return None

    for key,value in data_value.items():
        setattr(result,key,value)
    
    db.commit()
    db.refresh(result)

    return result

def delete_record(db: Session, model_class: Any, id: int):
    result = db.query(model_class).filter(model_class.id==id).first()

    if not result:
        print(f'\nID {id} not found!')
        return None
    
    db.delete(result)
    db.commit()
    return result


    