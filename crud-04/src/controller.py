import crud
from sqlalchemy.orm import Session
from typing import Any

def crud_controller(db: Session, model_class: Any, crud_type: str, id: int, db_value: dict):

    crud_types_list = ['create','get','delete','update']

    if crud_type not in crud_types_list:
        print(f"CRUD type {crud_type} chosen was not found.")
        print(f"Pick one of those and try again: {crud_types_list}.")
        
        return None 
    
    if crud_type == "create":
        result = crud.create_record(db,model_class,db_value)

    elif crud_type == "update":
        result = crud.update_record(db,model_class,id,db_value)

    elif crud_type == "get":
        if id is None or id == 0:
            result = crud.get_record(db,model_class)
        else:
            result = crud.get_record_by_id(db,model_class,id)

    elif crud_type == "delete":
        result = crud.delete_record(db,model_class,id)
    
    return result