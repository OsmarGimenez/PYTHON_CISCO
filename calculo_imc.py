'''funcion que realiza el calculo de imc de una persona
en base a su peso en kilogramos y altura en metros'''

#primero hacemos los calculos correspondientes para la conversion 
#en caso de que se quieran usar libras y pies/pulgadas
def pies_y_pulgadas_a_metros(pies, pulgadas = 0.0):
    return pies * 0.3048 + pulgadas * 0.0254

def libras_a_kg(libras):
    return libras * 0.4535923

#calculo del imc
def calculo_Imc(peso_kg,altura_metros):
    if altura_metros < 1.0 or altura_metros > 2.5 or peso_kg < 20 or peso_kg > 200 :
        return "Ingresa datos validos"
        
    return (peso_kg/(altura_metros**2))#formula de imc estandar

#se imprime por consola la llamada a la funcion calculo_imc pasando como parametros las dos funciones
#libras_a_kg y pies_y_pulgadas_a_metros cada uno a su vez con sus parametros
print(round(calculo_Imc(peso_kg= libras_a_kg(207.23),altura_metros= pies_y_pulgadas_a_metros(5,7)),1))#print por consola y llamada a la funcion con paso de 



