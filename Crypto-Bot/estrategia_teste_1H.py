import pandas as pd
import os
import time
from decimal import Decimal
from binance.client import Client
from binance.enums import *
from dotenv import load_dotenv
from termcolor import colored

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

def obter_preco_atual(codigo_ativo):
    """
    Obtém o preço atual do ativo na Binance.
    """
    ticker = cliente_binance.get_symbol_ticker(symbol=codigo_ativo)
    return float(ticker['price'])

def calcular_quantidade(valor_dolares, preco_atual, step_size):
    """
    Calcula a quantidade com base no valor em dólares e no preço atual, ajustada ao step size.
    """
    quantidade = valor_dolares / preco_atual
    return truncar_quantidade(quantidade, step_size)

def executar_ordem(tipo, ativo, quantidade, preco_atual):
    """
    Executa a ordem no modo real ou simula no modo de teste.
    """
    global preco_compra
    if tipo == "COMPRA":
        preco_compra = preco_atual

    if modo_teste:
        print(
            colored(
                f"[MODO TESTE] Simulando {tipo} de {quantidade} {ativo} ao preço de {preco_atual:.2f}. Nenhuma transação real foi realizada.",
                "green" if tipo == "COMPRA" else "red"
            )
        )
    else:
        # Realizar ordem real na Binance
        if tipo == "COMPRA":
            cliente_binance.create_order(
                symbol=codigo_ativo,
                side=SIDE_BUY,
                type=ORDER_TYPE_MARKET,
                quantity=quantidade
            )
        elif tipo == "VENDA":
            cliente_binance.create_order(
                symbol=codigo_ativo,
                side=SIDE_SELL,
                type=ORDER_TYPE_MARKET,
                quantity=quantidade
            )
        print(
            colored(
                f"[MODO REAL] Ordem de {tipo} executada para {quantidade} {ativo} ao preço de {preco_atual:.2f}.",
                "green" if tipo == "COMPRA" else "red"
            )
        )

def pegando_dados(codigo, intervalo):
    candles = cliente_binance.get_klines(symbol=codigo, interval=intervalo, limit=1000)
    precos = pd.DataFrame(candles)
    precos.columns = [
        'tempo_abertura', 'abertura', 'maxima', 'minima', 'fechamento', 'volume',
        'tempo_fechamento', 'moedas_negociadas', 'num_trades', 
        'volume_ativo_base_compra', 'volume_ativo_cotação', '-'
    ]
    precos = precos[['abertura', 'maxima', 'minima', 'fechamento', 'tempo_fechamento']]
    precos['fechamento'] = pd.to_numeric(precos['fechamento'], errors='coerce')
    precos['tempo_fechamento'] = pd.to_datetime(precos['tempo_fechamento'], unit='ms').dt.tz_localize('UTC')
    precos['tempo_fechamento'] = precos['tempo_fechamento'].dt.tz_convert('America/Sao_Paulo')
    return precos

def calcula_hma(dados, periodo, metodo='fechamento'):

    if metodo == 'ohlc':  # Média de abertura, máxima, mínima e fechamento
        dados['preco_medio'] = dados[['abertura', 'maxima', 'minima', 'fechamento']].mean(axis=1)
    else:  # Apenas fechamento
        dados['preco_medio'] = dados['fechamento']
    wma_metade = 2 * dados['preco_medio'].rolling(window=periodo // 2).mean()
    wma_completa = dados['preco_medio'].rolling(window=periodo).mean()
    diff_wma = wma_metade - wma_completa
    hma = diff_wma.rolling(window=int(periodo**0.5)).mean()
    return hma

def estrategia_trade(dados, codigo_ativo, ativo_operado, quantidade, posicao):
    """
    Estratégia de trade utilizando a Média Móvel de Hull (HMA).
    """
    global preco_compra

    dados['hma_curta'] = calcula_hma(dados, 9)
    dados['hma_longa'] = calcula_hma(dados, 21)

    ultima_hma_curta = dados['hma_curta'].iloc[-1]
    ultima_hma_longa = dados['hma_longa'].iloc[-1]

    preco_atual = obter_preco_atual(codigo_ativo)
    min_qty, max_qty, step_size = checa_min_compra_ativo(codigo_ativo)

    print(f"| Preço Atual: {preco_atual:.2f} | Última HMA Curta: {ultima_hma_curta:.2f} | Última HMA Longa: {ultima_hma_longa:.2f} |")

    if ultima_hma_curta > ultima_hma_longa and not posicao:
        quantidade = calcular_quantidade(valor_dolares, preco_atual, step_size)

        if quantidade is None:
            print(f"Erro: Quantidade {quantidade} não é válida para compra.")
            return posicao

        executar_ordem("COMPRA", ativo_operado, quantidade, preco_atual)
        posicao = True  # Atualiza a posição para indicar que há um ativo comprado

    elif ultima_hma_curta < ultima_hma_longa and posicao:
        conta = cliente_binance.get_account()
        for ativo in conta['balances']:
            if ativo['asset'] == ativo_operado:
                quantidade_atual = float(ativo['free'])

        quantidade_ajustada = ajusta_quantidade(quantidade_atual, min_qty, max_qty, step_size)

        if quantidade_ajustada is None:
            print(f"Erro: Quantidade disponível ({quantidade_atual}) não é válida para venda.")
            return posicao

        quantidade_truncada = truncar_quantidade(quantidade_ajustada, step_size)

        if preco_compra:
            lucro_percentual = ((preco_atual - preco_compra) / preco_compra) * 100
            print(
                colored(
                    f"Lucro/Perca: {lucro_percentual:.2f}% | Preço de Compra: {preco_compra:.2f} | Preço Atual: {preco_atual:.2f}",
                    "green" if lucro_percentual >= 0 else "red"
                )
            )

        executar_ordem("VENDA", ativo_operado, quantidade_truncada, preco_atual)
        posicao = False  # Atualiza a posição para indicar que o ativo foi vendido

    return posicao

# INFORMAÇÕES DO ATIVO - Configurações principais
codigo_ativo = 'ETHUSDT'
ativo_operado = 'ETH'
periodo_candle = Client.KLINE_INTERVAL_1HOUR
valor_dolares = 57
modo_teste = True
posicao_atual = False

while True:
    print("Atualizando dados e avaliando estratégia...")
    dados_atualizados = pegando_dados(codigo_ativo, periodo_candle)
    posicao_atual = estrategia_trade(dados_atualizados, codigo_ativo, ativo_operado, valor_dolares, posicao_atual)
    print("Aguardando próximo ciclo...\n")
    time.sleep(60)  # Aguarda minuto para o próximo ciclo