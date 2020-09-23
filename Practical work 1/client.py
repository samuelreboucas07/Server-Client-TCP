import socket
import sys
import pickle

buffer_size = 1024
socket_client = socket.socket()
address = sys.argv[1]
port = sys.argv[2]
socket_client.connect((address, int(port)))

if(len(sys.argv) == 5):
    file = sys.argv[3]
    path_save = sys.argv[4]
    file_name = pickle.dumps(file)
    socket_client.send(file_name)
    file_received = file
    status_search_file = socket_client.recv(buffer_size)
    status_message = pickle.loads(status_search_file)
    if(status_message['status']):
        with open(path_save+'/'+file_received, 'wb') as file:
            while True:
                fragment_file = socket_client.recv(buffer_size)
                if not fragment_file:
                    file.close()
                    print("Arquivo "+file_received+" salvo em "+path_save)
                    break
                file.write(fragment_file)


if(len(sys.argv) == 4):
    list_files_cache = sys.argv[3]
    if(list_files_cache == 'list_files_cache'):
        list_files_message = pickle.dumps(list_files_cache)
        socket_client.send(list_files_message)
        files_cache = socket_client.recv(buffer_size)
        files_cache_list = pickle.loads(files_cache)
        print("Arquivos presentes na memória cache:")
        for file in files_cache_list:
            print (file)

socket_client.close()