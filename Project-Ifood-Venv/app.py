import requests
import json

# definindo a url
url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
# solicitando os dados com o .get()
response = requests.get(url)
# caso a resposta seja 200, deu certo 
print(response)

# caso dê certo
if response.status_code == 200:
    # converte os dados em JSON
    dados_json = response.json()
    # criando um dicionario para os dados do restaurante
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        # caso o restaurante ainda não exista, criamos um
        if nome_do_restaurante not in dados_restaurante:
            dados_restaurante[nome_do_restaurante] = []

        # adicionando os itens no cardapio do restaurante 
        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })
else:
    print(f'O erro foi {response.status_code}')

# criando items para cada um dos restaurantes 
for nome_do_restaurante, dados in dados_restaurante.items():
    # definindo o nome do arquivo como restaurantes 
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    # abrindo o arquivo e colocando informações com ('w')
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)
