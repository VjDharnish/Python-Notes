# sender.py
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65433       # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        msg = input("Enter message (or 'exit' to quit): ")
        if msg.lower() == 'exit':
            break
        s.sendall(b'\x41\x42\x43')