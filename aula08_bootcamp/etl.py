import pandas as pd
import os
import glob

# FUNÇÃO DE EXTRACT QUE LE E CONSOLIDA OS JSON
def extrair_dados_e_consolidar(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df = pd.concat(df_list, ignore_index=True)

    return df

# FUNÇÃO DE TRANSFORMAÇÃO 
def calvular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df['Total'] = df['Quantidade'] * df['Venda']

    return df


# FUNÇÃO DE CARREGAMENTO DE DADOS
# Paramentro que vai ser 'csv' ou 'parquet' ou 'os dois
def carregar_dados(df: pd.DataFrame, format_saida: list):
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv('dados_consolidados.csv', index=False)
        if formato == 'parquet':
            df.to_parquet('dados_consolidados.parquet', index=False)


def pipeline_calcular_kpi_de_vendas_consolidados(pasta: str, formato_de_saida: list):
    df = extrair_dados_e_consolidar(pasta)
    df_calculado = calvular_kpi_de_total_de_vendas(df)
    carregar_dados(df_calculado, formato_de_saida)



if __name__ == '__main__':
    pass