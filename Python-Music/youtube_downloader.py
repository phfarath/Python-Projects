from pytube import YouTube, exceptions
from pytube.exceptions import PytubeError
import os
import time

class YoutubeDownloader:
    def __init__(self, download_path="downloads"):
        self.download_path = download_path
        if not os.path.exists(self.download_path):
            os.makedirs(self.download_path)

    def download_video(self, url, resolution="720p", max_retries=3):
        retries = 0
        while retries < max_retries:
            try:
                yt = YouTube(
                    url,
                    use_oauth=True,
                    allow_oauth_cache=True
                )
                print(f"Baixando: {yt.title}")
                
                # Try to get stream with specified resolution
                stream = yt.streams.filter(res=resolution, progressive=True).first()
                if stream is None:
                    print(f"Resolução {resolution} não disponível. Baixando a melhor resolução disponível.")
                    stream = yt.streams.filter(progressive=True).get_highest_resolution()
                
                if stream:
                    file_path = stream.download(self.download_path)
                    print(f"Download concluído: {yt.title}")
                    return file_path
                else:
                    print("Nenhum stream disponível para download")
                    return None
                    
            except exceptions.RegexMatchError as e:
                print(f"Erro: URL inválida. {str(e)}")
                return None
            except exceptions.VideoUnavailable as e:
                print(f"Erro: Vídeo indisponível. {str(e)}")
                return None
            except PytubeError as e:
                print(f"Erro PyTube: {str(e)}")
                retries += 1
                if retries < max_retries:
                    print(f"Tentativa {retries} de {max_retries}. Aguardando 5 segundos...")
                    time.sleep(5)
                continue
            except Exception as e:
                print(f"Erro inesperado: {str(e)}")
                retries += 1
                if retries < max_retries:
                    print(f"Tentativa {retries} de {max_retries}. Aguardando 5 segundos...")
                    time.sleep(5)
                continue
        
        print("Número máximo de tentativas atingido. Download falhou.")
        return None

    def download_playlist(self, playlist_url, resolution="720p"):
        try:
            from pytube import Playlist
            playlist = Playlist(playlist_url)
            print(f"Baixando playlist: {playlist.title}")
            file_paths = []
            for url in playlist.video_urls:
                file_path = self.download_video(url, resolution)
                if file_path:
                    file_paths.append(file_path)
            return file_paths
        except Exception as e:
            print(f"Erro ao baixar a playlist: {str(e)}")
            return None

if __name__ == "__main__":
    downloader = YoutubeDownloader()
    
    # Baixar um vídeo
    video_url = "https://www.youtube.com/watch?v=lpxKD_31S9U"
    downloader.download_video(video_url)

# Baixar uma playlist
# playlist_url = "https://www.youtube.com/playlist?list=PL-osiE80TeTtoQ9cBS1jWd-0d6
