import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('192.168.1.60', 8000))
print('Cliente Conectado!\n')

filename = str(input('Arquivo>'))

client.send(filename.encode())

with open(filename, 'wb') as file:
    while 1:
        data = client.recv(1000000) 
        if not data:
            break
        file.write(data)

print(f'{filename} recebido\n')