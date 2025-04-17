import pygame
import random
import sys
from pygame.locals import *

# Inicialização do Pygame
pygame.init()

# Configurações da tela
LARGURA = 1024
ALTURA = 768
TAMANHO_BLOCO = 50

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0) 
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)
CINZA = (128, 128, 128)
ROXO = (128, 0, 128)

# Configuração da janela
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('🎲 Mario Party Python')
relogio = pygame.time.Clock()

# Carregando fontes
fonte_titulo = pygame.font.Font(None, 72)
fonte_texto = pygame.font.Font(None, 36)
fonte_status = pygame.font.Font(None, 28)

class Jogador:
    def __init__(self, x, y, cor, nome):
        self.x = x
        self.y = y
        self.cor = cor
        self.nome = nome
        self.moedas = 0
        self.estrelas = 0
        self.posicao_tabuleiro = 0
        self.animando = False
        self.destino_x = x
        self.destino_y = y
        self.velocidade = 5
        
    def mover(self, dados):
        self.posicao_tabuleiro = (self.posicao_tabuleiro + dados) % 20
        self.destino_x = tabuleiro[self.posicao_tabuleiro][0]
        self.destino_y = tabuleiro[self.posicao_tabuleiro][1]
        self.animando = True
        
    def atualizar(self):
        if self.animando:
            dx = self.destino_x - self.x
            dy = self.destino_y - self.y
            dist = (dx**2 + dy**2)**0.5
            
            if dist < self.velocidade:
                self.x = self.destino_x
                self.y = self.destino_y
                self.animando = False
            else:
                self.x += (dx/dist) * self.velocidade
                self.y += (dy/dist) * self.velocidade
        
    def desenhar(self):
        pygame.draw.circle(tela, self.cor, (int(self.x), int(self.y)), 18)
        pygame.draw.circle(tela, BRANCO, (int(self.x), int(self.y)), 18, 2)

class Tabuleiro:
    def __init__(self):
        self.espacos = []
        self.tipos = []  # 0: normal, 1: moeda, 2: estrela
        self.gerar_tabuleiro()
        
    def gerar_tabuleiro(self):
        x = LARGURA//4
        y = ALTURA//4
        for i in range(20):
            if i < 5:
                self.espacos.append((x, y))
                x += TAMANHO_BLOCO * 1.5
            elif i < 10:
                self.espacos.append((x, y))
                y += TAMANHO_BLOCO * 1.5
            elif i < 15:
                self.espacos.append((x, y))
                x -= TAMANHO_BLOCO * 1.5
            else:
                self.espacos.append((x, y))
                y -= TAMANHO_BLOCO * 1.5
            
            # Define aleatoriamente o tipo do espaço
            tipo = random.choices([0, 1, 2], weights=[0.6, 0.3, 0.1])[0]
            self.tipos.append(tipo)
                
    def desenhar(self):
        for i, espaco in enumerate(self.espacos):
            cor = BRANCO if self.tipos[i] == 0 else AMARELO if self.tipos[i] == 1 else ROXO
            pygame.draw.rect(tela, cor, (espaco[0]-25, espaco[1]-25, 50, 50))
            pygame.draw.rect(tela, BRANCO, (espaco[0]-25, espaco[1]-25, 50, 50), 2)

def jogar_dados():
    return random.randint(1, 6)

def exibir_status(jogadores, jogador_atual):
    y = 20
    for i, jogador in enumerate(jogadores):
        cor_fundo = CINZA if i == jogador_atual else PRETO
        pygame.draw.rect(tela, cor_fundo, (10, y-5, 300, 30))
        texto = f"{jogador.nome}: {jogador.moedas}🪙 {jogador.estrelas}⭐"
        superficie = fonte_status.render(texto, True, jogador.cor)
        tela.blit(superficie, (20, y))
        y += 40

def exibir_mensagem(mensagem, y=ALTURA//2):
    superficie = fonte_titulo.render(mensagem, True, BRANCO)
    rect = superficie.get_rect(center=(LARGURA//2, y))
    tela.blit(superficie, rect)

# Criação do tabuleiro
tabuleiro_jogo = Tabuleiro()
tabuleiro = tabuleiro_jogo.espacos

# Criação dos jogadores
jogadores = [
    Jogador(tabuleiro[0][0], tabuleiro[0][1], VERMELHO, "Mario"),
    Jogador(tabuleiro[0][0], tabuleiro[0][1], AZUL, "Luigi"),
    Jogador(tabuleiro[0][0], tabuleiro[0][1], VERDE, "Yoshi"),
    Jogador(tabuleiro[0][0], tabuleiro[0][1], AMARELO, "Wario")
]

jogador_atual = 0
turno = 0
rodada = 1
dados_valor = 0
mensagem_evento = ""
tempo_mensagem = 0

# Loop principal do jogo
while True:
    tempo_atual = pygame.time.get_ticks()
    
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
            
        if evento.type == KEYDOWN:
            if evento.key == K_SPACE and turno == 0 and not any(j.animando for j in jogadores):
                # Jogada dos dados
                dados_valor = jogar_dados()
                mensagem_evento = f"Dados: {dados_valor}"
                tempo_mensagem = tempo_atual + 2000
                jogadores[jogador_atual].mover(dados_valor)
                turno = 1
    
    # Atualização dos jogadores
    for jogador in jogadores:
        jogador.atualizar()
    
    # Verificação de eventos após movimento
    if turno == 1 and not jogadores[jogador_atual].animando:
        pos = jogadores[jogador_atual].posicao_tabuleiro
        if tabuleiro_jogo.tipos[pos] == 1:  # Espaço de moeda
            jogadores[jogador_atual].moedas += random.randint(1, 3)
            mensagem_evento = f"{jogadores[jogador_atual].nome} ganhou moedas!"
        elif tabuleiro_jogo.tipos[pos] == 2:  # Espaço de estrela
            if jogadores[jogador_atual].moedas >= 20:
                jogadores[jogador_atual].estrelas += 1
                jogadores[jogador_atual].moedas -= 20
                mensagem_evento = f"{jogadores[jogador_atual].nome} comprou uma estrela!"
        
        tempo_mensagem = tempo_atual + 2000
        jogador_atual = (jogador_atual + 1) % 4
        if jogador_atual == 0:
            rodada += 1
        turno = 0
        
        if rodada > 20:
            vencedor = max(jogadores, key=lambda x: (x.estrelas, x.moedas))
            mensagem_evento = f"Fim do jogo! {vencedor.nome} venceu!"
            pygame.display.flip()
            pygame.time.wait(5000)
            pygame.quit()
            sys.exit()
    
    # Desenho
    tela.fill(PRETO)
    
    # Desenha título do jogo
    titulo = fonte_titulo.render("Mario Party Python", True, BRANCO)
    tela.blit(titulo, (LARGURA//2 - titulo.get_width()//2, 20))
    
    tabuleiro_jogo.desenhar()
    for jogador in jogadores:
        jogador.desenhar()
    exibir_status(jogadores, jogador_atual)
    
    # Exibe mensagens de evento
    if tempo_atual < tempo_mensagem:
        exibir_mensagem(mensagem_evento, ALTURA - 100)
    
    # Exibe instruções
    if not any(j.animando for j in jogadores):
        instrucao = fonte_texto.render("Pressione ESPAÇO para jogar os dados", True, BRANCO)
        tela.blit(instrucao, (LARGURA//2 - instrucao.get_width()//2, ALTURA - 50))
    
    # Atualização da tela
    pygame.display.flip()
    relogio.tick(60)
