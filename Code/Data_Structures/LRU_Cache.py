from Linked_List import DoublyLinkedList

class LRU:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.frequencyList = DoublyLinkedList()
        self.cache = {}
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        value = self.cache[key]
        self.frequencyList.remove((key, value))
        self.frequencyList.add_index(0, (key, value))
        return value
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old = self.cache[key]
            self.cache[key] = value
            self.frequencyList.remove((key, old))
            self.frequencyList.add_index(0, (key, value))
            return
        
        self.cache[key] = value
        self.frequencyList.add_index(0, (key, value))
        if self.size + 1 > self.capacity:
            last = self.frequencyList.getTail().data
            self.frequencyList.remove(last)
            del self.cache[last[0]]
            return 

        self.size += 1
        return
     

def LRU_Test_Cases():
    lru = LRU(2)
    lru.put(1,1)
    lru.put(2,2)
    lru.get(1)
    lru.put(3,3)
    lru.get(3)
    lru.get(4)

if __name__ == "__main__":
    LRU_Test_Cases()