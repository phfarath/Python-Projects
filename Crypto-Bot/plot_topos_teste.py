import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
from binance.client import Client
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente
load_dotenv()
api_key = os.getenv('KEY_BINANCE')
secret_key = os.getenv('SECRET_BINANCE')

# Cliente Binance
cliente_binance = Client(api_key, secret_key)

# Função para pegar dados da Binance
def pegar_dados_binance(codigo_ativo, intervalo, limite=1000):
    candles = cliente_binance.get_klines(symbol=codigo_ativo, interval=intervalo, limit=limite)
    precos = pd.DataFrame(candles, columns=[
        'tempo_abertura', 'abertura', 'maxima', 'minima', 'fechamento', 'volume',
        'tempo_fechamento', 'moedas_negociadas', 'num_trades',
        'volume_ativo_base_compra', 'volume_ativo_cotação', '-'
    ])
    precos['fechamento'] = pd.to_numeric(precos['fechamento'], errors='coerce')
    precos['tempo_fechamento'] = pd.to_datetime(precos['tempo_fechamento'], unit='ms').dt.tz_localize('UTC').dt.tz_convert('America/Sao_Paulo')
    return precos[['tempo_fechamento', 'fechamento']]

# Função para identificar topos locais
def identificar_topos(dados, janela=5):
    """
    Identifica topos locais em uma série de preços.
    :param dados: DataFrame com colunas de preços.
    :param janela: Número de candles antes e depois para considerar um topo.
    :return: DataFrame com os topos marcados.
    """
    # Detecta máximas locais
    dados['topo_local'] = dados['fechamento'].iloc[argrelextrema(
        dados['fechamento'].values, np.greater_equal, order=janela
    )]
    return dados

# Função para plotar os preços e destacar os topos
def plotar_topos(dados):
    plt.figure(figsize=(14, 7))
    plt.plot(dados['tempo_fechamento'], dados['fechamento'], label="Preço de Fechamento", color="blue")
    plt.scatter(
        dados['tempo_fechamento'][dados['topo_local'].notnull()],
        dados['topo_local'].dropna(),
        color="red", label="Topos Locais", marker="^", s=100
    )
    plt.title("Identificação de Topos Locais")
    plt.xlabel("Tempo")
    plt.ylabel("Preço")
    plt.legend()
    plt.grid()
    plt.show()

# Configuração do ativo e intervalo de análise
codigo_ativo = "SOLUSDT"  # Trocar pelo ativo desejado
intervalo = Client.KLINE_INTERVAL_1HOUR

# Teste do código
print("Obtendo dados do ativo...")
dados = pegar_dados_binance(codigo_ativo, intervalo)
print("Identificando topos locais...")
dados_com_topos = identificar_topos(dados, janela=5)
print("Plotando os resultados...")
plotar_topos(dados_com_topos)
