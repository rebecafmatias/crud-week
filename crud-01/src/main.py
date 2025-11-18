from databse import engine, Base
from models import DogsBreedModel 

# A importação faz o SQLAlchemy registrar os modelos dentro do Base.metadata
# Depois disso, o create_all() já consegue criar as tabelas.

def main():
    
    print('Initializing database...')
    Base.metadata.create_all(bind=engine)  
    print('Database initialized...')

if __name__ == "__main__":
    main()


