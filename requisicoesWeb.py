import requests
from bs4 import BeautifulSoup

print("\nConectando ao Site")

url = "https://www.uol.com.br"
resposta = requests.get(url)

if resposta.status_code == 200:
    print("conexao bem-sucedida!")

else:
    print("conexao mal-sucedida.codigo do erro:", resposta.status_code)
    exit()

print("\n analisando a estrutura do site")

soup= BeautifulSoup(resposta.text,"html.parser")

pageTitle = soup.title.string
print(f"exibindo titulo da pagina:{pageTitle}")

print("\nprocurando os titulos das noticias")

titles = soup.find_all(["h2","h3"])
keyword = ['acidente', 'doméstica', 'inteligencia artificial']
filteredTiltles = []

print("\n==========titulos enumerados===========")


# for i, titles in enumerate(titles,1):
#     print(f"{i}.{titles.get_text(strip = True)}")


for titles in titles:
    texto = titles.get_text(strip = True)

    if any(palavra.lower() in texto.lower() for palavra in keyword):
        linktag=titles.find('a')
        link=linktag['href'] if linktag and linktag.has_attr('href') else ' link indisponivel'
        filteredTiltles.append((texto,link))


for i,(texto,link) in enumerate (filteredTiltles, 1):
    print(f"{i}.{texto}\n {link}")
