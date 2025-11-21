from database import SessionLocal, engine, Base

def main():
    print("Iniciando db...")
    Base.metadata.create_all(bind=engine)
    print("DB inicializado...")

if __name__ == "__main__":
    main()