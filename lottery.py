import random

def generar_numero_loteria():
    # Generar un número aleatorio de 6 cifras
    numero = random.randint(0, 999999)
    numero_con_6_digitos = f"{numero:06d}" 
    return numero_con_6_digitos

def tiradas_loteria(cantidad):
    # Simular varias tiradas de lotería
    resultados = [generar_numero_loteria() for _ in range(cantidad)]
    return resultados

# Solicitar al usuario cuántas tiradas quiere
if __name__ == "__main__":
    try:
        cantidad_tiradas = int(input("¿Cuántas tiradas de lotería deseas realizar?: "))
        if cantidad_tiradas <= 0:
            print("Por favor, ingresa un número mayor a 0.")
        else:
            tiradas = tiradas_loteria(cantidad_tiradas)
            print("\nResultados de las tiradas:")
            for i, numero in enumerate(tiradas, 1):
                print(f"Tirada {i}: {numero}")
    except ValueError:
        print("Por favor, ingresa un número válido.")

