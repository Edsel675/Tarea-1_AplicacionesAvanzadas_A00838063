# queue
 
from collections import deque
 
class Queue:
 
    def __init__(self):
        self._datos = deque()
 
    def enqueue(self, item):
        self._datos.append(item)
 
    def dequeue(self):
        if self.is_empty():
            raise IndexError("La cola esta vacia")
        return self._datos.popleft()
 
    def front(self):
        if self.is_empty():
            raise IndexError("La cola esta vacia")
        return self._datos[0]
 
    def is_empty(self):
        return len(self._datos) == 0
 
    def size(self):
        return len(self._datos)
 
    def clear(self):
        self._datos.clear()
 
    def __repr__(self):
        return f"Queue({list(self._datos)})"