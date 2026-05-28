import json
import pandas as pd

def limpar_dados_kabum(sopa):
    """
    Recebe o HTML parseado, busca o JSON oculto e retorna um DataFrame do Pandas.
    """
    print("[TRANSFORM] Iniciando processamento dos dados...")
    scripts_ocultos = sopa.find_all('script', type='application/ld+json')
    lista_de_placas = []
    
    for script in scripts_ocultos:
        if "ItemList" in script.text or "Product" in script.text:
            try:
                dados_json = json.loads(script.text)
                for item in dados_json:
                    if item.get("@type") == "Product":
                        nome = item.get("name")
                        ofertas = item.get("offers", {})
                        
                        if isinstance(ofertas, dict):
                            preco = ofertas.get("price")
                            
                        if nome and preco:
                            lista_de_placas.append({
                                "Produto": nome, 
                                "Preço (R$)": float(preco)
                            })
                break
            except json.JSONDecodeError:
                pass
                
    if len(lista_de_placas) > 0:
        df = pd.DataFrame(lista_de_placas)
        print(f"[TRANSFORM] Tabela gerada com {len(df)} produtos.")
        return df
    else:
        print("[TRANSFORM - ALERTA] Nenhum dado encontrado.")
        return None