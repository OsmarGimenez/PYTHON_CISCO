def calcular_digito_vida(fecha):
    digitos = [int(d) for d in fecha if d.isdigit()]
    suma = sum(digitos)

    while suma > 9:
        nueva_suma = 0
        for digito in str(suma):
            nueva_suma += int(digito)
        suma = nueva_suma

    return suma

if __name__ == "__main__":
    fecha_nacimiento = input("Ingresa tu fecha de nacimiento (en formato AAAA-MM-DD, AAAAMMDD, MM-DD-AAAA, etc.): ")
    digito_vida = calcular_digito_vida(fecha_nacimiento)
    print("El Dígito de la Vida para la fecha ingresada es:", digito_vida)