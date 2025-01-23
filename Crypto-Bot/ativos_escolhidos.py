import pandas as pd
import os
import time
from decimal import Decimal
from binance.client import Client
from binance.enums import *
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('KEY_BINANCE')
secret_key = os.getenv('SECRET_BINANCE')
cliente_binance = Client(api_key, secret_key)

def checa_saldo():
    conta = cliente_binance.get_account()
    for ativo in conta['balances']:
        if float(ativo['free']) > 0:
            print(ativo['asset'], ativo['free'])

def checa_min_compra_ativo(ativo_operado):
    symbol_info = cliente_binance.get_symbol_info(ativo_operado)
    lot_size_filter = next((f for f in symbol_info['filters'] if f['filterType'] == 'LOT_SIZE'))
    min_qty = float(lot_size_filter['minQty'])
    max_qty = float(lot_size_filter['maxQty'])
    step_size = float(lot_size_filter['stepSize'])
    return min_qty, max_qty, step_size

def ajusta_quantidade(quantidade, min_qty, max_qty, step_size):
    """
    Ajusta a quantidade para ser múltiplo do stepSize e valida os limites.
    """
    step_size = Decimal(step_size)
    quantidade = Decimal(quantidade)

    # Ajusta para múltiplo do stepSize
    quantidade_ajustada = (quantidade // step_size) * step_size

    # Garante que está dentro dos limites permitidos
    if quantidade_ajustada < Decimal(min_qty):
        print(f"Erro: Quantidade ajustada ({quantidade_ajustada}) está abaixo do mínimo permitido ({min_qty}).")
        return None
    elif quantidade_ajustada > Decimal(max_qty):
        print(f"Erro: Quantidade ajustada ({quantidade_ajustada}) está acima do máximo permitido ({max_qty}).")
        return None

    return float(quantidade_ajustada)

def truncar_quantidade(quantidade, step_size):
    """Trunca a quantidade para o número máximo de casas decimais permitido."""
    casas_decimais = len(str(step_size).split('.')[-1].rstrip('0'))
    return round(quantidade, casas_decimais)

# INFORMAÇÕES DO ATIVO
periodo_candle = Client.KLINE_INTERVAL_5MINUTE

def pegando_dados(codigo, intervalo):
    # Pegando dados
    candles = cliente_binance.get_klines(symbol=codigo, interval=intervalo, limit=1000)
    # Transformando em dataframe
    precos = pd.DataFrame(candles)
    # Transformando as colunas
    precos.columns = [
        'tempo_abertura', 'abertura', 'maxima', 'minima', 'fechamento', 'volume',
        'tempo_fechamento', 'moedas_negociadas', 'num_trades', 
        'volume_ativo_base_compra', 'volume_ativo_cotação', '-'
    ]
    # Excluindo colunas desnecessárias
    precos = precos[['fechamento', 'tempo_fechamento']]
    # Transformando em datetime de São Paulo
    precos['fechamento'] = pd.to_numeric(precos['fechamento'], errors='coerce')
    precos['tempo_fechamento'] = pd.to_datetime(precos['tempo_fechamento'], unit='ms').dt.tz_localize('UTC')
    precos['tempo_fechamento'] = precos['tempo_fechamento'].dt.tz_convert('America/Sao_Paulo')

    return precos

def estrategia_trade(dados, codigo_ativo, ativo_operado, quantidade, posicao):
    # Criando médias móveis
    dados['media_rapida'] = dados['fechamento'].rolling(window=7).mean()
    dados['media_lenta'] = dados['fechamento'].rolling(window=40).mean()

    ultima_media_rapida = dados['media_rapida'].iloc[-1]
    ultima_media_lenta = dados['media_lenta'].iloc[-1]

    print(f"| Ultima média rápida: {ultima_media_rapida} | Ultima média lenta: {ultima_media_lenta} |")

    # Obter informações do ativo
    min_qty, max_qty, step_size = checa_min_compra_ativo(codigo_ativo)
    quantidade_ajustada = ajusta_quantidade(quantidade, min_qty, max_qty, step_size)

    if quantidade_ajustada is None:
        print("Quantidade inválida. Operação ignorada.")
        return posicao

    conta = cliente_binance.get_account()
    quantidade_atual = float(next((a['free'] for a in conta['balances'] if a['asset'] == ativo_operado), 0))

    if ultima_media_rapida > ultima_media_lenta:
        if not posicao:
            print(f"Comprando {quantidade_ajustada} de {ativo_operado}...")
            cliente_binance.create_order(
                symbol=codigo_ativo,
                side=SIDE_BUY,
                type=ORDER_TYPE_MARKET,
                quantity=quantidade_ajustada
            )
            posicao = True

    elif ultima_media_rapida < ultima_media_lenta:
        if posicao:
            min_qty, max_qty, step_size = checa_min_compra_ativo(codigo_ativo)
            quantidade_ajustada = ajusta_quantidade(quantidade_atual, min_qty, max_qty, step_size)

            if quantidade_ajustada is None:
                print(f"Erro: Quantidade disponível ({quantidade_atual}) não é válida para venda.")
                return posicao

            # Truncando a quantidade ajustada para o número de casas decimais permitido
            quantidade_truncada = truncar_quantidade(quantidade_ajustada, step_size)
            print(f"Vendendo {quantidade_truncada} de {ativo_operado}...")
            cliente_binance.create_order(
                symbol=codigo_ativo,
                side=SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantidade_truncada
            )
            posicao = False


posicao_atual_BTC = False
posicao_atual_ETH = False
posicao_atual_SOL = False
posicao_atual_SUI = False

quantidade_BTC = 0.001
quantidade_ETH = 0.001
quantidade_SOL = 0.001
quantidade_SUI = 0.001

while True:
    print("Atualizando dados e avaliando estratégia...")

#------------------------------------BTC-------------------------------------------
    dados_atualizados = pegando_dados('BTCUSDT', periodo_candle)
    posicao_atual = estrategia_trade(dados_atualizados, 'BTCUSDT', 'BTC', quantidade_BTC, posicao_atual_BTC)

# --------------------------------SOL-------------------------------------------------
    dados_atualizados = pegando_dados('SOLUSDT', periodo_candle)
    posicao_atual = estrategia_trade(dados_atualizados, 'SOLUSDT', 'SOL', quantidade_SOL, posicao_atual_SOL)

# --------------------------------ETH-------------------------------------------------
    dados_atualizados = pegando_dados('ETHUSDT', periodo_candle)
    posicao_atual = estrategia_trade(dados_atualizados, 'ETHUSDT', 'ETH', quantidade_ETH, posicao_atual_ETH)

# --------------------------------SUI-------------------------------------------------
    dados_atualizados = pegando_dados('SUIUSDT', periodo_candle)
    posicao_atual = estrategia_trade(dados_atualizados, 'SUIUSDT', 'SUI', quantidade_SUI, posicao_atual_SUI)

    print("Aguardando próximo ciclo...\n")


    time.sleep(5 * 60)  # 15 minutos




