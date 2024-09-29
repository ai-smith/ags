class PositionException(Exception):
    pass


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
   
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.current
            current.next = node

    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert(self, position, data):
        if position == 0:
            if self.head:
                self.prepend(data)
            else:
                raise PositionException('Position out of bounds')
        else:
            i = 0
            node = self.head
            while node and i < position - 1:
                node = node.next
                i += 1
            if not node:
                raise PositionException('Position out of bounds')
            else:
                new_node = Node(data)
                new_node.next = node.next
                node.next = new_node
            
    def delete(self, position):
        if position == 0:
            if self.head:
                self.head = self.head.next
            else:
                raise PositionException('Position out of bounds')
        else:
            i = 0
            node = self.head
            while node and i < position - 1:
                node = node.next
            if i != position - 1 or not node.next:
                raise PositionException('Position out of bounds')
            else:
                if node.next.next:
                    node.next = node.next.next
                else:
                    node.next = None

    def display(self):
        all_data = []
        node = self.head
        while node:
            all_data.append(node.data)
            node = node.next
        return all_data
    
    def length(self):
        node = self.head
        i = 0
        while node:
            node = node.next
            i += 1
        return i