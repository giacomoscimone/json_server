import requests  # è necessario installare la libreria

base_url = "https://gnews.io/api/v4/top-headlines"

response = requests.get(url)
articles = response.json()["articles"]


