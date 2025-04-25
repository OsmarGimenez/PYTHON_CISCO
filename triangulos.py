'''el objetivo es realizar funciones relacionadas a los triangulos probando calculos geometricos
con el lenguaje'''

#la funcion define si se puede hacer un triangulo con los datos que se pasan a la funcion
def es_triangulo(lado_a, lado_b,lado_c):
    return lado_a + lado_b > lado_c and lado_b+lado_c > lado_a and lado_a + lado_c > lado_b#  expresión universal para probar triángulos

#con estas lineas podemos probar la funcion es_triangulo y verificar si la logica es correcta (la comentamos para agregar mas logica al trabajo)
'''print(es_triangulo(1,1,3))
print(es_triangulo(1,1,1))
print(es_triangulo(2,1,3))
print(es_triangulo(1,2,2))
print(es_triangulo(1,2,1))'''

# a partir de ahora esto funcionara pidiendole a un usuario que ingrese cado lado (comentado para ampliar el trabajo)
# lado_a = float(input('Ingresa la longitud del primer lado: '))
# lado_b = float(input('Ingresa la longitud del segundo lado: '))
# lado_c = float(input('Ingresa la longitud del tercer lado: '))

#agregaremos la logica para determinar si es un triangulo para imprimir un mensaje en consecuencia
# if es_triangulo(lado_a, lado_b, lado_c):
#     print('Si, si puede ser un triangulo')
# else:
#     print('No, no puede ser un triangulo')

#a partir de aca tratareamos de determinar si un triangulo es triangulo rectangulo
#usando el teorema de pitagoras c2 = a2 + b2 donde 2 es el lado elevado al cuadrado
def triangulo_rectangulo(lado_a,lado_b,lado_c):
    if not es_triangulo(lado_a,lado_b,lado_c):
        return False
    if lado_c > lado_a and lado_c > lado_b:
        return lado_c ** 2 == lado_a ** 2 + lado_b ** 2 
        7
    if lado_a > lado_b and lado_a > lado_c:
        return lado_a ** 2 == lado_b ** 2 + lado_c ** 2

print(triangulo_rectangulo(5,3,4))
print(triangulo_rectangulo(1,3,4))


#ahora realizaremos el calculo del area de un triangulo con la formula de Heron

def heron(lado_a,lado_b,lado_c):
    semiperimetro_triangulo = (lado_a + lado_b + lado_c)/2
    #retorna el area del triangulo
    return (semiperimetro_triangulo * (semiperimetro_triangulo - lado_a) * (semiperimetro_triangulo - lado_b) * (semiperimetro_triangulo - lado_c)) ** 0.5

def area_triangulo(lado_a,lado_b,lado_c):
    if not es_triangulo(lado_a,lado_b,lado_c):
        return None
    return heron(lado_a,lado_b,lado_c)

print(area_triangulo(1.,1.,2.**.5))