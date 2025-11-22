import crud
from sqlalchemy.orm import Session

def get_crud_action(db: Session, crud_action: str ,id: int, crud_value: dict):
    
    crud_action_lower = crud_action.lower()
    valid_actions = ["create","update","get","delete"]
    
    if crud_action_lower not in valid_actions:
        print(f"Error: the action informed {crud_action} does not exist!")
        print(f"Pick one of those: {valid_actions}")
        return None

    if crud_action_lower == "create":
        result = crud.create_value(db,crud_value)
    elif crud_action_lower == "update":
        result = crud.update_by_id(db,id,crud_value)

    elif crud_action_lower == "get":
        if id is None:
            result = crud.get_all(db)
        else:
            result = crud.get_by_id(db,id)

    elif crud_action_lower == "delete":
        result = crud.delete_by_id(db,id)

    return result
