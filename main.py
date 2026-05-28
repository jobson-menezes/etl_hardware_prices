# Importações
from extract import extrair_dados_hardware
from transform import limpar_dados_kabum
from load import carregar_dados_sqlite 

if __name__ == "__main__":
    print(f"{'='*40}")
    print("🚀 INICIANDO PIPELINE ETL DE HARDWARE")
    print(f"{'='*40}\n")
    
    url_alvo = "https://www.kabum.com.br/busca/placa-de-v%C3%ADdeo-rtx-5060"
    
    # FASE 1: EXTRAÇÃO
    sopa_html = extrair_dados_hardware(url_alvo)
    
    if sopa_html:
        # FASE 2: TRANSFORMAÇÃO
        df_placas = limpar_dados_kabum(sopa_html)
        
        if df_placas is not None:
            print("\n[MAIN] Amostra dos dados:")
            print(df_placas.head())
            print("-" * 50)
            
            # FASE 3: CARREGAMENTO (LOAD)
            print("\n[MAIN] Enviando dados para o banco...")
            carregar_dados_sqlite(df_placas)
            
            print("\n[MAIN] 🎉 Pipeline ETL finalizado com sucesso!")
        else:
            print("\n[MAIN - ERRO] Falha na Transformação.")
    else:
        print("\n[MAIN - ERRO] Falha na Extração.")