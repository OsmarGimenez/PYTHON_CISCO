def mostrar_digito(digito):
    patrones = [
        [" ### ", "#   #", "#   #", "#   #", " ### "],  # 0
        ["   # ", "   #", "   #", "   #", "   # "],  # 1
        [" ### ", "    #", " ### ", "#    ", " ### "],  # 2
        [" ### ", "    #", " ### ", "    #", " ### "],  # 3
        ["#   #", "#   #", " ### ", "    #", "    #"],  # 4
        [" ### ", "#    ", " ### ", "    #", " ### "],  # 5
        [" ### ", "#    ", " ### ", "#   #", " ### "],  # 6
        [" ### ", "    #", "    #", "    #", "    #"],  # 7
        [" ### ", "#   #", " ### ", "#   #", " ### "],  # 8
        [" ### ", "#   #", " ### ", "    #", " ### "]   # 9
    ]

    if 0 <= digito <= 9:
        return patrones[digito]
    else:
        return [" Digito ", "no", "valido", "     ", "     "]

def mostrar_numero(numero):
    if not isinstance(numero, int) or numero < 0:
        print("Por favor, ingresa un número entero no negativo.")
        return

    digitos = [int(d) for d in str(numero)]
    segmentos_digitos = [mostrar_digito(d) for d in digitos]

    for fila in range(5):
        linea = ""
        for segmento in segmentos_digitos:
            linea += segmento[fila] + "  "  # Añade espacio entre dígitos
        print(linea)

if __name__ == "__main__":
    try:
        num_ingresado = int(input("Ingresa un número entero no negativo: "))
        mostrar_numero(num_ingresado)
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")