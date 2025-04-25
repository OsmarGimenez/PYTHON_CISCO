'''Objetivo de esta funcion es dar un pequeño ejemplo de recursividad
caracteristica importante el POO'''

#La recursividad es una tecnica de programacion donde una funcion se invoca a si misma

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
# esta version de Fibonacci hace uso directo de la recursividad
print(fib(2))

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n - 1)

print(factorial_function(3))