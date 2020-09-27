import socket
import pickle
import sys
import os
from threading import Thread, Lock
from cache import ManagerCache
from io import BufferedReader
from io import BytesIO

buffer_size = 1024
transformMB = 1048576 #1024 x 1024

class ServerThread(Thread):

    def __init__(self, address, port, conn, addr, path):
        Thread.__init__(self)
        self.address = address
        self.port = port
        self.conn = conn
        self.path = path
        print("Nova thread iniciada para "+str(addr[0])+" na porta: "+port)

    def run(self):
        lock = Lock()
        file_name_received = self.conn.recv(1024)
        file_name = pickle.loads(file_name_received)
        cache = ManagerCache()
        if(file_name == 'list_files'):
            files = cache.list_cache()
            list_cache = pickle.dumps(files) 
            self.conn.send(list_cache)
        else:
            lock.acquire()
            file_exist_cache = cache.verificFile(file_name)
            if( not file_exist_cache.get('status')): # File not cache
                try:
                    with open(self.path+'/'+file_name, 'rb') as file:
                        message_status = pickle.dumps({'status': True})
                        self.conn.send(message_status)
                        print("Cache miss, "+file_name+" enviado.")
                        fragment_file = file.read(buffer_size)

                        file_save_cache = open(self.path+'/'+file_name, 'rb') #Procurar alternativa
                        fragment_file_save = file_save_cache.read()
                        file_save_cache.close()
                        item_size = os.path.getsize (self.path+'/'+file_name)/transformMB
                        allocateCache = cache.verificCacheSpace(item_size)
                        if(allocateCache):
                            cache.allocate(file_name, fragment_file_save, item_size) # Allocate file  in cache
                        lock.release()
                        self.sendFile(file, fragment_file)
                    
                except FileNotFoundError:
                    message_status = pickle.dumps({'status': False}) 
                    self.conn.send(message_status)
                    print("Arquivo não encontrado.")
            else:
                lock.release()
                message_status = pickle.dumps({'status': True}) 
                self.conn.send(message_status)
                print("Cache hit, "+file_name+" enviado.")
                file_cache_received = file_exist_cache.get('data')
                file_cache = BytesIO(file_cache_received)
                fragment_file_cache = file_cache.read(buffer_size)
                self.sendFile(file_cache, fragment_file_cache)
        
    def sendFile(self, file, fragment_file):
        while(fragment_file):
            self.conn.send(fragment_file)
            fragment_file = file.read(buffer_size)
        if not fragment_file:
            file.close()
            self.conn.close()