import socket
import sys
import pickle

socket_client = socket.socket()
port = 5009
address = 'localhost'
buffer_size = 1024

file = sys.argv[1]
# address_save = sys.argv[2]

socket_client.connect((address, port))

file_name = pickle.dumps(file)

socket_client.send(file_name)

file_received = file
with open(file_received, 'wb') as file:
    print('Arquivo aberto')
    while True:
        fragment_file = socket_client.recv(buffer_size)
        if not fragment_file:
            file.close()
            print("Arquivo fechado")
            break
        file.write(fragment_file)

socket_client.close()

# data = socket_client.recv(1024)

# result = pickle.loads(data)

# print(result)