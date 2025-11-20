from database import engine, Base, SessionLocal
from sqlalchemy.orm import Session
from controller import get_crud_action
import models # precisamos chamar para que crie as tabelas do arquivo de models.py

def main(db: Session, action: str, id: int, city: dict):
    print("Initializing database...")
    Base.metadata.create_all(bind=engine)  
    print('Database initialized...')   

    result = get_crud_action(db,action,id,city)

    print(f"{action.capitalize()} completed!")

    print(f"Operation's result: {result}")
    if hasattr(result,"city"):
        print(f"City: {result.city}")

if __name__ == "__main__":

    db = SessionLocal()

    # new_data = {
    #     "city": "Fortaleza",
    #     "state": "CE",
    #     "area_code": 85
    # }

    # main(db,"create",None,new_data) 

    # id = 5

    # data_to_update = {
    #     "city": "Fortaleza"
    # }

    # main(db,"update",id,data_to_update)

    # main(db,"get",id,None)

    # main(db,"delete",id,None)


