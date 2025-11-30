import database
import controller
import models
import etl
from sqlalchemy.orm import Session
from typing import Any
from datetime import date

def main(db: Session, model_class: Any, crud_action: str, id: int, crud_value: Any):
    print('Initializing database...')
    database.Base.metadata.create_all(bind=database.engine)
    print('Database initializing concluded!')

    return controller.crud_controller(db,model_class,crud_action,id,crud_value)

# db: Session, model_class: Any, crud_action: str, id: int, crud_value: dict[list]

if __name__ == "__main__":
    db = database.SessionLocal()
    model_class = models.SalesModel
    crud_action = "update"
    id = 5
    csv_path = '..\data\sales.csv'
    data_batch_list = etl.open_csv(csv_path,'utf-8')
    final_data_list = etl.calculate_total_sales(data_batch_list)
    crud_value = {
        "status": "Completed"
    }
    # {
    #     "customer_name": "Rebeca F",
    #     "product": "Notebook Dell G15",
    #     "quantity": 1,
    #     "unit_price": 4500.00,
    #     "status": "Completed",
    #     "sale_date": date(2025, 11, 25),
    #     "total_price": 4500.00
    # }
    result = main(db,model_class,crud_action,id,crud_value)