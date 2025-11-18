from databse import engine, Base
from seeds import seed_dogs_breed

# A importação faz o SQLAlchemy registrar os modelos dentro do Base.metadata
# Depois disso, o create_all() já consegue criar as tabelas.

def main():
    
    print('Initializing database...')
    Base.metadata.create_all(bind=engine)  
    print('Database initialized...')
    print('Preparing to seed database...')
    seed_dogs_breed()
    print('Seeding finishid!')

if __name__ == "__main__":
    main()


