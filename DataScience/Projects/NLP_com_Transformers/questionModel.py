from transformers import pipeline

qa_pipeline = pipeline("question-answering")

context = """Hugging Face é uma empresa que fornece ferramentas para trabalhar com processamento de linguagem natural usando transformers."""
question = "O que é a Hugging Face?"

print(qa_pipeline(question=question, context=context))