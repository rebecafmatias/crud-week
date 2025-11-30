from sqlalchemy.orm import Session
import crud
from typing import Any

def crud_controller(db: Session, model_class: Any, crud_action: str, id: int, data_value: dict):

    valid_crud_actions = ['create', 'update', 'get', 'delete']

    if crud_action not in valid_crud_actions:
        print(f"Crud action chosen {crud_action} not valid.")
        print(f"Pick one of those: {valid_crud_actions}.")

        return None
    
    if crud_action == "create":
        result = crud.create_record(db,model_class,data_value)