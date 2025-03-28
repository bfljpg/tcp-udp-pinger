import socket
import time

def tcp_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"TCP Server listening on {host}:{port}")
        
    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
        
    # conn.close()
    time.sleep(0.5)

while True:
    tcp_server('0.0.0.0', 29900)