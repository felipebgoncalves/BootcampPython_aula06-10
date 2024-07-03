from etl import pipeline_calcular_kpi_de_vendas_consolidados

pasta_argumento: str = 'data'
formato_de_saida: list = ['csv', 'parquet']

pipeline_calcular_kpi_de_vendas_consolidados(pasta=pasta_argumento, formato_de_saida=formato_de_saida)