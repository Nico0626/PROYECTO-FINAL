import random
import aritmetica

def generar_operacion():
    operaciones = ['+', '-', '*', '/']
    operacion = random.choice(operaciones)
    numero1 = round(random.uniform(-100, 100), 2)
    numero2 = round(random.uniform(-100, 100), 2)

    if operacion == '/':
        while numero2 == 0:
            numero2 = round(random.uniform(-100, 100), 2)
    
    return numero1, numero2, operacion

def calcular_resultado(numero1, numero2, operacion):
    if operacion == '+':
        return aritmetica.sumar(numero1, numero2)
    elif operacion == '-':
        return aritmetica.restar(numero1, numero2)
    elif operacion == '*':
        return aritmetica.multiplicar(numero1, numero2)
    elif operacion == '/':
        return aritmetica.dividir(numero1, numero2)

def resolver_captcha():
    while True:
        numero1, numero2, operacion = generar_operacion()
        resultado_correcto = calcular_resultado(numero1, numero2, operacion)
        
        print(f"Resuelve la siguiente operación aritmética: {numero1} {operacion} {numero2}")
        
        try:
            respuesta_usuario = float(input("Ingresa el resultado (con dos dígitos decimales): "))
        except ValueError:
            print("Entrada inválida. Inténtalo de nuevo.")
            continue
        
        if round(respuesta_usuario, 2) == round(resultado_correcto, 2):
            print("¡Captcha resuelto correctamente!")
            return True
        else:
            print(f"Respuesta incorrecta. El resultado correcto era {round(resultado_correcto, 2)}.")
            opcion = input("¿Quieres intentar de nuevo? (s/n): ")
            if opcion.lower() != 's':
                print("Registro cancelado.")
                return False

if __name__ == '__main__':
    resolver_captcha()