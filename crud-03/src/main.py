from database import SessionLocal, engine, Base
from sqlalchemy.orm import Session
import models
import controller
from datetime import date

def main(db: Session, crud_action: str, id: int, crud_value: dict):
    print("Iniciando db...")
    Base.metadata.create_all(bind=engine)
    print("DB inicializado...")

    print(f"Preparing to start the {crud_action} process...")
    controller.get_crud_action(db,crud_action,id,crud_value)
    print(f"\n{crud_action.capitalize()} finished!")

if __name__ == "__main__":
    db = SessionLocal()
    crud_action = "create"
    id = None
    crud_value = {
        "name": "Rebeca Feitosa Matias",
        "birth_gender": "F",
        "birthdate": date(1997, 10, 28),
        "address": "Street example, 111",
        "start_date": date(2025,7, 1),
        "position": "Data Engineer",
        "monthly_salary": 100000
    }
    main(db,crud_action,id,crud_value)