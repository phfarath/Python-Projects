# Importação das bibliotecas necessárias
# requests: Para fazer requisições HTTP e buscar o conteúdo das páginas
# BeautifulSoup: Para interpretar e extrair dados do HTML de forma estruturada
# time: Para incluir pequenos intervalos entre requisições e evitar sobrecarregar servidores
# urljoin: Para converter URLs relativas em absolutas
# logging: Para registrar mensagens e acompanhar o funcionamento do crawler
# deque: Para usar uma fila eficiente, permitindo um rastreamento organizado das páginas

import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin
import logging
from collections import deque

# Classe principal do Web Crawler
class RastreadorWeb:
    def __init__(self, sementes, atraso=1):
        """
        Inicializa o rastreador com configurações básicas.

        Args:
            sementes (list): Lista de URLs iniciais para começar o rastreamento.
            atraso (int): Tempo de espera (em segundos) entre cada requisição para evitar sobrecarga.
        """
        self.sementes = sementes  # URLs iniciais do rastreamento
        self.atraso = atraso  # Tempo de espera entre requisições
        self.visitados = set()  # Conjunto para armazenar as URLs já visitadas
        self.fila = deque(sementes)  # Fila de URLs a serem processadas
        self.sessao = requests.Session()  # Sessão HTTP reutilizável para eficiência
        self.sessao.headers = {'User-Agent': 'PythonCrawler/1.0'}  # Identificação do crawler para evitar bloqueios

        # Configuração do sistema de logging para registrar o andamento do rastreamento
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.registrador = logging.getLogger(__name__)

    def respeita_robots_txt(self, url):
        """ 
        Verifica se o site permite o rastreamento, consultando o arquivo robots.txt.

        Args:
            url (str): URL do site que será verificado.

        Returns:
            bool: Retorna True se o rastreamento for permitido, False caso contrário.
        """
        try:
            url_robots = urljoin(url, '/robots.txt')  # Monta a URL do robots.txt
            resposta = self.sessao.get(url_robots)  # Faz a requisição para obter o conteúdo do arquivo
            
            # Se o arquivo indicar "Disallow: /", o site proíbe o rastreamento
            return 'Disallow: /' not in resposta.text  
        except:
            # Se houver erro ao acessar o robots.txt, assume-se que o rastreamento é permitido
            return True

    def extrai_links(self, sopa, url_base):
        """
        Encontra e extrai todos os links da página atual.

        Args:
            sopa (BeautifulSoup): Objeto contendo o HTML da página.
            url_base (str): URL da página de onde os links estão sendo extraídos.

        Returns:
            list: Lista de URLs encontradas na página.
        """
        links = []
        for link in sopa.find_all('a'):  # Busca todas as tags <a> (links)
            href = link.get('href')  # Obtém o atributo href (endereço do link)
            if href:
                # Converte URLs relativas em URLs absolutas para evitar links quebrados
                url_absoluta = urljoin(url_base, href)
                links.append(url_absoluta)
        return links

    def rastrear(self, max_paginas=100):
        """
        Inicia o processo de rastreamento, visitando páginas e extraindo links.

        Args:
            max_paginas (int): Número máximo de páginas a serem visitadas.
        """
        paginas_rastreadas = 0  # Contador de páginas visitadas

        while self.fila and paginas_rastreadas < max_paginas:
            url = self.fila.popleft()  # Pega a próxima URL da fila

            if url in self.visitados:  # Se a URL já foi visitada, pula para a próxima
                continue

            try:
                # Verifica se o rastreamento é permitido pelo robots.txt do site
                if not self.respeita_robots_txt(url):
                    self.registrador.warning(f"Rastreamento bloqueado pelo robots.txt: {url}")
                    continue

                self.registrador.info(f"Acessando: {url}")  # Exibe a URL sendo acessada no log
                
                resposta = self.sessao.get(url, timeout=10)  # Faz a requisição HTTP para obter a página
                self.visitados.add(url)  # Adiciona a URL ao conjunto de páginas visitadas
                paginas_rastreadas += 1  # Incrementa o contador de páginas processadas

                if resposta.status_code == 200:  # Se a requisição foi bem-sucedida
                    sopa = BeautifulSoup(resposta.text, 'html.parser')  # Converte o HTML em um objeto manipulável
                    
                    # Aqui é possível processar o conteúdo da página (extrair textos, imagens, etc.)

                    # Coleta os links encontrados e adiciona os novos na fila de rastreamento
                    novos_links = self.extrai_links(sopa, url)
                    for link in novos_links:
                        if link not in self.visitados:
                            self.fila.append(link)

                time.sleep(self.atraso)  # Aguarda um pouco antes da próxima requisição

            except Exception as e:
                self.registrador.error(f"Erro ao acessar {url}: {str(e)}")  # Registra erros no log

        self.registrador.info(f"Rastreamento concluído! Total de páginas visitadas: {paginas_rastreadas}")  # Mensagem final do rastreamento

# Execução do crawler (exemplo de uso)
if __name__ == "__main__":
    # Lista de sites para iniciar o rastreamento
    sementes = [
        "https://exemplo.com",
        "https://outroexemplo.com"
    ]

    # Cria uma instância do rastreador e inicia o rastreamento com um limite de 50 páginas
    rastreador = RastreadorWeb(sementes)
    rastreador.rastrear(max_paginas=50)
