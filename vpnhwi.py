import socket, threading, getpass

HOST = "127.0.0.1" # Solo tu celular
PORT = 8888
USER = "pantera"
PASS = getpass.getpass("Pon tu password segura: ")

print(f"Proxy SEGURO en {HOST}:{PORT} user:{USER}")
# ... resto de tu codigo ...