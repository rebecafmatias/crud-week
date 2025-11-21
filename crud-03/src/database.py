from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

# Informar o path do database
SQLALCHEMY_DATABASE_URL = 'sqlite:///../company_hr.db'

# Criar engine responsável por abrir a conexão com o banco. Ela sabe onde o banco está e qual driver usar e como se comunicar.
# Ponto central que o SQLAlchemy utiliza para todos as operações do crud.
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Criar a fábrica de sessões (um gerador de conexões). Cria uma classe de sessão pronta já configurada com engine.
# Quando você quer conversar com o banco, cria uma instância (db = SessionLocal())
SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)

# Criar a classe mãe de todos os modelos ORM. Todas as classes criadas no projeto herdam um comportamento especial que vem dela.
Base = declarative_base()