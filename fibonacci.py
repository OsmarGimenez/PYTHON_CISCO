'''Esta funcion tiene como objetivo reproducir una secuencia de numeros Fibonacci'''
# funcion fib de fibonacci
# n => numero

def fib(n):
    if n < 1:
        return 'Ingresa un numero valido'
    if n < 3:
        return 1
    
    elem_1 = elem_2 = 1
    suma = 0
    for i in range(3,n+1):
        suma = elem_1 + elem_2
        elem_1,elem_2 = elem_2, suma

    return suma

for n in range(1,10):
    print(n,'=>', fib(n))