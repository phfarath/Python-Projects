# 1. gerar número aleatório de X digitos 

# 2. estrutura de repetição

# 3. entrada para adivinhação do número

# 4. tratamento de possíveis inputs indesejados 

# 5. exibição da tentativa 

# 6. se correto, fim do jogo

import random

# quantidade de numeros desejada 
x = 5

# criando uma lista com x numeros aleatorios ('_' é uma variavel apenas para criar a lista, não iremos usá-la)
adivinha = [str(random.randint(0, 9)) for _ in range(x)]
adivinha_tentativas = [('_') for _ in range(x)]

tentativa = []

# enquanto verdade
while True:
    tentativa = input(f'Digite um número de {x} dígitos: ')

    # tratamento de inputs indesejados como menores que x e letras
    if len(tentativa) != x or not tentativa.isdigit():
        print(f'\033[91mDigite {x} números válidos!\033[0m')
        continue

    # convertendo para lista
    tentativa = list(tentativa)

    # print da sua tentativa
    print('------------------------------')
    print('Sua tentativa é : ')
    print(tentativa)
    print('------------------------------')

    # se o numero for correto, preenche a lista adivinha_tentativas com seu index, mantendo a posição correta
    for index, numero in enumerate(tentativa): 
        if numero == adivinha[index]:
            adivinha_tentativas[index] = numero

    # exibição dos números corretos da tentativa
    print(f'Números corretos: {adivinha_tentativas}') 

    # caso a tentativa esteja correta
    if adivinha_tentativas == adivinha:
        print('\033[92mVocê acertou! Parabéns!\033[0m')
        break # fim do programa 