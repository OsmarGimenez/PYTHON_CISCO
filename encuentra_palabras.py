def encontrar_palabra(palabra, caracteres):
    palabra = palabra.lower()
    caracteres = caracteres.lower()
    caracteres_disponibles = list(caracteres)

    for letra in palabra:
        if letra in caracteres_disponibles:
            caracteres_disponibles.remove(letra)
        else:
            return "no"
    return "si"

if __name__ == "__main__":
    palabra_buscar = input("Ingresa la palabra a buscar: ")
    grupo_caracteres = input("Ingresa el grupo de caracteres: ")
    resultado = encontrar_palabra(palabra_buscar, grupo_caracteres)
    print("¿Los caracteres de la primera cadena están ocultos en la segunda?", resultado)