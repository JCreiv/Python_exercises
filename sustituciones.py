# Diccionario de sustituciones avanzadas
sustituciones = {
    'O': '0', 'I': '1', 'E': '3', 'A': '4', 'S': '5',
    'G': '6', 'T': '7', 'B': '8', 'g': '9', 'o': '0', 
    'i': '1', 'e': '3', 'a': '4', 's': '5', 't': '7', 
    'b': '8', 'l': '|', 'z': '2', 'h': '#', 'c': '(', 
    'k': '|<', 'm': '^^'
}

# Leer la cadena del usuario
cadena = input("Introduce el texto a convertir: ")

for char in cadena:
    sustituciones.get(char,char)
    print(sustituciones.get(char, char), end='')

