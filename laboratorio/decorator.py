def decorator(func):
    def metodo(* args, **kwargs):
        print("Antes de")
        print(func(*args, **kwargs))
        print("Despues")
    return metodo

@decorator
def multiplicacion(a, b):
    return a*b

# multiplicacion = decorator(multiplicacion)


