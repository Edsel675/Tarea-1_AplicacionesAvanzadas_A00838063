# hash_table
class HashTable:
 
    def __init__(self, capacidad=16):
        self._capacidad = capacidad
        self._buckets = [[] for _ in range(capacidad)]
        self._tam = 0
 
    def _indice(self, key):
        return hash(key) % self._capacidad
 
    def put(self, key, value):
        idx = self._indice(key)
        for par in self._buckets[idx]:
            if par[0] == key:
                par[1] = value
                return
        self._buckets[idx].append([key, value])
        self._tam += 1
 
    def get(self, key, default=None):
        idx = self._indice(key)
        for par in self._buckets[idx]:
            if par[0] == key:
                return par[1]
        return default
 
    def remove(self, key):
        idx = self._indice(key)
        bucket = self._buckets[idx]
        for i, par in enumerate(bucket):
            if par[0] == key:
                bucket.pop(i)
                self._tam -= 1
                return par[1]
        raise KeyError(key)
 
    def contains(self, key):
        idx = self._indice(key)
        for par in self._buckets[idx]:
            if par[0] == key:
                return True
        return False
 
    def keys(self):
        resultado = []
        for bucket in self._buckets:
            for par in bucket:
                resultado.append(par[0])
        return resultado
 
    def values(self):
        resultado = []
        for bucket in self._buckets:
            for par in bucket:
                resultado.append(par[1])
        return resultado
 
    def items(self):
        resultado = []
        for bucket in self._buckets:
            for par in bucket:
                resultado.append((par[0], par[1]))
        return resultado
 
    def size(self):
        return self._tam
 
    def is_empty(self):
        return self._tam == 0
 
    def clear(self):
        self._buckets = [[] for _ in range(self._capacidad)]
        self._tam = 0
 
    def __repr__(self):
        pares = ", ".join(f"{k}: {v}" for k, v in self.items())
        return "HashTable({" + pares + "})"
 