from sqlalchemy.orm import Session
from models import EmployeesModel

def create_value(db: Session,value_to_create: dict):
    db_value = EmployeesModel(**value_to_create)

    db.add(db_value)
    db.commit()
    db.refresh(db_value)

def get_all(db: Session):
    return db.query(EmployeesModel).all()

def get_by_id(db: Session,id: int):
    db_get = db.query(EmployeesModel).filter(EmployeesModel.id==id).first()

    if db_get:
        return db_get
    else:
        print(f"This id {id} was not found.")
        return None

def update_by_id(db: Session, id: int, value_to_update: dict):
    db_update = db.query(EmployeesModel).filter(EmployeesModel.id==id).first()

    if db_update:
        for key, value in value_to_update.items():
            setattr(db_update,key,value)
    else:
        print(f"This id {id} was not found.")
        return None
    
    return db_update

def delete_by_id(db: Session, id: int):
    db_delete = db.query(EmployeesModel).filter(EmployeesModel.id==id).first()

    if db_delete:
        db.delete(db_delete)
        db.commit()
    else:
        print(f"This id {id} was not found.")
        return None
    
    return db_delete



