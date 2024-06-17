# Ferramentas de NLP na Hugging Face

## Análise de Sentimentos
Serviço que oferece análise de sentimentos usando modelos treinados.
**Exemplo:** Análise de sentimentos de avaliações de produtos em um site de e-commerce para identificar feedbacks positivos e negativos.

## Tradução de Texto
Serviço que oferece tradução automática de texto entre vários idiomas usando modelos de tradução.
**Exemplo:** Tradução automática de conteúdos de um blog para alcançar uma audiência global.

## Resumo de Texto
Serviço que resume automaticamente textos longos.
**Exemplo:** Geração de resumos de artigos científicos para facilitar a leitura e compreensão rápida.

## Resposta a Perguntas
erviço que responde perguntas baseadas em um contexto fornecido.
**Exemplo:** Criação de um chatbot para atendimento ao cliente que pode responder perguntas específicas sobre produtos ou serviços.

## Exemplo de Implementação por Requisições HTTP

### Análise de Sentimentos via HTTP
```python
import requests

# URL da API do Hugging Face para análise de sentimentos
url = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"

api_key = "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"

# Cabeçalhos da requisição
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Dados a serem analisados
data = {
    "inputs": "Eu amei a empresa."
}

# Realizar a requisição POST
response = requests.post(url, headers=headers, json=data)

# Exibir o resultado
print(response.json())
