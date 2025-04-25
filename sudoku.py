def es_sudoku_valido(sudoku):
    # Verificar filas
    for fila in sudoku:
        if not es_conjunto_valido(fila):
            return "No"

    # Verificar columnas
    for columna in range(9):
        columna_valores = [sudoku[fila][columna] for fila in range(9)]
        if not es_conjunto_valido(columna_valores):
            return "No"

    # Verificar subcuadrículas de 3x3
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subcuadricula = [sudoku[fila][columna] for fila in range(i, i + 3) for columna in range(j, j + 3)]
            if not es_conjunto_valido(subcuadricula):
                return "No"

    return "Si"

def es_conjunto_valido(conjunto):
    numeros = [n for n in conjunto if n != '.']
    return len(numeros) == len(set(numeros)) and all('1' <= n <= '9' for n in numeros)

if __name__ == "__main__":
    sudoku_tablero = []
    print("Ingresa las 9 filas del Sudoku, cada una con 9 dígitos (usa '.' para celdas vacías):")
    for _ in range(9):
        fila = input()
        if len(fila) != 9:
            print("Error: Cada fila debe contener 9 caracteres.")
            exit()
        sudoku_tablero.append(list(fila))

    resultado = es_sudoku_valido(sudoku_tablero)
    print(resultado)