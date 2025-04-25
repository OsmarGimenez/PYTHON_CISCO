def leer_entero_seguro(prompt, min_val, max_val):
    while True:
        try:
            entrada = input(prompt)
            entero = int(entrada)
            if min_val <= entero <= max_val:
                return entero
            else:
                print(f"Error: el valor no está dentro del rango permitido ({min_val}..{max_val})")
        except ValueError:
            print("Error: entrada incorrecta")

if __name__ == "__main__":
    minimo = -10
    maximo = 10
    numero_ingresado = leer_entero_seguro(f"Ingresa un número entre {minimo} a {maximo}: ", minimo, maximo)
    print("El número es:", numero_ingresado)