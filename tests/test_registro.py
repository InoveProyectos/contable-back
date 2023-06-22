import json
import requests

# token = "98a0975e3e0e55d166090ad401b092169baa5ed7"
headers = {
    # 'Authorization': f'Token {token}',
    "Content-Type": "application/json"
}
base_url = "http://localhost:8000/api/v1.0/registros/registro"
url = base_url + "/asiento/"

data = {
    "fecha_registro":"19/06/2023",
    "debe":[
        {
            "cuenta_id": 1,
            "concepto": "transferecia pago curso PI cuota 1",
            "numero_operacion": "cuota1",
            "monto": 500.50,
        },
        ],
    "haber":[
        {
            "cuenta_id": 2,
            "concepto": "Ingreso en banco",
            "numero_operacion": "BBVA45068",
            "monto": 500.50,
        },
    ]
}  

resp = requests.post(url, json=data, headers=headers)
print(resp.status_code)
print(resp.text)

# print(resp.json())