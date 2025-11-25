from sqlalchemy.orm import Session
import models

def create_employee(db: Session, employee_db: dict):
    db_to_add = models.EmployeeModel(**employee_db)

    db.add(db_to_add)
    db.commit()
    db.refresh(db_to_add)