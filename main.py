import requests  # è necessario installare la libreria

apikey = "bcfe6b40ae80a95468731f8d052e151d"
base_url = "https://gnews.io/api/v4/top-headlines"
category = "sports"
country = "it"
lang = "it"
maximum = "2"
url = f"{base_url}?category={category}&lang={lang}&country={country}&max={maximum}&apikey={apikey}"

response = requests.get(url)
articles = response.json()["articles"]


print(articles)
articolo = []
for article in articles:
    # print(article["title"], article["url"])
    articolo = article["title"] + "\n" + article["url"] + "\n"

articolo = str(articolo)

with open('C:\\Users\\Alternanza\\Downloads\\Articolo.txt', 'w') as file:
    file.write(articolo)