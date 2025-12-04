import csv
from datetime import datetime

def open_csv(path:str,encondig_type=str):
    
    with open(path, 'r', encoding=encondig_type) as file:
        reader = csv.DictReader(file)
        data_list = list(reader)

    return data_list

def calculate_total_sales(data_list:list):

    final_data_list = []
    for i in data_list:
        temp_sales_dict = i
        qty = int(i["quantity"])
        unit = float(i["unit_price"])
        string_date = i["sale_date"]
        total_price = qty*unit
        temp_sales_dict["total_price"] = total_price
        temp_sales_dict["quantity"] = qty
        temp_sales_dict["unit_price"] = unit
        temp_sales_dict["sale_date"] = datetime.strptime(string_date,'%Y-%m-%d').date()
        
        final_data_list.append(temp_sales_dict)
    
    return final_data_list

def altering_updates_data_type(data_list:list):
    final_data_list = []

    for i in data_list:
        temp_log_hist = i
        order_id = int(i["order_id"])
        statusDateTime = datetime.strftime(i["statusDateTime"],'%Y-%m-%d hh:mm:ss')

        temp_log_hist["order_id"] = order_id
        temp_log_hist["statusDateTime"] = statusDateTime

        final_data_list.append(temp_log_hist)
    
    return final_data_list

