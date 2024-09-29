
class DequeFullException(Exception):
    pass
    

class DequeEmptyException(Exception):
    pass


class Deque:
    
    def __init__(self, k):
        self._data = [0] * k
        self._size = k
        self._front = self._rear = -1

    def __str__(self):
        res = '|'
        cur = self._front
        end = self._rear
        while cur % self._size != end:
            res += f' {self._data[cur % self._size]}' 
            cur += 1
        if cur != -1:
            res += f' {self._data[cur % self._size]}' 
        res += ' |'
        return res

    def __repr__(self):
        return self.__str__()

    def is_empty(self):
        return self._front == -1

    def add_rear(self, item):
        if self._front == -1:
            self._front = self._rear = 0
            self._data[0] = item
        elif (self._rear + 1) % self._size != self._front:
            self._rear = (self._rear + 1) % self._size
            self._data[self._rear] = item
        else:
            raise DequeFullException('Deque is full.')

    def add_front(self, item):
        if self._front == -1:
            self._front = self._rear = 0
            self._data[0] = item
        elif (self._front - 1) % self._size != self._rear:
            self._front = (self._front - 1) % self._size
            self._data[self._front] = item
        else:
            raise DequeFullException('Deque is full.')

    def remove_front(self):
        if self._front == -1:
            raise DequeEmptyException('Deque is empty.')
        elif self._front == self._rear:
            val = self._data[self._front]
            self._front = self._rear = -1
            return val

        else:
            val = self._data[self._front]
            self._front = (self._front + 1) % self._size
            return val
            
    def remove_rear(self):
        if self._rear == -1:
            raise DequeEmptyException('Deque is empty.')
        elif self._front == self._rear:
            val = self._data[self._rear]
            self._front = self._rear = -1
            return val
        else:
            val = self._data[self._rear]
            self._rear = (self._rear - 1) % self._size
            return val

    def size(self):
        if self._front == -1:
            return 0
        elif self._front <= self._rear:
            return self._rear - self._front + 1
        length = self._rear % self._size - self._front % self._size + 1
        return length