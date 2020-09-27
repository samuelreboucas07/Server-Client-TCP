from threading import Thread
from server import ServerThread
import socket
import sys

port = sys.argv[1]
path = sys.argv[2]
address = '127.0.0.1'

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind((address, int(port)))
socket_server.listen()
while(True):
    print("Esperando conexão ....")
    conn, addr = socket_server.accept()
    newThread = ServerThread(address, port, conn, addr, path)
    newThread.start()