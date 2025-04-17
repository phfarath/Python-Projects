import pygame
import time
import random

# INICIALIZANDO
pygame.init()

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (213, 50, 80)
VERDE = (0, 255, 0)

# DEFININDO O TAMANHO DA JANELA
LARGURA = 600
ALTURA = 400
tela = pygame.display.set_mode((LARGURA, ALTURA))

# VELOCIDADE DO JOGO
clock = pygame.time.Clock()

# Tamanho dos blocos do jogo
BLOCO = 20

# Velocidade inicial da cobra
velocidade = 14

def jogo():
    fim_de_jogo = False
    cobra_viva = True
    pygame.display.set_caption('SNAKE GAME')

    # POSIÇÃO INICIAL DA COBRA
    x = LARGURA // 2
    y = ALTURA // 2
    x_mudanca = 0
    y_mudanca = 0

    # TAMANHO DA COBRA 
    corpo_cobra = []
    tamanho_cobra = 1

    comida_x = round(random.randrange(0, LARGURA - BLOCO) / BLOCO) * BLOCO
    comida_y = round(random.randrange(0, ALTURA - BLOCO) / BLOCO) * BLOCO

    while not fim_de_jogo:
        while not cobra_viva:
            # GAME OVER
            tela.fill(PRETO)
            fonte = pygame.font.SysFont(None, 23)
            msg_game_over = fonte.render("Game Over! Pressione E para jogar de novo ou Q para sair", True, VERMELHO)
            tela.blit(msg_game_over, [LARGURA // 6, ALTURA // 3])
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        fim_de_jogo = True
                        cobra_viva = True
                    if evento.key == pygame.K_e:
                        jogo()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_de_jogo = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_a:
                    x_mudanca = -BLOCO
                    y_mudanca = 0
                elif evento.key == pygame.K_d:
                    x_mudanca = BLOCO
                    y_mudanca = 0
                elif evento.key == pygame.K_w:
                    x_mudanca = 0
                    y_mudanca = -BLOCO
                elif evento.key == pygame.K_s:
                    x_mudanca = 0
                    y_mudanca = BLOCO

        # ATUALIZA A POSIÇÃO DA COBRA
        x += x_mudanca
        y += y_mudanca

        # VERIFICAÇÃO PARA A COBRA NÃO SAIR DA TELA
        if x >= LARGURA or x < 0 or y >= ALTURA or y < 0:
            cobra_viva = False

        # DESENHO DA COBRA E DA COMIDA
        tela.fill(PRETO)
        pygame.draw.rect(tela, VERMELHO, [comida_x, comida_y, BLOCO, BLOCO])
        cabeca_cobra = []
        cabeca_cobra.append(x)
        cabeca_cobra.append(y)
        corpo_cobra.append(cabeca_cobra)
        if len(corpo_cobra) > tamanho_cobra:
            del corpo_cobra[0]

        # Verificar se a cobra colidiu com o próprio corpo
        for bloco in corpo_cobra[:-1]:
            if bloco == cabeca_cobra:
                cobra_viva = False

        # Desenhar cada bloco do corpo da cobra
        for bloco in corpo_cobra:
            pygame.draw.rect(tela, VERDE, [bloco[0], bloco[1], BLOCO, BLOCO])

        pygame.display.update()

        # Verificar se a cobra comeu a comida
        if abs(x - comida_x) < BLOCO and abs(y - comida_y) < BLOCO:
            comida_x = round(random.randrange(0, LARGURA - BLOCO) / BLOCO) * BLOCO
            comida_y = round(random.randrange(0, ALTURA - BLOCO) / BLOCO) * BLOCO
            tamanho_cobra += 1

        # Definir a velocidade do jogo
        clock.tick(velocidade)

    pygame.quit()
    quit()

# Iniciar o jogo
jogo()