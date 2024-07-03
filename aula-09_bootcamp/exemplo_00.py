from sys import stderr
from loguru import logger


# # Configuração do logger para exibir logs no stderr e salvar em arquivo, com filtragem e formatação específicas
logger.add(
    sink=stderr,
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="INFO"
)

logger.add(
    "meu_arquivo_de_logs.log",  # Arquivo onde os logs serão salvos
    format="{time} {level} {message} {file}",
    level="INFO"
)

logger.add(
    "meu_arquivo_de_logs.log",  # Arquivo onde os logs serão salvos
    format="{time} {level} {message} {file}",
    level="CRITICAL"
)

# Exemplo de uso do logger
logger.info("Este é um log de informação.")
logger.error("Este é um log de erro.")


def soma(x, y):

    try:
        soma = x + y
        logger.info(f'Somando {x} e {y}')
        return soma
    except:
        logger.critical('Você tem que digitar valores corretos')


soma(2, 3)
soma(5, 7)
soma(2, '3')
