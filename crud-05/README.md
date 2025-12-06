# Logistics SLA Pipeline
A Data Engineering pipeline designed to ingest, transform, and model e-commerce data. The system processes sales orders and asynchronous logistic updates to calculate delivery SLAs and maintain an audit trail of events.

### Project Goal
To simulate a real-world Data Engineering environment where transaction data (Sales) and operational data (Logistics) arrive from different sources at different times. The pipeline ensures:

- Ingestion: Processing new sales orders.

- Event Sourcing: Processing logistic status updates to maintain a historical log (order_history) and update the current state (sales).

- Data Integrity: Strong typing and referential integrity using SQLAlchemy.

### Architecture & Tech Stack

- Language: Python 3.11+

- ORM: SQLAlchemy (for modeling and Database interaction)

- Database: SQLite (for simplicity and ease of setup; can be replaced with any SQL database)

- Data Generation: Faker (implemented with a State Machine logic for consistency)

- Design Pattern: Controller-Service-Repository

### Database Schema

``sales``: Fact table containing the current snapshot of an order (price, product, current status, last update timestamp).

``order_history``: Log table containing all status changes. Every update in the sales table is triggered by an insertion in this history table, ensuring full auditability.

### Project Structure

````
logistics-sla-pipeline/
│
├── data/                   # Storage for Raw CSV files (Generated)
│   ├── orders_new.csv
│   └── logistics_updates.csv
│
├── scripts/                # Utility scripts and tools
│   └── data_generator.py    # Data Generator (Mock with State Machine)
│
├── src/                    # Source code
│   ├── controller.py       # Orchestration logic
│   ├── models.py           # Database Entities (SQLAlchemy)
│   ├── database.py         # DB Connections and Configs
│   ├── crud.py             # CRUD Operations
│   ├── etl.py              # Transformation and Type Casting logic
│   └── main.py             # Pipeline Entrypoint
│
├── readme.md              # Project Documentation  
├── pyproject.toml         # Project configuration
└── poetry.lock            # Dependency lock file
````
### Key Features

**Smart Data Generator (State Machine)**

To ensure realistic testing, a custom script (``scripts/generate_data.py``) was built using ``Faker``.

- Logic: It implements a State Machine to prevent illogical status jumps.

- Example: An order cannot go from ``Pending`` directly to ``Delivered``. The script respects the flow ``Pending`` -> ``Processing`` -> ``Shipped`` -> ``Delivered``, while also ensuring chronological consistency (e.g., delivery_date > sale_date).

**ETL Pipeline**

The core module handles:

- Reading raw CSV files.

- Type Casting: Safely converting strings to native Python types (Datetime, Integer, Float).

- Business Logic: Updating the ``sales`` table only after successfully logging the event in ``order_history``.

**How to Run**

1. Install dependencies:
   ```bash
   poetry install
   ```

2. Generate mock data:
   ```bash
   python -m scripts.generate_data
    # This will create consistent CSV files in the /data folder.
   ```
3. Run the pipeline:
   ```bash
    python -m src.main
    ```

**Roadmap**

[ ] Implement Airflow for task orchestration.

[ ] Add a Control Table to log processed files and ensure idempotency.

[ ] Create an Analytics layer (View) to calculate Average SLA by Region.

[ ] Migrate heavy processing modules to PySpark.

### Author
Developed as a portfolio project to demonstrate Data Engineering capabilities, focusing on Python, SQL, and Data Modeling.