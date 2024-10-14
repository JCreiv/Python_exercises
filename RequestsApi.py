import requests

url = "https://dummyjson.com/users"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Convierte la respuesta en formato JSON
    
    # Filtra los nombres de usuario
    usernames = [user['firstName'] for user in data['users']]
    
    # Muestra los nombres de usuario
    print(usernames)
else:
    print(f"Error: {response.status_code}")

def write_file(code,url,file = "resultados.txt"):
    with open(file, "a") as f:
        f.write(f"[{code}] - {url}\n")

write_file(usernames, url)