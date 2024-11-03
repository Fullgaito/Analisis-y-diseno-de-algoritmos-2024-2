class Queue:
  def __init__(self):
    """Crea una nueva cola"""
    self._items = []
  def enqueue(self, item):
    """Ingresa elementos a la cola"""
    self._items.insert(0, item)
  def size(self):
    """Determina el tamaño de la cola"""
    return len(self._items)
  def isEmpty(self):
    """Determina si la cola esta vacia o no"""
    return not bool(self._items)
  def dequeue(self):
    """Elimina de la cola el primer elemento agregado"""
    return self._items.pop()
  def peek(self):
    """Muestra el primer elemento en ser agregado a la cola"""
    return self._items[0]
cliente=Queue()
cliente.enqueue("Cliente 1")
cliente.enqueue("Cliente 2")
cliente.enqueue("Cliente 3")

print(f"Pasar a la sala de informacion el cliente {cliente.dequeue()}")