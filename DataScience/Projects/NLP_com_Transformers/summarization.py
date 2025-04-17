from transformers import pipeline

# pipeline de sumarização
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

text = """A inteligência artificial é uma área da ciência da computação que se dedica à criação de sistemas capazes de simular a inteligência humana. 
Esses sistemas são projetados para realizar tarefas que normalmente exigiriam intervenção humana, como reconhecimento de voz, tomada de decisões e tradução de idiomas."""

summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
print(summary[0]['summary_text'])