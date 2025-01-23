import requests

url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
response = requests.get(url)

if response.status_code == 200:
    dados_dic = response.json()
    cotacao_atual = float(dados_dic['USDBRL']['bid'])
    mensagem = f'U$ 1 dolar corresponde a R$ {cotacao_atual:.2f}'
    print(mensagem)
else:
    print(f'A requisição falhou {response.status_code}')