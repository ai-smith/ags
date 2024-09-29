class QueueFullException(Exception):
    pass


class QueueEmptyException(Exception):
    pass


class Queue:    
    def __init__(self, k):
        self._queue = [None] * k
        self._size = k
        self._front = self._rear = -1


    def enqueue(self, d):
        if self._rear == self._size - 1:
            raise QueueFullException('Queue is full.')
        elif self._front == -1:
            self._front = self._rear = 0
            self._queue[self._rear] = d
        else:
            self._rear += 1
            self._queue[self._rear] = d


    def dequeue(self):
        if self._rear == -1:
            raise QueueEmptyException('Queue is empty.')
        elif self._front == self._rear:
            res = self._queue[self._front]
            self._front = self._rear = -1
            return res
        else:
            res = self._queue[self._front]
            self._front += 1
            return res


    def is_empty(self):
        if self._rear != -1:
            return False
        else:
            return True


    def is_full(self):
        if self._rear != self._size - 1:
            return False
        else:
            return True

    def peek(self):
        if self._rear == -1:
            raise QueueEmptyException('Queue is empty.')
        else:
            return self._queue[self._front]