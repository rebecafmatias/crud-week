# CRUD Week — Simple Python CRUD Example

This repository contains a compact example of a simple CRUD (Create, Read, Update, Delete) application implemented in Python. It is intended as a learning / starter project that demonstrates a small, well-structured code layout separating models, persistence, business logic, and a light controller/runner.

The project is intentionally minimal but organized so you can extend it into a fuller app or use pieces as a reference.

## Features

- Simple CRUD operations organized across a `models`, `crud`, and `database` layer.
- A small `controller` and `main` runner that ties modules together for interactive or scripted use.
- Lightweight and easy to read — good for learning patterns and experimenting.

## Requirements

- Python 3.8 or newer
- [Poetry](https://python-poetry.org/) is recommended for dependency and environment management (optional).

## Installation

Using Poetry (recommended):

```powershell
poetry install
poetry shell
```

Or without Poetry, create and activate a virtual environment, then install any required packages (if you have a `pyproject.toml` or `requirements.txt`):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt  # if present
```

## Running the project

Run the main runner. With Poetry:

```powershell
poetry run python -m src.main
```

Or if you're inside the virtual environment:

```powershell
python -m src.main
```

The `main.py` file is a small entry point that demonstrates how the modules interact. It may run an interactive prompt or a simple scripted flow depending on the project's current implementation.

## Project Structure

- `src/main.py` — the application entry point / runner.
- `src/controller.py` — wiring between user input and CRUD operations (light orchestration).
- `src/crud.py` — core Create / Read / Update / Delete business logic.
- `src/database.py` — persistence helpers (file or SQLite wrapper; adjust to your needs).
- `src/models.py` — data classes / domain models used across the project.

Each module has a focused responsibility so you can swap or extend behavior easily (for example, replacing `database.py` internals with an ORM or remote API).

## Usage Examples

Programmatic usage (importing the modules in a Python REPL or script):

```python
from src import crud, models

# create a new item (example API — adapt to the actual function signatures)
# item = crud.create({'name': 'Example', 'value': 123})

# list items
# items = crud.list_all()
```

Check `src/crud.py` and `src/controller.py` for the precise function names and parameters.

## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE. See the `LICENSE` file for details.