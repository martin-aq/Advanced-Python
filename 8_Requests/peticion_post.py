import requests

url = "https://webhook.site/d714ac52-6250-4273-82a4-26e730653059"
payload = {"plato": "pasta", "cantidad": 2}
query_params = {"nombre": "Paco"}
response = requests.post(url, data=payload, params=query_params)