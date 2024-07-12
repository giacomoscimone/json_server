import json

json_string = '{"nome": "Giulia Verdi", "età": 25, "email": "giulia.verdi@example.com"}'
dizionario = json.loads(json_string)
print(dizionario)
