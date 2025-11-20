from sqlalchemy.orm import Session
from models import BrazilCitiesModel

# Função para selecionar todos os registros:

def get_all_cities(db: Session):
    return db.query(BrazilCitiesModel).all()

# Função para selecionar registro por id:

def get_city_by_id(db: Session, id: int):
    return db.query(BrazilCitiesModel).filter(BrazilCitiesModel.id==id).first()

# Função para criar novo registro:

def create_new_city(db: Session, city_create):
    db_city = BrazilCitiesModel(**city_create)

    db.add(db_city)
    db.commit()
    db.refresh(db_city)

    return db_city

# Função para atualizar um registro:

def update_city_by_id(db: Session, id: int, city_update):
    db_city = db.query(BrazilCitiesModel).filter(BrazilCitiesModel.id==id).first()
    if db_city:
        for key, value in city_update.items():
            setattr(db_city,key,value)

        db.commit()
        db.refresh(db_city)
    else:
        print(f"Essa cidade, id {id}, não foi encontrada na base de dados.")
        return None
    
    return db_city

# Função para deletar um registro:

def delete_city_by_id(db: Session, id: int):
    db_city = db.query(BrazilCitiesModel).filter(BrazilCitiesModel.id==id).first()

    if db_city:
        db.delete(db_city)
        db.commit()
    else:
        print(f"Essa cidade, id {id}, não foi encontrada na base de dados.")
        return None

    return db_city