import requests

# Configurações da NEF
NEF_BASE_URL = "http://127.0.0.5:8000"  # Endereço da NEF

# Função para enviar requisição de influência de tráfego
def influence_traffic(nef_url, json_data):
    endpoint = f"{nef_url}/3gpp-traffic-influence/v1/af001/subscriptions"
    response = requests.post(endpoint, json=json_data)

    if response.status_code == 201:
        print("Requisição de influência de tráfego enviada com sucesso!")
        print(response.json())
    else:
        print(f"Erro ao enviar requisição: {response.status_code}")
        print(response.text)

if __name__ == '__main__':
    # Dados da requisição
    af_data = {
        "afServiceId": "Service1",
        "dnn": "internet",
        "snssai": {
            "sst": 1,
            "sd": "010203"
        },
        "anyUeInd": True,
        "notificationDestination": "http://af:8000/test123",
        "trafficFilters": [
            {
                "flowId": 1,
                "flowDescriptions": [
                    "deny out ip from 192.168.1.0/24 to 10.60.0.0/16"
                ]
            }
        ],
        "trafficRoutes": [
            {
                "dnai": "internet"
            }
        ]
    }

    # Envia a requisição à NEF
    influence_traffic(NEF_BASE_URL, af_data)