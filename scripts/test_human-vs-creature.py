import random

# Valores iniciales
vida_humano = 6
vida_criatura = 3
caras_dado = 6

def simular_enfrentamiento(vida_humano, vida_criatura, caras_dado):
    resultado = []
    while vida_humano > 0 and vida_criatura > 0:
        dado_humano = random.randint(1, caras_dado)
        dado_criatura = random.randint(1, caras_dado)
        
        if dado_humano > dado_criatura:
            vida_criatura -= 1
            resultado.append("El humano hace daño a la criatura. Vida de la criatura: {}".format(vida_criatura))
        elif dado_humano < dado_criatura:
            vida_humano -= 1
            resultado.append("La criatura hace daño al humano. Vida del humano: {}".format(vida_humano))
        else:
            resultado.append("Empate. Ninguno hace daño.")

    if vida_humano <= 0:
        resultado.append("La criatura ha ganado.")
    else:
        resultado.append("El humano ha ganado.")

    return resultado

def guardar_resultado(resultados):
    with open("resultado_enfrentamiento.txt", "w") as file:
        for linea in resultados:
            file.write(linea + "\n")

if __name__ == "__main__":
    resultados = simular_enfrentamiento(vida_humano, vida_criatura, caras_dado)
    for resultado in resultados:
        print(resultado)
    guardar_resultado(resultados)
