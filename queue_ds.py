from collections import deque
 
 
class Queue:
    """Cola FIFO. Entra por atras, sale por el frente."""
 
    def __init__(self):
        self._elementos = deque()