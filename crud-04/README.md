# Simple SQLAlchemy CRUD demo

A tiny example project that demonstrates basic CRUD operations with SQLAlchemy and a local SQLite database.

This project was created using Poetry and targets Python 3.11 (I used pyenv local 3.11).

## Prerequisites

- Python 3.11 (pyenv recommended, e.g. `pyenv local 3.11`)
- Poetry (for dependency/virtualenv management)

SQLAlchemy is used as the ORM (declared in `pyproject.toml`: `sqlalchemy >=2.0.44`).

## Quick setup (Windows / PowerShell)

1. Make sure pyenv and Python 3.11 are selected:

```powershell
pyenv local 3.11
```

2. Install dependencies and enter the poetry environment:

```powershell
poetry install
poetry shell
# or run directly without a shell:
poetry run python src/main.py
```

## How to run

- From inside the Poetry shell:

```powershell
python src/main.py
```

- Or one-off with Poetry:

```powershell
poetry run python src/main.py
```

The `src/main.py` file contains an example call in its `if __name__ == '__main__'` block — you can edit the `crud_type` and `db_value` there to run `create`, `get`, `update`, and `delete` operations.

## What the project contains

- `pyproject.toml` — project metadata and registered dependency on SQLAlchemy
- `src/database.py` — SQLAlchemy engine, session and Base
- `src/models.py` — example models: `StoreModel` and `EmployeeModel`
- `src/crud.py` — CRUD utility functions (create, get, update, delete)
- `src/controller.py` — choosable controller that delegates CRUD operations
- `src/main.py` — small runner / example usage and simple script entrypoint

## Database

This project uses a local SQLite database file (`src/chain.db`) and will create tables automatically on first run by calling `Base.metadata.create_all(bind=engine)`.

## Notes

- There are no tests included in this repository.
- The code is intentionally small and simple for learning and demonstration purposes.


