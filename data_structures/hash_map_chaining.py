from typing import Any
from .linked_list import Node


class HashMap:

    def __init__(self, size):
        self._size = size
        self._arr = [None for _ in range(size)]

    def __setitem__ (self, key, value):
        ind = hash(key) % self._size
        if not self._arr[ind]:
            self._arr[ind] = Node((key, value))
        else:
            node = self._arr[ind]
            while node.next:
                item = node.data
                if item[0] == key:
                    node.data = (key, value)
                    break
                node = node.next
            else:
                node.next = Node((key, value))
        
    def __getitem__(self, key):
        ind = hash(key) % self._size
        if self._arr[ind]:
            node = self._arr[ind]
            while node.next:
                item = node.data
                if item[0] == key:
                    return item[1]
                node = node.next
        raise KeyError(key)

    def __delitem__(self, key):
        ind = hash(key) % self._size
        if self._arr[ind]:
            node = self._arr[ind]
            if node.data[0] == key:
                self._arr[ind] = node.next
                return
            while node.next:
                item = node.next.data
                if  item[0] == key:
                    node.next = node.next.next
                    return
        raise KeyError(key)


    def __str__(self):
        res = '{'
        for node in self._arr:
            while node:
                item = node.data
                res += f'\'{item[0]}\':{item[1]}'
                node = node.next
        res += '}'
        return res

    def __repr__(self):
        return self.__str__()