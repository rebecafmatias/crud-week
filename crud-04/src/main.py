from database import engine, Base, SessionLocal
import models
import controller
from sqlalchemy.orm import Session
from typing import Any

def main(db: Session, model_class: Any, crud_type: str, id: int, db_value: dict):
    Base.metadata.create_all(bind=engine)
    
    controller.crud_controller(db,model_class,crud_type,id,db_value)

if __name__ == "__main__":
    db = SessionLocal
    model_class = models.StoreModel
    crud_type = "create"
    id = None
    db_value = {
        "name": "Big Book Store",
        "address": "Av. Beira Mar Norte, 1500",
        "zipcode": 88015200, 
        "city": "Florianopolis",
        "state": "SC"
    }

    main(db, model_class, crud_type, id, db_value)