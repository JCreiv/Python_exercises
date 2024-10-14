
### Script sustituciones.py

Este script tiene como objetivo **convertir un texto ingresado por el usuario en una versión modificada** usando una serie de sustituciones de caracteres 


##### Características:

- El script reemplaza caracteres en mayúsculas y minúsculas por símbolos, números o combinaciones de caracteres especiales según las reglas de un **diccionario de sustituciones**.

##### Ejemplo de entrada y salida:

Entrada:
`"Hola amigos!"`

Salida:
``H0|4 4^^1905!%``
#### Estructura del código:

1. **Diccionario de sustituciones**: Se define un diccionario llamado `sustituciones`, donde cada clave es un carácter original y su valor correspondiente es el carácter de sustitución.

2. **Lectura del texto**: El texto se solicita al usuario a través de la función `input()`. El usuario puede ingresar cualquier cadena de texto.
3. **Proceso de sustitución**:
- El texto insertado entra en bucle for donde cada carácter se procesa uno a uno
- Para cada carácter busca en el diccionario su valor
- Si encuentra el valor lo sustituye, si no lo encuentra deja el carácter original
4. **Resultado:** El resultado final es una cadena con las modificaciones aplicadas, que se imprime directamente en la consola.


### Script caja.py


##### Características:

- Este script **genera y muestra una "caja" de caracteres ASCII de un tamaño específico**, con un contenido aleatorio de letras y números. La caja puede ser de tipo "simple", "doble" o "fea". El usuario debe especificar el ancho, alto y tipo de caja al ejecutar el script.

#### Uso:

1. Uso: python caja.py 
```bash
python caja.py <ancho> <alto> <tipo>
```

2. Argumentos: 
- ancho (int): Ancho de la caja (debe ser un número entero positivo). 
- alto (int): Alto de la caja (debe ser un número entero positivo). 
- tipo (str): Tipo de caja (debe ser 'simple', 'doble', o un único carácter para 'fea'). 
3. Ejemplos: 
- python caja.py 10 5 simple  
- python caja.py 8 4 doble python 
- python caja.py 6 3 @ 
4. Notas: 
- El ancho y alto se ajustan automáticamente si son iguales o difieren en 1 o 2. 
- Si el tipo especificado no es válido, el script mostrará un mensaje de error. 

### Script ping.py

Este script permite **hacer pings a una dirección IP específica con un tamaño y número de peticiones configurables.**

#### Uso 
1. Ejecuta el script en tu terminal. 
2. Introduce la dirección IP de la víctima. 
3. Especifica el número de peticiones que deseas enviar. 
4. Especifica el tamaño de las peticiones en bytes.

##### Ejemplo


```bash
python ping_script.py 
Dirección IP víctima: 192.168.1.1 
Número de peticiones: 10 
Tamaño de peticiones: 100
```

##### Notas 
- El tamaño de las peticiones se limita a un máximo de 1000 bytes. 
- Asegúrate de tener los permisos necesarios para ejecutar el comando `ping`.


### peticiones.py

##### Script de Peticiones HTTP/HTTPS

Este script realiza peticiones HTTP y HTTPS a un dominio o dirección IP proporcionada y muestra el código de estado de la respuesta. Si no se especifica el protocolo, el script intentará realizar la primera petición con `https://` y luego intentará con `http://`.

#### Uso

Para ejecutar el script, utiliza el siguiente comando:

```bash
python script.py <dominio o IP>
```

### RequestsApi.py

##### Script de Petición a API de Usuarios

Este script realiza una petición a la API `https://dummyjson.com/users`, obtiene los nombres de los usuarios y los guarda en un archivo de texto llamado `resultados.txt`.

##### Uso

1. El script realiza una petición GET a la API de usuarios.
2. Si la respuesta es exitosa (código 200), filtra los nombres de los usuarios.
3. Imprime los nombres de los usuarios en la consola.
4. Almacena el código de respuesta junto con la URL de la petición en un archivo llamado `resultados.txt`.

##### Notas

- El archivo `resultados.txt` se crea automáticamente si no existe y se agrega información al final del archivo cada vez que se ejecuta el script.
- Si la petición falla, se muestra un mensaje de error con el código de estado de la respuesta.

##### Ejemplo

```bash
python script.py
```


Este comando ejecutará el script y guardará los resultados en el archivo `resultados.txt`.


### Keylogger.py

Este proyecto es un keylogger simple desarrollado en Python que captura las pulsaciones del teclado y las envía a un servidor a través de una solicitud HTTP `GET`. Las teclas capturadas también se guardan en un archivo local.

##### Requisitos

Este keylogger requiere los siguientes paquetes de Python:

- `pynput` para la captura de las teclas del teclado.
- `requests` para enviar las teclas capturadas a un servidor remoto.

Puedes instalarlos con los siguientes comandos:

```bash
pip install pynput requests
```

#### Estructura del Código

El keylogger realiza dos tareas principales:

1. **Captura las teclas** que se presionan y las guarda en un archivo de registro.
2. **Envía las teclas capturadas a un servidor** remoto utilizando una solicitud HTTP GET.

##### Componentes del Código:

1. **`on_press(key)`**: Esta función se ejecuta cada vez que se presiona una tecla.
    
    - Captura teclas regulares y las guarda en la variable `log`.
    - Captura teclas especiales (como espacio, shift, etc.) y las almacena en un formato adecuado.
    - Llama a la función `enviar_datos()` para enviar las teclas al servidor.
    - Guarda las teclas localmente en el archivo `keylogger_output.txt`.
2. **`enviar_datos(data)`**: Esta función toma las teclas capturadas y las envía a un servidor remoto mediante una solicitud HTTP GET.
    
    - La URL del servidor está especificada en la variable `url`.
    - Si la solicitud es exitosa (código de estado HTTP 200), imprime un mensaje de éxito. De lo contrario, muestra un mensaje de error.
3. **`start_keylogger()`**: Inicia el listener del teclado que captura las teclas utilizando la biblioteca `pynput`.
    

#### Uso

1. Asegúrate de haber instalado los requisitos con `pip install pynput requests`.
2. Configura la URL donde quieres enviar los datos modificando la variable `url` en el script principal.

```bash
python keylogger.py
```


## Advertencias

Este script es solo con fines educativos. El uso no autorizado de un keylogger puede ser ilegal en muchos países. Asegúrate de tener el consentimiento adecuado antes de usar este código en sistemas que no sean de tu propiedad.