import socket
import time

def udp_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP Server listening on {host}:{port}")
        
    while True:
        data, addr = server_socket.recvfrom(1024)
        print(f"Received from {addr}: {data.decode()}")
        server_socket.sendto(data, addr)

while True:
    udp_server('127.0.0.1', 12345)