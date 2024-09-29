class PriorityQueueList:
    
    def __init__(self):
        self._queue = []

    def insert(self, p, d):
        self._queue.append((p, d))


    def extract_max(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        max_index = 0
        for i in range(1, len(self._queue)):
            if self._queue[i][0] > self._queue[max_index][0]:
                max_index = i
        return self.queue.pop(max_index)

    def peek(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        
        max_index = 0
        for i in range(1, len(self._queue)):
            if self._queue[i][0] > self._queue[max_index][0]:
                max_index = i
        
        return self.queue[max_index]

    def is_empty(self):
        return len(self.queue) == 0

    def __str__(self):
        res = ' '.join([f'({priority}, {item})' 
                        for priority, item in self.queue])
        return 



class PriorityQueueHeap:
    
    def __init__(self):
        self._heap = []

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2

        if index > 0 and self._heap[index][0] > self._heap[parent_index][0]:
            self._swap(parent_index, index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        n = len(self._heap)
        largest = index
        l = 2 * index + 1
        r = 2 * index + 2
        if l < n and self._heap[l][0] > self._heap[largest][0]:
            largest = l
        if r < n and self._heap[r][0] > self._heap[largest][0]:
            largest = r
        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)
        
    def _swap(self, index1, index2):
        self._heap[index1], self._heap[
            index2] = self._heap[index2], self._heap[index1]

    def insert(self, p, d):
        self._heap.append((p, d))
        self._heapify_up(len(self._heap) - 1)

    def extract_max(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        self._swap(0, len(self._heap) - 1)
        max_item = self._heap.pop()
        self._heapify_down(0)
        return max_item

    def peek(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty")
        return self._heap[0]


    def is_empty(self):
        return len(self._heap) == 0


    def __str__(self):
        res = ' '.join([f'({priority}, {item})' 
                        for priority, item in self._heap])
        return res


    def __repr__(self) -> str:
        return self.__str__()