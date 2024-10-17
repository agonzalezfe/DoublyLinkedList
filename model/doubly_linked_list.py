class Child:
    def __init__(self, id, name, age, gender):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender


class Node:
    def __init__(self, child):
        self.child = child
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        tmp = self.head
        result = ''
        while tmp:
            result += str(tmp.child.name)
            if tmp.next:
                result += ' <-> '
            tmp = tmp.next
        return result
    def append(self, child):
        newNode = Node(child)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1

    def prepend(self, child):
        newNode = Node(child)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.length += 1

    def deleteID(self, id):
        tmp = self.head
        if self.head.child.id == id:
            self.head = self.head.next
            self.head.prev = None
            return tmp
        if self.tail.id == id:
            tmp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            return tmp

        while tmp:
            if tmp.child.id == id:
                tmp.prev.next = tmp.next
                tmp.next.prev = tmp.prev

                self.length -= 1
                return tmp

            tmp = tmp.next

        return None

    def removeByPosition(self, position):
        if position < 1 or position > self.length:
            return 'posicion no valida'

        if self.head is None:
            return 'lista vacia'
        tmp = self.head
        if position == 1:
            self.head = tmp.next
            self.head.prev = None
            self.length -= 1
            return self.head
        if position == self.length:
            tmp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return tmp

        for i in range(1, position):
            tmp = tmp.next

        tmp.prev.next = tmp.next
        tmp.next.prev = tmp.prev
        self.length -= 1
        return tmp

    def addAtPosition(self, position, child):
        if position < 1 or position > self.length + 1:
            return "Posición no válida"

        new_node = Node(child)

        if position == 1:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            else:
                self.tail = new_node
            self.head = new_node
            self.length += 1
            return new_node

        if position == self.length + 1:
            new_node.prev = self.tail
            if self.tail:
                self.tail.next = new_node
            else:
                self.head = new_node
            self.tail = new_node
            self.length += 1
            return new_node

        tmp = self.head
        for i in range(1, position - 1):
            tmp = tmp.next

        new_node.next = tmp.next
        new_node.prev = tmp
        tmp.next.prev = new_node
        tmp.next = new_node

        self.length += 1
        return new_node

    def reverse(self):
        if self.head is None:
            return "La lista está vacía"

        current = self.head
        prev_node = None

        while current is not None:
            next_node = current.next
            current.next = prev_node
            current.prev = next_node
            # go to the next node
            prev_node = current
            current = next_node

        self.tail = self.head
        self.head = prev_node

        return "La lista ha sido invertida"

    def swapExtremes(self):
        if self.head is None or self.head == self.tail:
            return "No es necesario intercambiar, la lista está vacía o tiene un solo nodo"

        # Guardar referencias de los extremos
        head_node = self.head
        tail_node = self.tail

        if head_node.next == tail_node:

            head_node.next = None
            tail_node.prev = None
            head_node.prev = tail_node
            tail_node.next = head_node
        else:

            head_node.next, tail_node.next = tail_node.next, head_node.next
            head_node.prev, tail_node.prev = tail_node.prev, head_node.prev

            if head_node.next:
                head_node.next.prev = head_node
            if tail_node.prev:
                tail_node.prev.next = tail_node

        self.head = tail_node
        self.tail = head_node

        return "Nodos extremos intercambiados"

    def mixByGender(self):
        if self.length < 2:
            return 'son menos de dos no se pueden mezclar'

        boys = DoublyLinkedList()
        girls = DoublyLinkedList()

        tmp = self.head
        while tmp:
            if tmp.child.gender.upper() == 'M':
                boys.append(tmp.child)

            else:
                girls.append(tmp.child)

            tmp = tmp.next

        self.head = None
        self.length = 0

        boyNode = boys.head
        girlNode = girls.head

        while boyNode or girlNode:
            if boyNode:
                self.append(boyNode.child)
                boyNode = boyNode.next

            if girlNode:
                self.append(girlNode.child)
                girlNode = girlNode.next


if __name__ == '__main__':
    child0 = Child('0','unnamed',0,'M')
    node1 = Node(child0)
    print(node1)
    dll = DoublyLinkedList()
    print('-------append--------')
    child1 = Child('1', 'juana', 15, 'F')
    child2 = Child('2', 'marlon', 23, 'M')
    dll.append(child1)
    dll.append(child2)
    print(dll)
    print('--------prepend----')
    child3 = Child('3', 'pedro', 20, 'M')
    dll.prepend(child3)
    print(dll)
    print('---------reverse------')
    dll.reverse()
    print(dll)
    print('---------deleteID----------')
    child4 = Child('4','johana',20,'F')
    dll.append(child4)
    print(dll)
    dll.deleteID('2')
    print(dll)
    print('---------deletePosition-------')
    print(dll)
    dll.removeByPosition(1)
    print(dll)
    print('---------mixByGenders(without mixing)--------')
    child6 = Child('6', 'mario', 20, 'M')
    child7 = Child('7', 'samuel', 12, 'M')
    child8 = Child('8', 'maria', 15, 'F')
    child9 = Child('9', 'estefania', 20, 'F')
    child10 = Child('10', 'karen', 10, 'F')
    dll.append(child6)
    dll.append(child7)
    dll.append(child8)
    dll.append(child9)
    dll.append(child10)

    print(dll)
    dll.mixByGender()
    print('-----method applied(mixed)-------')
    print(dll)
