class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Crea una nueva pila"""
        self._items = []

    def isEmpty(self):
        """Determina si la pila esta vacia o no"""
        return not bool(self._items)

    def push(self, item):
        """Agrega elementos a la pila"""
        self._items.append(item)

    def pop(self):
        """Elimina el ultimo elemento de la pila"""
        return self._items.pop()

    def peek(self):
        """Muestra el ultimo elemento agregado a la pila"""
        return self._items[-1]

    def size(self):
        """Muestra el numero de elementos en la pila"""
        return len(self._items)
numero=Stack()
numero.push("12345")
numero.push("69153")
numero.push("32190")

print(f"El ultimo numero el cual usted recibio una llamada es {numero.peek()}")
print(f"Usted recibio un total de {numero.size()} llamadas")