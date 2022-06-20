import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('192.168.1.60', 8000))
server.listen(1)

connection, address = server.accept()

filename = connection.recv(1500).decode()

with open(filename, 'rb') as file:
    for data in file.readlines():
        connection.send(data)

    print('Envio com sucesso!')