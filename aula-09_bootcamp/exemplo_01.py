from utils_log import log_decorator
from hello_decoretor import hello

@hello
@log_decorator
def soma(x, y):
    return x + y

soma(2, 3)
soma(2, 7)