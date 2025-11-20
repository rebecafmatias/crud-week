from database import engine, Base
import models # precisamos chamar para que crie as tabelas do arquivo de models.py

def main():
    print("Initializing database...")
    Base.metadata.create_all(bind=engine)  
    print('Database initialized...')

if __name__ == "__main__":
    main()