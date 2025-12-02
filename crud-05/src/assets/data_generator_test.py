import csv
import random
import os
from faker import Faker
from datetime import datetime, timedelta

# Inicializa o Faker em Português
fake = Faker('pt_BR')

# --- CONFIGURAÇÕES ---
QTD_VENDAS = 50
QTD_UPDATES = 30
CAMINHO_PASTA = 'data' # Certifique-se de criar essa pasta antes!

def gerar_massa_de_dados():
    # Garante que a pasta existe
    if not os.path.exists(CAMINHO_PASTA):
        os.makedirs(CAMINHO_PASTA)

    print(f"🚀 Iniciando geração de dados simulados...")

    # ==============================================================================
    # 1. GERADOR DE VENDAS (PIPELINE 1)
    # ==============================================================================
    sales_data = []
    created_ids = [] # Lista auxiliar para garantir integridade

    # Vamos começar os IDs do 1000 para ficar bonito
    start_id = random.randint(1000, 9000)

    for i in range(QTD_VENDAS):
        current_id = start_id + i
        
        # Gera data de venda nos últimos 30 dias
        sale_date = fake.date_between(start_date='-30d', end_date='today')
        
        row = {
            "order_id": current_id,
            "customer_name": fake.name(),
            "product": random.choice(['Notebook Dell G15', 'Mouse Logitech MX', 'Monitor LG Ultrawide', 'Teclado Keychron', 'Headset HyperX']),
            "quantity": random.randint(1, 5),
            "unit_price": round(random.uniform(150.0, 4500.0), 2),
            "status": "Pending", # Todo pedido nasce Pending
            "sale_date": sale_date
        }
        
        sales_data.append(row)
        created_ids.append(current_id) # Guarda o ID na memória

    # Salva CSV de Vendas
    file_orders = f"{CAMINHO_PASTA}/orders_new.csv"
    with open(file_orders, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=sales_data[0].keys())
        writer.writeheader()
        writer.writerows(sales_data)
    
    print(f"✅ Arquivo gerado: {file_orders} ({QTD_VENDAS} registros)")


    # ==============================================================================
    # 2. GERADOR DE UPDATES LOGÍSTICOS (PIPELINE 2)
    # ==============================================================================
    updates_data = []
    
    # Status possíveis na logística
    status_options = ['Processing', 'Shipped', 'Delivered', 'Cancelled']

    for _ in range(QTD_UPDATES):
        # O SEGREDO: Só escolhe IDs que sabemos que existem!
        selected_id = random.choice(created_ids)
        
        # Gera uma data/hora aleatória recente
        event_date = fake.date_time_between(start_date='-5d', end_date='now')
        
        row = {
            "order_id": selected_id,
            "new_status": random.choice(status_options),
            "event_date": event_date.strftime("%Y-%m-%d %H:%M:%S")
        }
        updates_data.append(row)

    # Salva CSV de Updates
    file_updates = f"{CAMINHO_PASTA}/logistics_updates.csv"
    with open(file_updates, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=updates_data[0].keys())
        writer.writeheader()
        writer.writerows(updates_data)

    print(f"✅ Arquivo gerado: {file_updates} ({QTD_UPDATES} registros)")
    print("\n📦 Massa de dados pronta para teste!")

if __name__ == "__main__":
    gerar_massa_de_dados()