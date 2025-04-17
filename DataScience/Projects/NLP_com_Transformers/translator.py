from transformers import pipeline

translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")

# Exemplo: inglês para francês
translation = translator("I'm a brazilian student of FIAP.", max_length=40)

print(translation)