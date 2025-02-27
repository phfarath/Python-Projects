# Importa as bibliotecas necessárias
import pygame  # Para reprodução de áudio
import os  # Para manipulação de arquivos
from tkinter import *  # Para interface gráfica
from tkinter import filedialog, ttk  # Para diálogos de arquivo e widgets modernos
import time  # Para controle de tempo
from mutagen.mp3 import MP3  # Para metadados de arquivos MP3

class MusicPlayer:
    def __init__(self):
        # Inicializa o pygame e o mixer para reprodução de áudio
        pygame.init()
        pygame.mixer.init()
        
        # Configuração da janela principal
        self.janela = Tk()
        self.janela.title('🎵 Reprodutor de Música')
        self.janela.geometry('600x400')
        self.janela.configure(bg='#2C3E50')
        
        # Lista de músicas e índice atual
        self.playlist = []  # Lista que armazena os caminhos das músicas
        self.atual = 0  # Índice da música atual
        self.pausado = False  # Estado de pausa
        
        # Variáveis para controle de volume
        self.volume = DoubleVar(value=70)
        
        # Cria os elementos da interface
        self.criar_widgets()
        
    def criar_widgets(self):
        # Frame principal
        main_frame = Frame(self.janela, bg='#2C3E50')
        main_frame.pack(expand=True, fill=BOTH, padx=20, pady=10)
        
        # Título estilizado
        Label(main_frame, text="Reprodutor de Música", font=('Helvetica', 16, 'bold'), 
              bg='#2C3E50', fg='white').pack(pady=10)
        
        # Frame para informações da música atual
        self.info_frame = Frame(main_frame, bg='#34495E', padx=10, pady=5)
        self.info_frame.pack(fill=X)
        
        self.musica_atual_label = Label(self.info_frame, text="Nenhuma música selecionada",
                                      font=('Helvetica', 10), bg='#34495E', fg='white')
        self.musica_atual_label.pack()
        
        # Barra de progresso
        self.progresso = ttk.Progressbar(main_frame, length=400, mode='determinate')
        self.progresso.pack(pady=10)
        
        # Frame para controles
        frame_controles = Frame(main_frame, bg='#2C3E50')
        frame_controles.pack(pady=10)
        
        # Estilo para botões
        botao_estilo = {'font': ('Helvetica', 12), 'bg': '#3498DB', 'fg': 'white',
                       'width': 8, 'relief': 'flat', 'padx': 10}
        
        # Botões de controle
        Button(frame_controles, text="⏮️", command=self.anterior, **botao_estilo).pack(side=LEFT, padx=5)
        Button(frame_controles, text="▶️", command=self.tocar, **botao_estilo).pack(side=LEFT, padx=5)
        Button(frame_controles, text="⏸️", command=self.pausar, **botao_estilo).pack(side=LEFT, padx=5)
        Button(frame_controles, text="⏹️", command=self.parar, **botao_estilo).pack(side=LEFT, padx=5)
        Button(frame_controles, text="⏭️", command=self.proxima, **botao_estilo).pack(side=LEFT, padx=5)
        
        # Controle de volume
        volume_frame = Frame(main_frame, bg='#2C3E50')
        volume_frame.pack(pady=10)
        
        Label(volume_frame, text="Volume:", bg='#2C3E50', fg='white').pack(side=LEFT)
        volume_slider = ttk.Scale(volume_frame, from_=0, to=100, orient=HORIZONTAL,
                                variable=self.volume, command=self.ajustar_volume)
        volume_slider.pack(side=LEFT, padx=10)
        
        # Frame para lista de músicas
        lista_frame = Frame(main_frame, bg='#34495E', padx=10, pady=10)
        lista_frame.pack(fill=BOTH, expand=True)
        
        # Botão para adicionar músicas
        Button(lista_frame, text="+ Adicionar Músicas", command=self.adicionar_musica,
               bg='#27AE60', fg='white', relief='flat').pack(pady=5)
        
        # Lista de músicas com scrollbar
        self.lista_musicas = Listbox(lista_frame, width=50, bg='#ECF0F1', selectmode=SINGLE,
                                   font=('Helvetica', 9))
        scrollbar = ttk.Scrollbar(lista_frame, orient=VERTICAL, command=self.lista_musicas.yview)
        self.lista_musicas.configure(yscrollcommand=scrollbar.set)
        
        scrollbar.pack(side=RIGHT, fill=Y)
        self.lista_musicas.pack(side=LEFT, fill=BOTH, expand=True)
        
        # Bind para duplo clique na lista
        self.lista_musicas.bind('<Double-Button-1>', lambda e: self.tocar_selecionada())
        
    def ajustar_volume(self, *args):
        volume = self.volume.get() / 100
        pygame.mixer.music.set_volume(volume)
        
    def tocar_selecionada(self):
        sel = self.lista_musicas.curselection()
        if sel:
            self.atual = sel[0]
            self.tocar()
            
    def adicionar_musica(self):
        arquivos = filedialog.askopenfilenames(filetypes=[("Arquivos MP3", "*.mp3")])
        for arquivo in arquivos:
            self.playlist.append(arquivo)
            nome_musica = os.path.basename(arquivo)
            self.lista_musicas.insert(END, nome_musica)
    
    def tocar(self):
        if self.playlist:
            if not self.pausado:
                pygame.mixer.music.load(self.playlist[self.atual])
                pygame.mixer.music.play()
                self.atualizar_info_musica()
            else:
                pygame.mixer.music.unpause()
                self.pausado = False
    
    def atualizar_info_musica(self):
        nome_musica = os.path.basename(self.playlist[self.atual])
        self.musica_atual_label.config(text=f"Tocando: {nome_musica}")
    
    def pausar(self):
        pygame.mixer.music.pause()
        self.pausado = True
    
    def parar(self):
        pygame.mixer.music.stop()
        self.pausado = False
        self.musica_atual_label.config(text="Nenhuma música selecionada")
    
    def proxima(self):
        if self.atual < len(self.playlist) - 1:
            self.atual += 1
            self.tocar()
    
    def anterior(self):
        if self.atual > 0:
            self.atual -= 1
            self.tocar()
    
    def iniciar(self):
        self.janela.mainloop()

# Ponto de entrada do programa
if __name__ == "__main__":
    player = MusicPlayer()  # Cria uma instância do reprodutor
    player.iniciar()  # Inicia o reprodutor
