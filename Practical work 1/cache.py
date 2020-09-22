
cache = {}
max_size_cache = 2 #MB
class ManagerCache():
    def allocate(self, file_name, file, item_size):
        self.verificCacheSpaceFree()
        cache[file_name] = {'file': file, 'size': item_size}
    
    def verificFile(self, file_name):
        if file_name in cache:
            file = cache.get(file_name)['file']
            return {'status': True, 'data': file}
        else:
            return {'status': False, 'data': {}}

    def verificCacheSpaceFree(self):
        # print(cache)
        print("Verificando espaço livre")