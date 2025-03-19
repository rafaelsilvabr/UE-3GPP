import requests

# Configurações da NEF
NEF_BASE_URL = "http://127.0.0.5:8000"  # Endereço da NEF
AF_ID = "af001"  # Identificador do AF

# Função para enviar a regra de bloqueio
def block_internet_traffic(nef_url, af_id):
    endpoint = f"{nef_url}/3gpp-traffic-influence/v1/{af_id}/subscriptions"
    payload = {
        "afServiceId": "BlockInternet",
        "dnn": "internet",
        "snssai": {
            "sst": 1,
            "sd": "010203"
        },
        "anyUeInd": True,
        "notificationDestination": "http://127.0.0.1:8001/notifications",
        "trafficFilters": [
            {
                "flowId": 1,
                "flowDescriptions": [
                    "deny out ip from 60.60.0.0/24 to any"
                ]
            }
        ],
        "trafficRoutes": [
            {
                "dnai": "blocked"
            }
        ]
    }

    response = requests.post(endpoint, json=payload)

    if response.status_code == 201:
        print("Regra de bloqueio enviada com sucesso!")
        print(response.json())
    else:
        print(f"Erro ao enviar regra de bloqueio: {response.status_code}")
        print(response.text)

if __name__ == '__main__':
    # Envia a regra de bloqueio à NEF
    block_internet_traffic(NEF_BASE_URL, AF_ID)