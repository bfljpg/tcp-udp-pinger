import socket
import time

def udp_client(host, port, message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    start_time = time.time()
    client_socket.sendto(message.encode(), (host, port))
        
    try:
        client_socket.settimeout(1)  # 1 saniye içinde yanıt gelmezse timeout
        data, _ = client_socket.recvfrom(1024)
        end_time = time.time()
        print(f"Received: {data.decode()} | RTT: {end_time - start_time:.6f} sec")
    except socket.timeout:
        print("Packet lost!")
        
    client_socket.close()
    time.sleep(0.5)

while True:
    udp_client('0.0.0.0', 29900, 'ping')