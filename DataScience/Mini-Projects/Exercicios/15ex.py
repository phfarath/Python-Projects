# Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de papel [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Com esses valores, faça um programa que calcule a média de gastos. Dica: use as funções built-in sum() e len().

lista_compras = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

def media_lista(lista):
    soma = 0

    for item in lista:
        soma += item

    media = soma / len(lista)
    return media

# print(media_lista(lista_compras))

# -------------------------------------------------------------------------
#  Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.

def conta_acima(lista, num):
    contador = 0
    for item in lista:
        if item >= num:
            contador += 1
    return contador 

porcentagem_por_item = 100/len(lista_compras)
porcentagem_acima_3000 = porcentagem_por_item * conta_acima(lista_compras, 3000)

# print(porcentagem_acima_3000)
#--------------------------------------------------------------------------
# Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].
import random

lista_numeros = []

def adiciona_numeros(quant_numeros, min, max, lista):
    for i in range(1, quant_numeros + 1):
        num = random.randint(min, max)
        lista.append(num)

adiciona_numeros(5, 1, 9, lista_numeros)
# print(lista_numeros)
#--------------------------------------------------------------------------
# Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.
lista_num2 = []

adiciona_numeros(5, 1, 9, lista_num2)

def inverte_lista(lista):
    lista = lista[::-1]
    return lista

# print(lista_num2)
# print(inverte_lista(lista_num2))
#--------------------------------------------------------------------------
# Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.
lista_primos = []

def verifica_primo(num):
    pass
#--------------------------------------------------------------------------
# Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise. 

import datetime
# dia = int(input('Digite o dia de hoje: '))
# mes = int(input('Digite o mes de hoje: '))
# ano = int(input('Digite o ano atual: '))

# try:
#     data = datetime.date(ano, mes, dia)
#     print(data)
# except ValueError:
#     print('Essa data não é válida!')

#--------------------------------------------------------------------------
# Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias por dia (em milhares) e pode ser observado a seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do dia anterior.

lista_num_bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]
dic_percentual = {}

def percentual_crescimento(atual, passado):
    calculo = 100 * (atual - passado) / passado
    return calculo 

dia = 1
for i in range(1, len(lista_num_bacterias)):
    pc = percentual_crescimento(lista_num_bacterias[i], lista_num_bacterias[i-1])
    dic_percentual[f'Dia {dia}'] = pc
    dia += 1

# print(dic_percentual)

#--------------------------------------------------------------------------
# Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.

dic_ID = {}

for i in range (1, 11):
    id = random.randint(1,999)
    if id % 2 != 0:
        dic_ID[f'{id}'] = 'Amargo'
    else:
        dic_ID[f'{id}'] = 'Doce'

def conta_produtos(dic, tipo):
    cont = 0
    for valor in dic.values():
        if valor == tipo:
            cont += 1
    return cont

# print(dic_ID.items())
# print('Amargos: ', conta_produtos(dic_ID, 'Amargo'))  
# print('Doces: ', conta_produtos(dic_ID, 'Doce'))   
#--------------------------------------------------------------------------
# Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.
lista_gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
lista_resposta = []

# for i in range(1, len(lista_gabarito) + 1):
    # escolha = input('Digite a resposta da questão: ').capitalize()
    # lista_resposta.append(escolha)

# def conta_pontos(resposta, gabarito):
#     pontos = 0
#     for j in range(0, len(resposta)):
#         if resposta[j] == gabarito[j]:
#             pontos += 1
#     return pontos

# print(f'Você acertou {conta_pontos(lista_resposta, lista_gabarito)} questões!')
#--------------------------------------------------------------------------
# Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).
lista_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
lista_temp_meses = []

for i in range(0, len(lista_meses)):
    temp = random.randint(8, 39)
    lista_temp_meses.append(temp)

def media_anual(lista_temp):
    soma = 0
    for i in lista_temp:
        soma += i
    media_anual = soma / 12
    return media_anual

# for j in range(0, len(lista_temp_meses)):
#     if lista_temp_meses[j] > media_anual(lista_temp_meses):
#         print(lista_meses[j])


#--------------------------------------------------------------------------
# Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:
# {'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
#  'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
# Escreva um código que calcule o total de vendas e o produto mais vendido.

dic_vendas = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60, 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

def calcula_total(vendas):
    total_vendas = 0
    for i in vendas.values():
        total_vendas += i
    return total_vendas

def calcula_maior_venda(vendas):
    maior_venda = 0 
    for i in vendas.values():
        if i > maior_venda:
            maior_venda = i
    return maior_venda

# print(calcula_total(dic_vendas))
# print(calcula_maior_venda(dic_vendas))
#--------------------------------------------------------------------------
# Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças. A pesquisa foi feita e o votos computados podem ser observados abaixo:
'''
Tabela de votos da marca
Design 1 - 1334 votos
Design 2 - 982 votos
Design 3 - 1751 votos
Design 4 - 210 votos
Design 5 - 1811 votos
'''
# Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, informe o design vencedor e a porcentagem de votos recebidos.

dic_votos = {'Design 1': 1334, 'Design 2': 982, 'Design 3': 1751, 'Design 4': 210, 'Design 5': 1811}

def vencedor_porcentagem(votos):
    mais_votado = ''
    maior_voto = 0
    soma_votos = 0

    for key, value in votos.items():
        soma_votos += value
        if value > maior_voto:
            maior_voto = value
            mais_votado = key

    porcentagem_mais_votado = (maior_voto * 100)/soma_votos
    return mais_votado, porcentagem_mais_votado
    
# print(vencedor_porcentagem(dic_votos))
#--------------------------------------------------------------------------
# As pessoas colaboradoras de um setor da empresa que você trabalha vão receber um abono correspondente a 10% do salário devido ao ótimo desempenho do time. O setor financeiro solicitou sua ajuda para a verificação das consequências financeiras que esse abono irá gerar nos recursos. Assim, foi encaminhada para você uma lista com os salários que receberão o abono: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. O abono de cada colaborador(a) não pode ser inferior a 200. Em código, transforme cada um dos salários em chaves de um dicionário e o abono de cada salário no elemento. Depois, informe o total de gastos com o abono, quantos(as) colaboradores(as) receberam o abono mínimo e qual o maior valor de abono fornecido.

lista_salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
dic_salario_abono = {}

def adiciona_abono(lista_salarios, dic_abono):
    for item in lista_salarios:
        abono = (item/100) * 10
        if abono < 200:
            abono = 200
        dic_abono[f'{item}'] = abono
    return dic_abono

soma_abonos = 0
maior_abono = 0
quant_de_minimos = 0
for value in adiciona_abono(lista_salarios, dic_salario_abono).values():
    soma_abonos += value
    if value == 200:
        quant_de_minimos += 1
    if value > maior_abono:
        maior_abono = value
    
# print(
#     f'O total de gastos com abono foi de: {soma_abonos}\n', 
#     f'O número de abonos mínimos foi de: {quant_de_minimos}\n', 
#     f'O maior abono foi de: {maior_abono}'
#     )
#--------------------------------------------------------------------------
# Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta. A equipe fez a coleta de informações sobre o número de espécies de plantas e animais em cada área dessa floresta e armazenou essas informações em um dicionário. Nele, a chave descreve a área dos dados e os valores nas listas correspondem às espécies de plantas e animais nas áreas, respectivamente.
# {'Área Norte': [2819, 7236],
#  'Área Leste': [1440, 9492],
#  'Área Sul': [5969, 7496],
#  'Área Oeste': [14446, 49688],
#  'Área Centro': [22558, 45148]}
# Escreva um código para calcular a média de espécies por área e identificar a área com a maior diversidade biológica.

dic_info = {
    'Área Norte': [2819, 7236],
    'Área Leste': [1440, 9492],
    'Área Sul': [5969, 7496],
    'Área Oeste': [14446, 49688],
    'Área Centro': [22558, 45148]
    }

def calcula_media(dic):
    soma_especies = 0
    soma_areas = 0
    for value in dic.values():
        soma_areas += 1
        for item in value:
            soma_especies += item
    media = soma_especies / soma_areas
    return media

def maior_diversidade(dic):
    area_maior_diversidade = ''
    maior_diversidade = 0
    for key, value in dic.items():
        diversidade = 0
        for item in value:
            diversidade += item
        if diversidade > maior_diversidade:
            maior_diversidade = diversidade
            area_maior_diversidade = key
    return area_maior_diversidade

# print(f'A média é de: {calcula_media(dic_info)} espécies por área e a Área com maior diversidade foi a {maior_diversidade(dic_info)}')

#--------------------------------------------------------------------------
# O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as) de 4 setores da empresa. Para isso, foram fornecidos os seguintes dados:
# {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
#  'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
#  'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
#  'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
# Sabendo que cada setor tem 10 colaboradores(as), construa um código que calcule a média de idade de cada setor, a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.

dic_colab = {
    'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
    'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
    'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
    'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
    }

soma_maiores_da_media = 0

for key, value in dic_colab.items():
    soma_idades = sum(value)
    # print(f'A média do setor {key} é {soma_idades/10}')

def calcula_media_geral_idade(dic):
    soma_tudo = 0
    num_de_colaboradores = 0
    for value in dic.values():
        soma_tudo += sum(value)
        num_de_colaboradores += len(value)
    media_geral = soma_tudo/num_de_colaboradores
    return media_geral

for lista in dic_colab.values():
    for colab in lista:
        if colab > calcula_media_geral_idade(dic_colab):
            soma_maiores_da_media += 1

# print(f'A média geral é de: {calcula_media_geral_idade(dic_colab)}')
# print(f'O número de pessoas acima da média é de: {soma_maiores_da_media}')