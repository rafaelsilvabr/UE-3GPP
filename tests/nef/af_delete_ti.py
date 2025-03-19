import requests

# Configurações da NEF
NEF_BASE_URL = "http://127.0.0.5:8000"  # Endereço da NEF
AF_ID = "af001"  # Identificador do AF
SUBSCRIPTION_ID = "1"  # ID da inscrição a ser removida

# Função para remover uma regra de influência de tráfego
def remove_traffic_influence(nef_url, af_id, subscription_id):
    endpoint = f"{nef_url}/3gpp-traffic-influence/v1/{af_id}/subscriptions/{subscription_id}"
    response = requests.delete(endpoint)

    if response.status_code == 204:
        print(f"Inscrição {subscription_id} removida com sucesso!")
    else:
        print(f"Erro ao remover inscrição: {response.status_code}")
        print(response.text)

if __name__ == '__main__':
    # Remove a inscrição de influência de tráfego
    remove_traffic_influence(NEF_BASE_URL, AF_ID, SUBSCRIPTION_ID)