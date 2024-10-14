import requests
import sys 

if len(sys.argv) != 2:
    print("Uso: python script.py <dominio o IP>")
    sys.exit(1)

domain = sys.argv[1]
timeout = 5 # Tiempo máximo de espera en segundos para la respuesta

if not domain.startswith("http://") and not domain.startswith("https://"):
    domain = "https://" + domain
    

def hacer_peticion(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"Petición a {url} con código de estado: {response.status_code}")
    except requests.exceptions.Timeout:
        print(f"Error: La solicitud a {url} excedió el tiempo límite de {timeout} segundos")
    except requests.exceptions.RequestException as e:
            print(f"Error en la petición a {url}: {e}")

hacer_peticion(domain)

# Hacer otra petición con una posible URL HTTP explícita (puedes ajustar http_domain)
http_domain = "http://" + sys.argv[1]
hacer_peticion(http_domain)