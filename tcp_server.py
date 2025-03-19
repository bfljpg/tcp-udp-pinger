import socket
import time

host='127.0.0.1'
port=12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print(f"TCP Server listening on {host}:{port}")
    
conn, addr = server_socket.accept()
print(f"Connected by {addr}")
    
while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
    
conn.close()