import database
import controller
import models
import etl
from sqlalchemy.orm import Session
from typing import Any
import os

def main(db: Session, model_class: Any, crud_action: str, id: int, crud_value: Any):
    print('Initializing database...')
    database.Base.metadata.create_all(bind=database.engine)
    print('Database initializing concluded!')

    return controller.crud_controller(db,model_class,crud_action,id,crud_value)

# db: Session, model_class: Any, crud_action: str, id: int, crud_value: dict[list]

if __name__ == "__main__":
    db = database.SessionLocal()
    model_class = models.SalesModel
    crud_action = "batch"
    id = 16
    # 1. Descobre onde o arquivo main.py está (pasta src)
    DIR_DO_SCRIPT = os.path.dirname(os.path.abspath(__file__))

    # 2. Constrói o caminho voltando um nível de forma segura
    # (src -> .. -> data -> arquivo)
    csv_path = os.path.join(DIR_DO_SCRIPT, '..', 'data', 'orders_new.csv')
    data_batch_list = etl.open_csv(csv_path,'utf-8')
    final_data_list = etl.calculate_total_sales(data_batch_list)
    crud_value = final_data_list
    # crud_value = {
    #     "status": "Completed"
    # }
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