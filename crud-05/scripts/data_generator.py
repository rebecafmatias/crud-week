import csv
import random
import os
from faker import Faker
from datetime import datetime, timedelta

fake = Faker('pt_BR')

# --- CONFIGURAÇÕES ---
QTD_VENDAS = 50
QTD_UPDATES = 40 # Aumentei um pouco pra garantir que alguns pedidos avancem bastante
CAMINHO_PASTA = '../data' 

# --- FLUXO DE STATUS (MÁQUINA DE ESTADOS) ---
# Define qual é o PRÓXIMO status permitido baseado no ATUAL
PROXIMO_PASSO = {
    'Pending': ['Processing', 'Cancelled'],
    'Processing': ['Shipped'],
    'Shipped': ['Delivered'],
    'Delivered': [], # Fim da linha
    'Cancelled': []  # Fim da linha
}

def gerar_massa_de_dados():
    if not os.path.exists(CAMINHO_PASTA):
        os.makedirs(CAMINHO_PASTA)

    print(f"🚀 Iniciando geração de dados simulados...")

    # ==============================================================================
    # 1. GERADOR DE VENDAS 
    # ==============================================================================
    sales_data = []
    
    # Dicionário para controlar o estado atual de cada pedido na memória
    # Chave: ID do pedido -> Valor: {status: 'Pending', data: datetime}
    controle_pedidos = {} 

    start_id = random.randint(1000, 9000)

    for i in range(QTD_VENDAS):
        current_id = start_id + i
        # Venda aconteceu entre 30 dias atrás e ontem (pra dar tempo de ter updates)
        sale_date = fake.date_time_between(start_date='-30d', end_date='-1d')
        
        row = {
            "order_id": current_id,
            "customer_name": fake.name(),
            "product": random.choice(['Notebook Dell G15', 'Mouse Logitech MX', 'Monitor LG Ultrawide', 'Teclado Keychron']),
            "quantity": random.randint(1, 5),
            "unit_price": round(random.uniform(150.0, 4500.0), 2),
            "status": "Pending",
            "sale_date": sale_date.strftime("%Y-%m-%d") # Salva só a data na venda
        }
        
        sales_data.append(row)
        
        # Inicializa o controle desse pedido
        controle_pedidos[current_id] = {
            "status": "Pending",
            "last_date": sale_date # Guarda a data exata com hora
        }

    # Salva CSV de Vendas
    with open(f"{CAMINHO_PASTA}/orders_new.csv", 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=sales_data[0].keys())
        writer.writeheader()
        writer.writerows(sales_data)
    
    print(f"✅ Vendas geradas.")


    # ==============================================================================
    # 2. GERADOR DE UPDATES LOGÍSTICOS (COM LÓGICA)
    # ==============================================================================
    updates_data = []
    
    # Vamos tentar gerar updates. 
    # Como alguns pedidos podem chegar no fim da linha ('Delivered'),
    # precisamos filtrar quais IDs ainda podem receber updates.
    
    for _ in range(QTD_UPDATES):
        # Filtra apenas pedidos que NÃO estão finalizados
        ids_disponiveis = [k for k, v in controle_pedidos.items() if v['status'] not in ['Delivered', 'Cancelled']]
        
        if not ids_disponiveis:
            print("⚠️ Todos os pedidos foram finalizados antes de atingir a meta de updates.")
            break

        selected_id = random.choice(ids_disponiveis)
        dados_atuais = controle_pedidos[selected_id]
        
        # Descobre qual pode ser o próximo status
        opcoes_proximo = PROXIMO_PASSO[dados_atuais['status']]
        new_status = random.choice(opcoes_proximo)
        
        # Gera data do evento: Tem que ser DEPOIS da última atualização desse pedido
        # Adiciona entre 1 hora e 2 dias aleatoriamente
        tempo_decorrido = timedelta(hours=random.randint(1, 48))
        event_date = dados_atuais['last_date'] + tempo_decorrido
        
        # Garante que não passamos da data de hoje (futuro)
        if event_date > datetime.now():
            event_date = datetime.now()

        row = {
            "order_id": selected_id,
            "new_status": new_status,
            "event_date": event_date.strftime("%Y-%m-%d %H:%M:%S")
        }
        updates_data.append(row)
        
        # Atualiza o controle na memória para o próximo loop saber
        controle_pedidos[selected_id]['status'] = new_status
        controle_pedidos[selected_id]['last_date'] = event_date

    # Salva CSV de Updates
    with open(f"{CAMINHO_PASTA}/logistics_updates.csv", 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=updates_data[0].keys())
        writer.writeheader()
        writer.writerows(updates_data)

    print(f"✅ Updates gerados com coerência cronológica.")

if __name__ == "__main__":
    gerar_massa_de_dados()