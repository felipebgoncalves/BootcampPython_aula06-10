from etl import filtar_produtos_nao_entregues, ler_csv, somar_valores_dos_produtos

path_arquivo = 'vendas.csv'

lista_de_produtos = ler_csv(path_arquivo)
produtos_nao_entregues = filtar_produtos_nao_entregues(lista_de_produtos)
valores_dos_produtos_nao_entregues = somar_valores_dos_produtos(produtos_nao_entregues)
print(f' R$ {valores_dos_produtos_nao_entregues}')