class FibonacciHeapNode:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.parent = None
        self.child = None
        self.degree = 0
        self.mark = False
        self.next = self
        self.prev = self

    def __str__(self):
        return f'Node(key={self.key}, data={self.data})'

    def __repr__(self):
        return self.__str__()


class FibonacciHeap:
    def __init__(self):
        self._min_node = None
        self._total_nodes = 0

    def __str__(self):
        return self._str_tree(self._min_node)

    def __repr__(self):
        return self.__str__()

    def _str_tree(self, node, indent="root"):
        current = node
        res = ''
        if current is None:
            return res
        if indent == 'root':
            res += indent
            indent = ''
        flag = True
        while current != node or flag:
            if current == node:
                flag = False
            if current.next == node:
                arrow = "└── "
                child_indent = "    "
            else:
                arrow = "├── "
                child_indent = "│   "
            res += ('\n' + indent + arrow + f'{current.key} (degree: {current.degree}, data: {current.data})')
            if current.child:
                res += self._str_tree(current.child, indent + child_indent)
            current = current.next
        return res

    def _add_node(self, root, node):
        node.prev.next = root.next
        root.next.prev = node.prev
        node.prev = root
        root.next = node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node
        node.prev = node

    def _iterate(self, head):
        node = head
        flag = True
        while node != head or flag:
            if node == head:
                flag = False
            yield node
            node = node.next

    def _consolidation(self):
        aux = [None] * self._total_nodes.bit_length()
        for x in [n for n in self._iterate(self._min_node)]:
            while aux[x.degree]:
                y = aux[x.degree]
                if x.key > y.key:
                    x, y = y, x
                aux[x.degree] = None
                self._remove_node(y)
                y.parent = x
                if x.child:
                    self._add_node(x.child, y)
                else:
                    x.child = y
                x.degree += 1
            aux[x.degree] = x
        self._min_node = None
        for node in aux:
            if node:
                if self._min_node:
                    if node.key < self._min_node.key:
                        self._min_node = node
                else:
                    self._min_node = node

    def _cascading(self, node):
        parent = node.parent
        if parent is not None:
            if not node.mark:
                node.mark = True
            else:
                if node.right == node:
                    parent.child = None
                else:
                    parent.child = node.right
                    self._remove_node(node)
                node.parent = None
                self._add_node(self._min_node, node)
                node.mark = False
                self._cascading(parent)
                
    def insert(self, key, data=None):
        new_node = FibonacciHeapNode(key, data)
        if self._min_node is None:
            self._min_node = new_node
        else:
            self._add_node(self._min_node, new_node)
            if new_node.key < self._min_node.key:
                self._min_node = new_node
        self._total_nodes += 1

    def extract_min(self):
        min_node = self._min_node
        if min_node:
            if min_node.child:
                child = min_node.child
                while True:
                    child.parent = None
                    child = child.next
                    if child == min_node.child:
                        break
                min_node.child = None
                self._add_node(min_node, child)
            if min_node.next == min_node:
                self._min_node = None
            else:
                self._min_node = min_node.next
                self._remove_node(min_node)
                min_node.parent = None
                self._consolidation() 
            self._total_nodes -= 1
        return min_node

    def decrease_key(self, node, key):
        if key > node.key:
            ValueError('Key is bigger then existing.')
        node.key = key
        parent = node.parent
        if parent is not None and key < parent.key:
            if node == node.next:
                parent.child = None
            else:
                parent.child = node.next
            self._remove_node(node)
            node.parent = None
            parent.degree -= 1
            self._add_node(self._min_node, node)
            node.mark = False
            self._cascading(parent)
        if node.key < self._min_node:
            self._min_node = node

    def delete(self, node):
        self.decrease_key(node, float('-inf'))
        self.extract_min()
            
    def find_min(self):
        if self._min_node:
            return self._min_node.key
        
    def union(self, other):
        if other._min_node is None:
            return
        elif self._min_node is None:
            self._min_node = other._min_node
        else:
            self._add_node(self._min_node, other._min_node)
        self._total_nodes += other._total_nodes
        