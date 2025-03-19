import socket
import time

host='127.0.0.1'
port=12345
message='ping'


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
    
start_time = time.time()
client_socket.sendall(message.encode())
data = client_socket.recv(1024)
end_time = time.time()
    
print(f"Received: {data.decode()} | RTT: {end_time - start_time:.6f} sec")
client_socket.close()