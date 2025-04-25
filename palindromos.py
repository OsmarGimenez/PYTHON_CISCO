def es_palindromo_v1(texto):
    texto_procesado = "".join(caracter.lower() for caracter in texto if caracter.isalnum())
    return texto_procesado == texto_procesado[::-1]

if __name__ == "__main__":
    texto_ingresado = input("Ingresa un texto: ")
    if texto_ingresado == "":
        print("La cadena vacía no es un palíndromo.")
    elif es_palindromo_v1(texto_ingresado):
        print(f"'{texto_ingresado}' es un palíndromo.")
    else:
        print(f"'{texto_ingresado}' no es un palíndromo.")