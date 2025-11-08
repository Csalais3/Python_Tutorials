class Node():
    def __init__(self, data):
        self.data = data
        self._next = None
        self._prev = None
        
class SinglyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def getHead(self) -> Node | None:
        return self.head
    
    def getTail(self) -> Node | None:
        return self.tail
    
    def getSize(self) -> int:
        return self.size
    
    def isEmpty(self) -> bool:
        return self.size == 0
    
    def add(self, data) -> None:
        if data == None:
            raise TypeError("None type is not allowed")
        if self.size == 0:
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
            return
        
        self.tail._next = Node(data)
        self.tail = self.tail._next
        self.size += 1
            
    def remove(self, data) -> None:
        if data == None:
            raise TypeError("None type is not allowed")
        if self.size == 0:
            raise AttributeError("There is no data")
        if self.size == 1:
            if self.head.data == data:
                del self.head
                self.head = None
                self.tail = None
                self.size -= 1
                return
            raise ValueError(f"{data} was not found")
        if self.head.data == data:
            dummy = self.head
            self.head = self.head._next

            if self.head is None:
                self.tail == None
            del dummy
            self.size -= 1
            return
        
        curr = self.head
        while curr._next != None:
            if curr._next == self.tail:
                self.tail = curr
            if curr._next.data == data:
                dummy = curr._next
                curr._next = dummy._next
                del dummy
                self.size -= 1
                return
            curr = curr._next
        
        raise ValueError(f"{data} was not found")
        
    def add_index(self, data, index) -> None:
        if data == None:
            raise TypeError("None type is not allowed")
        if index < 0 or index > self.size:
            raise IndexError("Desired index is larger than the size")
        if index == 0:
            dummy = self.head
            self.head = Node(data)
            self.head._next = dummy
            self.size += 1
            return
        if index == self.size:
            self.add(data)
            return
        
        curr = self.head
        for i in range(index - 1):
            curr = curr._next
        
        dummy = curr._next
        curr._next = Node(data)
        curr._next._next = dummy
        dummy = None
        del dummy
        self.size += 1
        
    def remove_index(self, index: int) -> None:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        if self.size == 0:
            raise AttributeError("There is no data")
        
        curr = self.head
        if index == 0:
            self.head = curr._next
            if self.size == 1:
                self.tail = None
            del curr
            self.size -=1
            return 

        for i in range(index):
            prev = curr
            curr = curr._next
        
        nexts = curr._next
        
        if curr._next is None:
            self.tail = prev
            
        prev._next = nexts
        self.size -= 1
        
    def find(self, data) -> Node:
        if data == None:
            raise TypeError("None type is not allowed")
        if self.size == 0:
            raise AttributeError("There is no data")
        
        curr = self.head
        while curr != None:
            if curr.data == data:
                return curr
            
            curr = curr._next
        
        
        raise ValueError(f"{data} was not found")
    
    def index(self, index: int) -> Node:
        if index < 0 or index >= self.size:
            raise ValueError("Index out of range")
        if index == 0:
            return self.head
        if index == self.size - 1:
            return self.tail
        
        curr = self.head
        for i in range(index):
            curr = curr._next
        
        return curr
            
    def all_data(self) -> list:
        if self.size == 0:
            return []
        
        values = []
        curr = self.head
        while curr != None:
            values.append(curr.data)
            curr = curr._next
    
        return values
    
    def reverse(self) -> None:
        if self.size == 0:
            raise AttributeError("There is no list")
        if self.size == 1:
            return
        
        curr = self.head
        prev = None
        while curr != None:
            next = curr._next
            curr._next = prev
            prev = curr
            curr = next
                    
        self.tail, self.head = self.head, prev
        
        # tail = self.reverseh(self.head, None)
        # self.head = tail

    ## For Recursive solution
    def reverseh(self, next: Node, prev: Node) -> Node | None:
        current = next
        next = current._next
        current._next = prev
                        
        if next != None:
            current = self.reverseh(next, current)

        return current
    

    def visualization(self) -> None:
        if self.size == 0:
            return
        
        point = "-->"
        visual = ""
        
        curr = self.head
        while curr != None:
            visual += f" {curr.data} {point}"
            curr = curr._next
        
        print(visual)    


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def getHead(self) -> Node | None:
        return self.head
    
    def getTail(self) -> Node | None:
        return self.tail
    
    def getSize(self) -> int:
        return self.size
    
    def isEmpty(self) -> bool:
        return self.size == 0
    
    def add(self, data: int) -> None:
        if data == None:
            raise ValueError("NoneType is not allowed")
        if self.isEmpty():
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
            return

        prev = self.tail
        new = Node(data)
        prev._next = new
        new._prev = prev
        self.tail = new
        self.size += 1
        
    def remove(self, data) -> None:
        if data == None:
            raise ValueError("NoneType data is not allowed")
        if  self.isEmpty():
            raise ValueError("There is no data to remove")
        if self.size == 1:
            if data == self.head.data:
                del self.head
                self.size -= 1
                return
            raise ValueError(f"{data} was not found")
        
        if data == self.head.data:
            curr = self.head
            self.head = self.head._next
            del curr
            self.head._prev = None
            self.size -= 1
            return
        if data == self.tail.data:
            curr = self.tail
            self.tail = self.tail._prev
            del curr
            self.tail._next = None
            self.size -= 1
            return
        
        curr1 = self.tail
        curr2 = self.head
        while curr1 and curr2 and curr1 != curr2 and curr1._prev != curr2:
            curr1 = curr1._prev
            curr2 = curr2._next
            if curr1.data == data:
                prev = curr1._prev
                nexts = curr1._next
                prev._next = nexts
                nexts._prev = prev
                del curr1
                self.size -= 1
                return
            if curr2.data == data:
                prev = curr2._prev
                nexts = curr2._next
                prev._next = nexts
                nexts._prev = prev
                del curr2
                self.size -= 1
                return

        if curr1 == curr2 and curr1.data == data:
            prev = curr1._prev
            nexts = curr1._next
            if prev: 
                prev._next = nexts
            if nexts: 
                nexts._prev = prev
            del curr1
            self.size -= 1
            return
        
        raise ValueError(f"{data} was not found")  
    
    def add_index(self, index: int, data) -> None:
        if data == None:
            raise ValueError("NoneType data is not allowed")
        if index < 0 or index > self.size:
            raise IndexError(f"{index} is out of range")
        if self.size == 0:
            self.add(data)
            return
        if index == 0:
            head = self.head
            new = Node(data)
            new._next = head
            head._prev = new
            self.head = new 
            self.size += 1
            return
        if index == self.size:
            tail = self.tail
            new = Node(data)
            new._prev = tail
            tail._next = new
            self.tail = new
            self.size += 1
            return
        if self.size == 1:
            self.add(data)
            return
        
        if index > self.size // 2:
            curr = self.tail
            for i in range(self.size - index):
                curr = curr._prev
            
            prev = curr._prev
            new = Node(data)
            prev._next = new
            curr._prev = new
            new._next = curr
            new._prev = prev
            self.size += 1
            return
        
        curr = self.head
        for i in range (index):
            curr = curr._next
        
        prev = curr._prev
        new = Node(data)
        prev._next = new
        curr._prev = new
        new._next = curr
        new._prev = prev
        self.size += 1 
        return
    
    def remove_index(self, index: int) -> None:
        if index < 0 or index >= self.size:
            raise IndexError(f"{index} is out of range")
        
        if index == 0:
            curr = self.head
            self.head = curr._next
            self.head._prev = None
            del curr
            self.size -= 1
            return
        if index == self.size -1:
            curr = self.tail
            self.tail = curr._prev
            self.tail._next = None
            del curr
            self.size -= 1
            return

        if index > self.size // 2:
            curr = self.tail
            for i in range(self.size - index):
                curr = curr._prev
            
            prev = curr._prev
            nexts = curr._next
            prev._next = nexts
            nexts._prev = prev
            del curr
            self.size -= 1
            return 
            
        curr = self.head
        for i in range(index):
            curr = curr._next
        
        prev = curr._prev
        nexts = curr._next
        prev._next = nexts
        nexts._prev = prev
        del curr
        self.size -= 1
        return 
            
    def find(self, data) -> Node:
        if data == None:
            raise ValueError("NoneType data is not allowed")
        
        if self.head.data == data:
            return self.head
        if self.tail.data == data:
            return self.tail
        
        curr1 = self.head
        curr2 = self.tail
        while curr1 and curr2 and curr1 != curr2 and curr1._prev != curr2:
            curr1 = curr1._next
            curr2 = curr2._prev
            
            if curr1.data == data:
                return curr1
            if curr2.data == data:
                return curr2
        
        raise ValueError(f"{data} was not found")
            
    def index(self, index: int) -> Node:
        if index < 0 or index >= self.size:
            raise ValueError("Invalid Index")
        if index == 0:
            return self.head
        
        if index > self.size // 2:
            curr = self.tail
            for i in range(self.size - index - 1):
                curr = curr._prev
            
            return curr
        
        curr = self.head
        for i in range(index):
            curr = curr._next
        
        return curr
    
    def all_data(self) -> list:    
        if self.isEmpty():
            return []
        
        values = []
        curr = self.head
        while curr != None:
            values.append(curr.data)
            curr = curr._next
        
        return values
    
    def reverse(self) -> None:
        if self.size == 0 or self.size == 1:
            return 
    
        curr = self.head
        prev = None
        while curr:
            nexts = curr._next
            curr._next = prev
            curr._prev = nexts
            prev = curr
            curr = nexts
            
        self.tail = self.head
        self.head = prev
            
    def visualize(self):
        out = ""
        pointer = "<-->"
        
        curr = self.head
        while curr != None:
            out += f" {curr.data} {pointer}"
            curr = curr._next
        
        print(out)
        
        
def SinglyLinkedListTests():
    linkedlist = SinglyLinkedList()
    linkedlist.add(6)
    linkedlist.remove(6)
    linkedlist.add(1)
    linkedlist.add(2)
    linkedlist.add(5)
    linkedlist.add("Hello")
    
    linkedlist.remove(5)
    linkedlist.add_index(100.0, 2)
    print(linkedlist.all_data())
    linkedlist.visualization()
    
    linkedlist.reverse()
    linkedlist.remove_index(0)
    linkedlist.visualization()
    print(linkedlist.index(0).data)
    
    
def DoublyLinkedListTests():
    dlinkedlist = DoublyLinkedList()
    
    dlinkedlist.add(3)
    dlinkedlist.add(7)
    dlinkedlist.add(100)
    dlinkedlist.add(4.3)
    dlinkedlist.add("Hello")
    
    dlinkedlist.remove(4.3)
    dlinkedlist.remove_index(0)
    print(dlinkedlist.find(100))
    print(dlinkedlist.find(100).data)
    print(dlinkedlist.all_data())
    dlinkedlist.visualize()
    
    dlinkedlist.reverse()
    dlinkedlist.visualize()


if __name__ == "__main__":
    SinglyLinkedListTests()
    DoublyLinkedListTests()


