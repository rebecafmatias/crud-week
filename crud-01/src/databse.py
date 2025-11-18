from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. Vamos declarar o database em que vamos trabalhar

SQLALCHEMY_DATABASE_URL = 'sqlite:///../dogs_breed.db'

# 2. ---------------------------------------------------------------------------------------------------

# Criar engine de conexão com db.
# A engine abre a conexão com o banco. Ela sabe onde está o banco (URL), qual driver usar e como se comunicar.
# Ela mantem um pool de conexões e as reaproveita para não precisar abrir/fechar toda hora.
# Ponto central que o SQLAlchemy usa para toda operação: criar tabela, abrir sesão, fazer queries, commit/rollback

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 3. ---------------------------------------------------------------------------------------------------

# Criar sessão -> cria uma fábrica de sessões (um gerador de conexões)
# O que faz? Cria uma classe de sessão pronta, já configurada com engine.
# Quando você quer conversar com o banco, você cria uma instância assim: db = SessionLocal()

SessionLocal = sessionmaker(autocommit=False, # Você precisa dar .commit() manualmente para salvar alterações (evita salvar merda sem querer).
                            autoflush=False, # Não envia automaticamente mudanças para o banco antes de uma query.
                            bind=engine # Liga (bind) essa fábrica de sessões ao engine.
                            # As sessões criadas por SessionLocal() vão usar este banco de dados aqui. Sem isso, a sessão não sabe aonde se conectar.
                            ) 
# A sessão é o meio de campo entre: você (com objetos Python), o mecanismo SQL (engine) e o banco.

# 4. ---------------------------------------------------------------------------------------------------

# Criar a base que é a classe mãe de todos os modelos ORM. Ela é o ponto central que:
# - registra todas as suas tabelas
# - guarda o mapeamento das classes → tabelas
# - permite criar as tabelas no banco
# - fornece o comportamento ORM (atributos especiais, metadata etc.)
# Você está criando uma base para que todas as suas classes ORM herdem comportamento especial.

Base = declarative_base()

# 5. ---------------------------------------------------------------------------------------------------

# Cria uma sessão, entrega para a rota e fecha depois.

def get_db():
    db = SessionLocal()
    try:
        yield db #yield = “return que pausa” → permite código antes e depois da rota.
    finally:
        db.close


