
from .linked_list import Node

class StackFullException(Exception):
    pass

class StackEmptyException(Exception):
    pass

class Stack:

    def __init__(self):
        self._top = None

    def push(self, d):
        node = Node(d)
        if self._top:
            node.next = self._top                
        self._top = node 

    def pop(self):
        if self._top:
            node = self._top
            self._top = node.next
            return node.data
        else:
            raise StackEmptyException('Stask is empty.')

    def is_empty(self):
        if self._top:
            return False
        else:
            return True

    def size(self):
        n = 0
        node = self._top
        while node:
            n += 1
            node = node.next
        return n

    def peek(self):
        if self._top:
            return self._top.data
        raise StackEmptyException('Stack is empty')