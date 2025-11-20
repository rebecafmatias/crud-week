# crud-02

Projeto de exemplo com operações CRUD em Python, pensado para estudos e testes com `SQLAlchemy` e `pydantic`.

**Resumo rápido**

- Python: 3.11+
- Gerenciador de ambiente e dependências: `poetry`
- ORM: `SQLAlchemy` (2.x)
- Validação / modelos: `pydantic` (2.x)

## Objetivo

Este projeto demonstra operações CRUD (create, read, update, delete) organizadas dentro do diretório `src/`. Ele monta uma pequena base usando `SQLAlchemy` e expõe funções no código para executar cada ação (veja `src/controller.py` e `src/crud.py`). O módulo principal `src/main.py` mostra exemplos de chamadas comentadas.

## Requisitos

- Instale `pyenv` e defina a versão local do Python para `3.11` (opcional, mas recomendado para reprodutiblidade)
- `poetry` para gerenciar dependências e ambiente virtual

## Instalação (passo a passo)

1. (opcional) Instale e selecione a versão do Python com `pyenv`:

   ```powershell
   pyenv install 3.11.0
   pyenv local 3.11.0
   ```

2. Instale dependências com `poetry` (na raiz do projeto):

   ```powershell
   poetry install
   ```

3. Entrar no shell do `poetry` (opcional):

   ```powershell
   poetry shell
   ```

Observação: este projeto declara no `pyproject.toml` as dependências `sqlalchemy` e `pydantic`.

## Executando o projeto

O ponto de entrada é o módulo `src.main`. Ele cria as tabelas automaticamente usando `Base.metadata.create_all(bind=engine)` e fornece exemplos comentados para testar as operações CRUD.

- Executar diretamente via `poetry` (recomendado):

  ```powershell
  poetry run python -m src.main
  ```

- Ou, se estiver dentro do `poetry shell`:

  ```powershell
  python -m src.main
  ```

Nota: `src/main.py` contém chamadas de exemplo comentadas. Para testar uma operação, edite o bloco no final do arquivo para descomentar a chamada `main(db, action, id, city)` correspondente e execute o módulo.

## Estrutura do projeto

- `pyproject.toml` - configuração do projeto e dependências (Poetry)
- `README.md` - este arquivo
- `src/` - código fonte
  - `main.py` - ponto de entrada com exemplos de uso
  - `database.py` - configuração do `engine`, `SessionLocal` e `Base` do SQLAlchemy
  - `models.py` - modelos / tabelas declaradas com SQLAlchemy
  - `crud.py` - operações CRUD sobre os modelos
  - `controller.py` - camada que interpreta ações e chama funções CRUD

## Exemplos de uso

1. Criar uma entrada (exemplo comentado em `src/main.py`):

   - No arquivo `src/main.py` há um dicionário de exemplo chamado `new_data`. Descomente o trecho:

   ```python
   main(db, "create", None, new_data)
   ```

   e execute `poetry run python -m src.main`.

2. Ler / Atualizar / Deletar

   - Há exemplos comentados para `get`, `update` e `delete` no final de `src/main.py`. Ajuste o `id` e os campos, descomente e execute.

## Desenvolvimento

- Para adicionar dependências: `poetry add <package>`
- Para rodar em modo interativo use `poetry shell` e depois `python -m src.main` ou importar funções nos seus testes/REPL.

## Testes

Não há uma suíte de testes incluída neste repositório por enquanto. Para adicionar `pytest`:

```powershell
poetry add --dev pytest
```

E então crie uma pasta `tests/` com seus casos.

## Notas sobre o `pyproject.toml`

As dependências atuais (conforme `pyproject.toml`) são:

- `sqlalchemy >=2.0.44, <3.0.0`
- `pydantic >=2.12.4, <3.0.0`

## Licença

Este repositório segue o arquivo LICENSE na raiz. 




