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

    # Your crud action options are: ["create","update","get","delete"]
    crud_action = "create"

    # Specify an ID if you want to get, update or delete a value by id

    id = None

    # Create a dict with the information you want to create or update on the db

    crud_value = {
        "name": "Sheldon Cooper",
        "birth_gender": "M",
        "birthdate": date(1980, 2, 26),
        "address": "Street example, 222",
        "start_date": date(2025,7, 1),
        "position": "Physicist",
        "monthly_salary": 100000
    } ## creating example

    # crud_value = {
    #     "position": "Professor"
    # } ## updating by id example

    main(db,crud_action,id,crud_value)