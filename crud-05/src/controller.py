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

    elif crud_action == "update":
        result = crud.update_record(db,model_class,id,data_value)

    elif crud_action == "delete":
        result = crud.delete_record(db,model_class,id)

    elif crud_action == "get":
        if id == None or id == 0:
            result = crud.get_all(db,model_class)
        else:
            result = crud.get_by_id(db,model_class,id)
    
    return result