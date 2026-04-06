# demo

from stack import Stack
from queue_ds import Queue
from hash_table import HashTable

print("=== STACK ===")
pila = Stack()
pila.push(10)
pila.push(20)
pila.push(30)
print(f"Pila: {pila}")
print(f"pop(): {pila.pop()}")
print(f"peek(): {pila.peek()}")

print("\n=== QUEUE ===")
cola = Queue()
cola.enqueue("A")
cola.enqueue("B")
cola.enqueue("C")
print(f"Cola: {cola}")
print(f"dequeue(): {cola.dequeue()}")
print(f"front(): {cola.front()}")

print("\n=== HASH TABLE ===")
ht = HashTable()
ht.put("nombre", "Eddie")
ht.put("edad", 22)
print(f"Tabla: {ht}")
print(f"get('nombre'): {ht.get('nombre')}")
ht.remove("edad")
print(f"Despues de remove: {ht}")