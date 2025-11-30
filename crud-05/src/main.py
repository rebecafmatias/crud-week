import database
import controller
import models
from sqlalchemy.orm import Session
from typing import Any

def main(db: Session, model_class: Any, crud_action: str, id: int, crud_value: dict):
    print('Initializing database...')
    database.Base.metadata.create_all(bind=database.engine)
    print('Database initializing concluded!')

    return controller.crud_controller(db,model_class,crud_action,id,crud_value)

# db: Session, model_class: Any, crud_action: str, id: int, crud_value: dict[list]

if __name__ == "__main__":
    db = database.SessionLocal()
    model_class = models.SalesModel
    crud_action = "create"
    id = None
    crud_value = {
        
    }
    main()