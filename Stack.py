# stack


class Stack:

    def __init__(self):
        self._datos = []

    def push(self, item):
        self._datos.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("La pila esta vacia")
        return self._datos.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("La pila esta vacia")
        return self._datos[-1]

    def is_empty(self):
        return len(self._datos) == 0

    def size(self):
        return len(self._datos)

    def clear(self):
        self._datos.clear()

    def __repr__(self):
        return f"Stack({self._datos})"