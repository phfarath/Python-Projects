import whisper

# Carregar o modelo Whisper (pode ser 'tiny', 'base', 'small', 'medium', ou 'large')
model = whisper.load_model("base")

# Caminho do arquivo de áudio
audio_path = "tinywow_Aula 01_74864387.mp3"  # Substitua pelo caminho correto

# Transcrever o áudio
result = model.transcribe(audio_path)

# Salvar transcrição em um arquivo de texto
with open("transcricao.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])

print("Transcrição concluída! O texto foi salvo em 'transcricao.txt'")
