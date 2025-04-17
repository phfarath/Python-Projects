import os
from pytube import YouTube
from moviepy import AudioFileClip

class MusicDownloader:
    def __init__(self):
        """
        Inicializa o downloader de músicas
        """
        self.download_path = "downloads"
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)

    def baixar_musica(self, url):
        """
        Baixa uma música do YouTube e converte para MP3
        
        Args:
            url (str): URL do vídeo do YouTube
        
        Returns:
            str: Caminho do arquivo MP3 baixado
        """
        try:
            # Cria objeto YouTube
            yt = YouTube(url)
            
            # Pega apenas o áudio do vídeo
            video = yt.streams.filter(only_audio=True).first()
            
            # Baixa o arquivo
            print(f"Baixando: {yt.title}")
            arquivo_baixado = video.download(self.download_path)
            
            # Converte para MP3
            nome_base = os.path.splitext(arquivo_baixado)[0]
            novo_arquivo = nome_base + '.mp3'
            
            video_clip = AudioFileClip(arquivo_baixado)
            video_clip.write_audiofile(novo_arquivo)
            
            # Remove o arquivo original
            os.remove(arquivo_baixado)
            video_clip.close()
            
            print(f"Download concluído: {yt.title}")
            return novo_arquivo
            
        except Exception as e:
            print(f"Erro ao baixar música: {str(e)}")
            return None

    def baixar_playlist(self, urls):
        """
        Baixa várias músicas de uma lista de URLs
        
        Args:
            urls (list): Lista de URLs do YouTube
        
        Returns:
            list: Lista com os caminhos dos arquivos MP3 baixados
        """
        arquivos_baixados = []
        for url in urls:
            arquivo = self.baixar_musica(url)
            if arquivo:
                arquivos_baixados.append(arquivo)
        return arquivos_baixados

# Exemplo de uso
if __name__ == "__main__":
    downloader = MusicDownloader()
    
    # Baixar uma música
    url = "https://www.youtube.com/watch?v=kCmibjt_kTQ"
    arquivo = downloader.baixar_musica(url)
    
    # Baixar várias músicas
    # urls = [
    #     "https://www.youtube.com/watch?v=exemplo1",
    #     "https://www.youtube.com/watch?v=exemplo2"
    # ]
    # arquivos = downloader.baixar_playlist(urls)
