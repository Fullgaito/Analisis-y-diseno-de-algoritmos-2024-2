class TablaHash:
    def __init__(self, size):
        self.table = [None] * size
        self.size = size
        self.colisiones = 0

    # Función hash
    def h(self, item):
        return item % self.size

    def put(self, key, item):  # Método para ingresar elementos
        hash_index = self.h(key)
        if self.table[hash_index] is None:
            self.table[hash_index] = item
            return hash_index
        else:
            i = 1
            self.colisiones += 1
            while True:
                rehash = (hash_index + i) % self.size
                if self.table[rehash] is None:
                    self.table[rehash] = item
                    return rehash
                i += 1
                self.colisiones += 1

    def search(self, key):  # Método para buscar elementos
        hash_index = self.h(key)
        i = 0
        while True:
            current_index = (hash_index + i) % self.size
            if self.table[current_index] is None:
                return None 
            elif key == self.table[current_index].getID():
                return self.table[current_index].getNombre()  
            i += 1
            if i >= self.size: 
                return None  

    def delete(self, key):  # Método para eliminar un elemento
        hash_index = self.h(key)
        i = 0
        while True:
            current_index = (hash_index + i) % self.size
            if self.table[current_index] is None:
                return False  
            elif key == self.table[current_index].getID():
                self.table[current_index] = None  
                return True  
            i += 1
            if i >= self.size:  
                return False  

    def __str__(self):  # Método para representar la tabla hash
        return ', '.join(f'{i}: {p.getNombre() if p else "None"}' for i, p in enumerate(self.table))


class Persona:
    def __init__(self, ID, nombre):
        self.ID = ID
        self.nombre = nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def setID(self, ID):
        self.ID = ID

    def getNombre(self):
        return self.nombre

    def getID(self):
        return self.ID


def listaPersonas(listaID, listaNombre):
    listapersonas = []
    for i in range(len(listaID)):
        listapersonas.append(Persona(listaID[i], listaNombre[i]))
    return listapersonas

ids = [1, 2, 3, 4, 5]
nombres = ["Jorge", "Andres", "Sergio", "Camila", "Luis"]  


personas = listaPersonas(ids, nombres)

tabla = TablaHash(5)
for persona in personas:
    tabla.put(persona.getID(), persona)

# Buscar una persona
nombre_encontrado = tabla.search(3)
print(f"{nombre_encontrado} está agregada en la Tabla Hash")

# Imprimir carga original de la tabla hash
print(f"Carga original: {tabla}")

# Eliminar una persona
tabla.delete(2)
print(f"Después de eliminar, buscar ID 2: {tabla.search(2)}")
print(f"Carga actualizada: {tabla}")
