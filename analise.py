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
