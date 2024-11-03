class Node:
    def __init__(self, age):
        self.age = age
        self.left = None
        self.right = None

class AgeBST:
    def __init__(self):
        self.root = None

    def insert(self, age):
        """Inserta una edad en el árbol binario de búsqueda"""
        if self.root is None:
            self.root = Node(age)
        else:
            self._insert_recursive(self.root, age)

    def _insert_recursive(self, current, age):
        if age < current.age:
            if current.left is None:
                current.left = Node(age)
            else:
                self._insert_recursive(current.left, age)
        elif age > current.age:
            if current.right is None:
                current.right = Node(age)
            else:
                self._insert_recursive(current.right, age)

    def search(self, age):
        """Busca una edad específica en el árbol"""
        return self._search_recursive(self.root, age)

    def _search_recursive(self, current, age):
        if current is None:
            return False
        if current.age == age:
            return True
        elif age < current.age:
            return self._search_recursive(current.left, age)
        else:
            return self._search_recursive(current.right, age)

    def inorder(self):
        """Recorrido en orden para mostrar todas las edades ordenadas"""
        ages = []
        self._inorder_recursive(self.root, ages)
        return ages

    def _inorder_recursive(self, current, ages):
        if current:
            self._inorder_recursive(current.left, ages)
            ages.append(current.age)
            self._inorder_recursive(current.right, ages)

    def preorden(self):
        """Recorrido preorden"""
        ages = []
        self._preorden_recursive(self.root, ages)
        return ages

    def _preorden_recursive(self, current, ages):
        if current:
            ages.append(current.age)
            self._preorden_recursive(current.left, ages)
            self._preorden_recursive(current.right, ages)

    def postorden(self):
        """Recorrido postorden"""
        ages = []
        self._postorden_recursive(self.root, ages)
        return ages

    def _postorden_recursive(self, current, ages):
        if current:
            self._postorden_recursive(current.left, ages)
            self._postorden_recursive(current.right, ages)
            ages.append(current.age)

    def eliminacion(self, age):
        """Elimina una edad del árbol, si existe"""
        self.root = self._eliminar_recursive(self.root, age)

    def _eliminar_recursive(self, current, age):
        if current is None:
            return current
        if age < current.age:
            current.left = self._eliminar_recursive(current.left, age)
        elif age > current.age:
            current.right = self._eliminar_recursive(current.right, age)
        else:
            # Nodo con un solo hijo o sin hijos
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            temp = self._min_value_node(current.right)
            current.age = temp.age
            current.right = self._eliminar_recursive(current.right, temp.age)
        return current
age_tree = AgeBST()
age_tree.insert(30)
age_tree.insert(25)
age_tree.insert(31)
age_tree.insert(32)
age_tree.insert(21)
age_tree.insert(45)
age_tree.insert(28)

print("Edades ordenadas:", age_tree.inorder())
print("Edades en preorden:", age_tree.preorden())
print("Edades en postorden:", age_tree.postorden())

age_tree.eliminacion(31)
print("Edades ordenadas después de eliminar 31:", age_tree.inorder())
