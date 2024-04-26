import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    message = "Hello, server!"
    client_socket.sendall(message.encode())
    received_data = client_socket.recv(1024)
    print("Connected to the server")
    # print("Received:", received_data.decode())
