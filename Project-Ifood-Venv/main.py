from fastapi import FastAPI, Query
import requests

app = FastAPI()

# criando uma rota para printar Hello World (localhost/api/hello)
@app.get('/api/hello')
def hello_world():
    return {'Hello':'World'}

@app.get('/api/restaurantes/')
# criando uma rota e o restaurante será None quando não tiver nada
def get_restaurantes(restaurante: str = Query(None)):
    '''
        Endpoint para ver o cardapio dos restaurantes
    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    
    if response.status_code == 200:
        dados_json = response.json()
        # caso None, retorna uma lista de restaurantes 
        if restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:

                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurante': restaurante, 'Cardapio': dados_restaurante}
    else:
        return {'Erro':f'{response.status_code} - {response.text}'}

# localhost/docs - abre a documentação do projeto para visualização das APIs