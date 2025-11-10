from Linked_List import DoublyLinkedList
from Linked_List import Node

class SpecializedLinkedList(DoublyLinkedList):
    def __init__(self):
       super().__init__()
    
    def getTail(self) -> Node:
        return self.tail
    
    def add_Node(self, data: tuple) -> Node:
        if self.size == 0:
            new = Node(data)
            self.head = new
            self.tail = new
            self.size += 1
            return new 
        
        new = Node(data)
        head = self.head
        new._next = head
        head._prev = new
        self.head = new
        self.size += 1
        return new
    
    def refresh_Node(self, node: Node, newData: tuple) -> Node | int:
        if self.size == 0:
            raise IndexError("There is currently no data")
        if self.size == 1 or node == self.head:
            node.data = newData
            return node 
        if node == self.tail:
            node.data = newData
            head = self.head
            newTail = node._prev
            newTail._next = None
            node._next = head
            node._prev = None
            head._prev = node
            self.head = node
            self.tail = newTail
            return node
        
        node.data = newData
        head = self.head
        prev = node._prev
        nexts = node._next
        prev._next = nexts
        nexts._prev = prev
        node._next = head
        node._prev = None
        head._prev = node
        self.head = node
        return node

    def remove_Node(self, node: Node) -> None:
        if self.size == 0:
            raise IndexError("There is no data")
        if self.size == 1:
            self.head = self.tail = None
            self.size -= 1
            return
        if node == self.head:
            self.head = node._next
            self.head._prev = None
        elif node == self.tail:
            self.tail = node._prev
            self.tail._next = None
        else:
            prev, nexts = node._prev, node._next
            prev._next = nexts
            nexts._prev = prev
       
        self.size -= 1
        return

class LRU:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.recencyList = SpecializedLinkedList()
        self.cache = {}
    
    def showCache(self):
        print(self.cache)
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            raise ValueError(f"{key} is not in the cache")
        
        cached = self.cache[key]
        self.recencyList.refresh_Node(cached[1], (key, cached[0]))
        return cached[0]
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old = self.cache[key]
            refresh = self.recencyList.refresh_Node(old[1], (key, value))
            self.cache[key] = (value, refresh)
            return
        
        newNode = self.recencyList.add_Node((key, value))
        self.cache[key] = (value, newNode)
        if self.size + 1 > self.capacity:
            last = self.recencyList.getTail()
            del self.cache[last.data[0]]
            self.recencyList.remove_Node(last)
            return 

        self.size += 1
        return
     

def LRU_Test_Cases():
    lru = LRU(2)
    lru.put(1,1)
    lru.put(2,2)
    print(lru.get(1))
    lru.put(3,3)
    print(lru.get(3))
    lru.showCache()

if __name__ == "__main__":
    LRU_Test_Cases()