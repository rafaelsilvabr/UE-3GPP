import requests

# Configurações da NEF
NEF_BASE_URL = "http://127.0.0.5:8000"  # Endereço da NEF
AF_NOTIFICATION_URL = "http://127.0.0.1:8081/notifications"  # Endpoint do AF

# Função para inscrever-se em eventos da NEF
def subscribe_to_nef(nef_url, af_url, imsi):
    endpoint = f"{nef_url}/nef/v1/subscriptions"
    payload = {
        "externalId": "app-12345",
        "notificationDestination": af_url,
        "monitoredResourceUris": [
            f"/nudm-sdm/v1/{imsi}/location"
        ],
        "event": "LOCATION_REPORT",
        "subscriptionType": "ONESHOT"
    }

    response = requests.post(endpoint, json=payload)

    if response.status_code == 201:
        print("Inscrição realizada com sucesso!")
        print(response.json())
    else:
        print(f"Erro ao inscrever-se: {response.status_code}")
        print(response.text)

if __name__ == '__main__':
    # IMSI do UE que será monitorado
    UE_IMSI = "imsi-001010000000001"

    # Inscreve-se para receber notificações de localização
    subscribe_to_nef(NEF_BASE_URL, AF_NOTIFICATION_URL, UE_IMSI)