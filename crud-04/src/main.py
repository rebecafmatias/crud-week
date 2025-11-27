from database import engine, Base, SessionLocal
import models
import controller
from sqlalchemy.orm import Session
from typing import Any
from datetime import date

def main(db: Session, model_class: Any, crud_type: str, id: int, db_value: dict):
    Base.metadata.create_all(bind=engine)
    
    controller.crud_controller(db,model_class,crud_type,id,db_value)

if __name__ == "__main__":
    
    db = SessionLocal()
    model_class = models.EmployeeModel
    crud_type = "delete"
    id = 2
    # db_value = {
    #     "name": "Big Book Store",
    #     "address": "Av. Beira Mar Norte, 1500",
    #     "zipcode": 88015200, 
    #     "city": "Florianopolis",
    #     "state": "SC"
    # } 
    # db_value = {"name": "The Great Book Store"}

    # db_value = {"name": "Rito da Silva",
    #     "birthdate": date(2000, 5, 20), 
    #     "position": "Vendedor Junior",
    #     "startDate": date(2025, 1, 15),
    #     "storeId": 1
    # }

    db_value = None

    main(db, model_class, crud_type, id, db_value)