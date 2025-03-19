import requests

# Configurações da NEF
NEF_BASE_URL = "http://127.0.0.1:8000"  # Endereço da NEF

# Função para influenciar o tráfego
def influence_traffic(nef_url, ue_id, traffic_filters, qos_reference, redirect_info):
    endpoint = f"{nef_url}/nef/v1/traffic-influence"
    payload = {
        "externalId": "app-12345",
        "ueId": ue_id,
        "trafficFilters": traffic_filters,
        "qosReference": qos_reference,
        "redirectInfo": redirect_info
    }

    response = requests.post(endpoint, json=payload)

    if response.status_code == 201:
        print("Requisição de influência de tráfego enviada com sucesso!")
        print(response.json())
    else:
        print(f"Erro ao enviar requisição: {response.status_code}")
        print(response.text)

if __name__ == '__main__':
    # Parâmetros da requisição
    UE_IMSI = "imsi-001010000000001"
    TRAFFIC_FILTERS = [
        {
            "ipv4SrcAddr": "192.168.1.1",
            "ipv4DstAddr": "203.0.113.1",
            "protocol": "TCP",
            "dstPort": 80
        }
    ]
    QOS_REFERENCE = "QoS1"
    REDIRECT_INFO = {
        "redirectEnabled": True,
        "redirectAddressType": "IPv4",
        "redirectServerAddress": "203.0.113.2"
    }

    # Envia a requisição de influência de tráfego
    influence_traffic(NEF_BASE_URL, UE_IMSI, TRAFFIC_FILTERS, QOS_REFERENCE, REDIRECT_INFO)