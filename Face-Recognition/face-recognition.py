import cv2
import numpy as np
from datetime import datetime

def detectar_rostos(caminho_imagem=None, fonte_video=0):
    """
    Detecta rostos em imagens ou stream de vídeo usando o OpenCV.
    
    caminho_imagem (str, opcional): Caminho para o arquivo de imagem. Se none, usa stream de vídeo
    fonte_video (int, opcional): indice da câmera para captura de vídeo. padrão -> 0 (webcam)
    """
    # Carrega o classificador pré-treinado de detecção facial
    classificador_facial = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    )
    
    def processar_quadro(quadro):
        # Converte quadro para escala de cinza para detecção facial
        cinza = cv2.cvtColor(quadro, cv2.COLOR_BGR2GRAY)
        
        # Detecta rostos
        rostos = classificador_facial.detectMultiScale(
            cinza,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        
        # Desenha retângulos e informações para cada rosto detectado
        for (x, y, w, h) in rostos:
            # Desenha retângulo ao redor do rosto
            cv2.rectangle(quadro, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            # Adiciona rótulo
            cv2.putText(quadro, 
                       f'Rosto detectado',
                       (x, y - 10),
                       cv2.FONT_HERSHEY_SIMPLEX,
                       0.5,
                       (0, 255, 0),
                       2)
        
        return quadro, len(rostos)
    
    if caminho_imagem:
        # Processa uma única imagem
        imagem = cv2.imread(caminho_imagem)
        if imagem is None:
            raise ValueError("Não foi possível carregar a imagem do caminho fornecido")
        
        imagem_processada, contador_rostos = processar_quadro(imagem)
        
        # Exibe resultados
        cv2.imshow('Deteccao Facial', imagem_processada)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    else:
        # Processamento de vídeo
        captura_video = cv2.VideoCapture(fonte_video)
        
        if not captura_video.isOpened():
            raise ValueError("Não foi possível abrir a fonte de vídeo")
        
        print("Pressione 'q' para sair")
        
        while True:
            ret, quadro = captura_video.read()
            if not ret:
                break
                
            quadro_processado, contador_rostos = processar_quadro(quadro)
            
            # Adiciona contagem de rostos ao quadro
            cv2.putText(quadro_processado,
                       f'Rostos detectados: {contador_rostos}',
                       (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX,
                       1,
                       (0, 255, 0),
                       2)
            
            # Exibe resultados
            cv2.imshow('Detecção Facial', quadro_processado)
            
            # Interrompe loop ao pressionar 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        captura_video.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Processamento de Imagem da webcam principal (fonte_video = 0)
    detectar_rostos()