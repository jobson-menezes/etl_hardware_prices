import sqlalchemy as sa
import pandas as pd
from datetime import datetime

def carregar_dados_sqlite(df, nome_tabela="historico_precos"):
    """
    Recebe um DataFrame do Pandas e salva em um banco de dados SQLite local.
    """
    if df is None or df.empty:
        print("[LOAD - ALERTA] Não há dados para salvar no banco.")
        return

    print("[LOAD] Iniciando conexão com o banco de dados SQLite...")
    
   
    df['Data_Coleta'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    
    engine = sa.create_engine('sqlite:///hardware_db.sqlite')

    try:
        
        df.to_sql(nome_tabela, con=engine, index=False, if_exists='append')
        print(f"[LOAD] Sucesso! {len(df)} registros foram salvos permanentemente na tabela '{nome_tabela}'.")
    except Exception as erro:
        print(f"[LOAD - ERRO] Falha ao salvar no banco de dados: {erro}")