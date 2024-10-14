import sys
import random
import string


if len(sys.argv) < 2:
    print("Uso : python caja.py <ancho> <alto> <tipo>")
    sys.exit(1)
elif len(sys.argv) < 3:
    print("Uso : python caja.py <ancho> <alto> <tipo>")
    sys.exit(1)
elif len(sys.argv) < 4:
    print("Uso : python caja.py <ancho> <alto> <tipo>")
    sys.exit(1)

ancho = (sys.argv[1]) 
alto = (sys.argv[2])
tipo = sys.argv[3]



if ancho.isdigit():
    ancho = int(ancho)
else:
    print("El ancho debe ser un numero.")
    sys.exit(1)

if alto.isdigit():
    alto = int(alto)
else:
    print("El alto debe ser un numero.")
    sys.exit(1)

# Compobrar que las cajas se vean proporcionales:
if ancho == alto:
    ancho = ancho * 3
elif ancho == alto + 1:
    ancho = ancho * 2
elif ancho == alto + 2:
    ancho = ancho + 2


# Comprobar si el tipo es válido:
if len(tipo) > 1 and tipo not in ["simple", "doble"]:
    print("El tipo debe ser un solo caracter, simple o doble.")
    sys.exit(1)


def imprimir_caja_simple():
    top = "\u250C" + "\u2500"*ancho + "\u2510"
    bottom = "\u2514" + "\u2500"*ancho + "\u2518"
    print(top)
    for x in range (0,alto):
        mid = "\u2502" + ''.join(random.choice(string.ascii_letters + string.digits) for x in range(ancho)) + "\u2502"
        print(mid)
    print(bottom)



def imprimir_caja_doble():
    top = "\u250F" + "\u2501"*ancho + "\u2513"
    bottom = "\u2517" + "\u2501"*ancho + "\u251B"
    print(top)
    for x in range (0,alto):
        mid = "\u2517" + ''.join(random.choice(string.ascii_letters + string.digits) for x in range(ancho)) + "\u2517"
        print(mid)
    print(bottom)


def imprimir_caja_fea():
    top = tipo + tipo*ancho + tipo
    bottom = tipo + tipo*ancho + tipo
    print(top)
    for x in range (0,alto):
        mid = tipo + ''.join(random.choice(string.ascii_letters + string.digits) for x in range(ancho)) + tipo
        print(mid)
    print(bottom)

if tipo == "simple":
    print("El resultado es: ")
    imprimir_caja_simple()
elif tipo == "doble":
    print("El resultado es: ")
    imprimir_caja_doble()
elif len(tipo) == 1:
    imprimir_caja_fea()




