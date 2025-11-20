from crud import get_all_cities, get_city_by_id, update_city_by_id, create_new_city, delete_city_by_id
from sqlalchemy.orm import Session

def get_crud_action(db: Session, action: str, id: int, city: dict):
    if action.lower() == "get":

        if id:
            result = get_city_by_id(db,id)
        else:
            result = get_all_cities(db)

    elif action.lower()=='create':

        result = create_new_city(db,city)

    elif action.lower()=='update':
        
        result = update_city_by_id(db,id,city)

    elif action.lower()=='delete':
        
        result = delete_city_by_id(db,id)

    return result
        