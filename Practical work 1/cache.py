
cache = {}
max_size_cache = 600 #MB

class ManagerCache():
    def list_cache(self):
        files = []
        for file in cache:
            files.append(file)
        return files

    def allocate(self, file_name, file, item_size):
        cache[file_name] = {'file': file, 'size': item_size}

    def verificFile(self, file_name):
        if file_name in cache:
            file = cache.get(file_name)['file']
            return {'status': True, 'data': file}
        else:
            return {'status': False, 'data': {}}

    def verificCacheSpace(self, file_size):
        busy_size = 0.0
        if(file_size > max_size_cache):
            print("Arquivo maior que a capacidade máxima da cache.")
            return False
        else:
            print("Verificando espaço livre")
            for file in cache.values():
                busy_size = busy_size + file['size']
            if(busy_size + file_size > max_size_cache):
                self.freeMemory(file_size)
                return True
            else:
                print("Alocar na cache")
                return True

    def freeMemory(self, file_size): #Remove item com tamanho maior ou igual, caso não tenha, vai removendo até liberar espaço
        print("LIBERAR CACHE")
        size_excluded_cache = 0.0
        freed_up_space = False
        for file in cache:
            if(cache[file]['size'] >= file_size):
                cache.pop(file)
                freed_up_space = True
                break
        if(freed_up_space):
            return True
        else:        
            while(size_excluded_cache<file_size):
                if(len(cache) > 0):
                    item_excluded_cache = cache.popitem()
                    size_excluded_cache = size_excluded_cache + item_excluded_cache[1]['size']
                else:
                    break  
            return True
