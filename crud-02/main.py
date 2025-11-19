from src.database import engine, Base

def main():
    print("Initializing database...")
    Base.metadata.create_all(bind=engine)  
    print('Database initialized...')

if __name__ == "__main__":
    main()