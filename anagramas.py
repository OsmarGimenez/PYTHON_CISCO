def son_anagramas(texto1, texto2):
    texto1_procesado = sorted("".join(caracter.lower() for caracter in texto1 if caracter.isalnum()))
    texto2_procesado = sorted("".join(caracter.lower() for caracter in texto2 if caracter.isalnum()))
    return texto1_procesado == texto2_procesado

if __name__ == "__main__":
    texto1_ingresado = input("Ingresa el primer texto: ")
    texto2_ingresado = input("Ingresa el segundo texto: ")

    if texto1_ingresado == "" or texto2_ingresado == "":
        print("Dos cadenas vacías no son anagramas.")
    elif son_anagramas(texto1_ingresado, texto2_ingresado):
        print(f"'{texto1_ingresado}' y '{texto2_ingresado}' son anagramas.")
    else:
        print(f"'{texto1_ingresado}' y '{texto2_ingresado}' no son anagramas.")