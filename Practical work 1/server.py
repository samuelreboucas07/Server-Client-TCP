import socket
import pickle
import sys
import os

path = './files'
buffer_size = 1024
port = 5009
address = 'localhost'
# for path, directory, file in os.walk('./files'): #reading of file in directory
#     print(file) #files of directory

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

socket_server.bind((address, port))

socket_server.listen()

while(True):
    print("Esperando conexão ....")
    conn, addr = socket_server.accept()
    print("Conexão realizada com cliente")
    
    file_name_client = conn.recv(1024)
    file_name = pickle.loads(file_name_client)

    file = open(path+'/'+file_name, 'rb')

    fragment_file = file.read(buffer_size)
    while(fragment_file):
        conn.send(fragment_file)
        fragment_file = file.read(buffer_size)
    if not fragment_file:
        file.close()
        conn.close()



#     msg = pickle.dumps(x)

#     conn.send(msg)
