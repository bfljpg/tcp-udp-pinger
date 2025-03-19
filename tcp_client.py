import socket
import time

def tcp_client(host, port, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
        
    start_time = time.time()
    client_socket.sendall(message.encode())
    data = client_socket.recv(1024)
    end_time = time.time()
        
    print(f"Received: {data.decode()} | RTT: {end_time - start_time:.6f} sec")
    client_socket.close()
    time.sleep(0.5)

while True:
    tcp_client('0.0.0.0', 29900, 'ping')