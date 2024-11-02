def sumar(a, b):
    return float(a + b)

def restar(a, b):
    return float(a - b)

def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre 0")
    else:
        return float(a / b)

def multiplicar(a, b):
    return float(a * b)

def sumar_n(*args):
    return float(sum(args))

def promedio_n(*args):
    return float(sumar_n(*args) / len(args))
