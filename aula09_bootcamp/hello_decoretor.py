from functools import wraps

def hello(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Isso é um decorador")
        return result
    return wrapper