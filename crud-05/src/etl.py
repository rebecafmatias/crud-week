import csv

csv_path = '..\data\sales.csv'

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
        total_price = qty*unit
        temp_sales_dict["total_price"] = total_price
        final_data_list.append(temp_sales_dict)
    
    return final_data_list

