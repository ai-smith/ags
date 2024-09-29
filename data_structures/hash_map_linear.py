from .linked_list import Node
from itertools import chain


class HashMapFullException(Exception):
    pass


class HashMap:

    def __init__(self, size):
        self._size = size
        self._arr = [None for _ in range(size)]


    def __setitem__ (self, key, value):
        ind = hash(key) % self._size
        for ind in chain(range(ind, self._size), range(0, ind)):
            item = self._arr[ind]
            if not item:
                self._arr[ind] = (key, value)
                break
            elif item[0] == key:
                self._arr[ind] = (key, value)
                break
        else:
            raise HashMapFullException('Hash map is full')
                        

    def __getitem__(self, key):
        ind = hash(key) % self._size
        for ind in chain(range(ind, self._size), range(0, ind)):
            item = self._arr[ind]
            if item and item[0] == key:
                return item[1]
        else:
            raise KeyError(key)


    def __delitem__(self, key):
        ind = hash(key) % self._size
        for ind in chain(range(ind, self._size), range(0, ind)):
            item = self._arr[ind]
            if item and item[0] == key:
                self._arr[ind] = None
                break
        else:
            raise KeyError(key)


    def __str__(self):
        res = '{'
        for item in self._arr:
            if item:
                res += f'\'{item[0]}\':{item[1]}'
        res += '}'
        return res


    def __repr__(self):
        return self.__str__()