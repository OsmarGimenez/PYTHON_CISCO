'''Esta funcion tiene como objetivo el calculo de factoriales'''

def factorial(numero):
    if numero < 0 :
        return 'Ingresa un numero valido'
    if numero < 2:
        return 1
    producto = 1

    for i in range (2, numero + 1):
        producto *= i
    return producto
    
for n in range (1, 6):
    print(n, factorial(n))