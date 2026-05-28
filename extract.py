import requests
from bs4 import BeautifulSoup

def extrair_dados_hardware(url):
    """
    Acessa a URL e retorna o HTML parseado (BeautifulSoup).
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    print(f"[EXTRACT] Iniciando extração da URL: {url}")
    
    try:
        resposta = requests.get(url, headers=headers)
        resposta.raise_for_status() 
        print("[EXTRACT] HTML baixado com sucesso.")
        return BeautifulSoup(resposta.text, 'html.parser')

    except requests.exceptions.RequestException as erro:
        print(f"[EXTRACT - ERRO] Falha na conexão: {erro}")
        return None