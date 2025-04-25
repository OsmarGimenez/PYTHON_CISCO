def cifrado_cesar_mejorado(texto, desplazamiento):
    resultado = ''
    for caracter in texto:
        if caracter.isalpha():
            inicio = ord('a') if caracter.islower() else ord('A')
            desplazamiento_mod = desplazamiento % 26
            nuevo_codigo = ord(caracter) - inicio + desplazamiento_mod
            resultado += chr(inicio + nuevo_codigo % 26)
        else:
            resultado += caracter
    return resultado

def obtener_desplazamiento():
    while True:
        try:
            desplazamiento = int(input("Ingresa el valor de desplazamiento (un número entero del 1 al 25): "))
            if 1 <= desplazamiento <= 25:
                return desplazamiento
            else:
                print("El valor de desplazamiento debe estar entre 1 y 25.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

if __name__ == "__main__":
    texto_a_cifrar = input("Ingresa la línea de texto para encriptar: ")
    desplazamiento = obtener_desplazamiento()
    texto_cifrado = cifrado_cesar_mejorado(texto_a_cifrar, desplazamiento)
    print("Texto codificado:", texto_cifrado)