class Node():
    def __init__(self, data):
        self.data = data
        self._next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add(self, data) -> None:
        if data == None:
            raise TypeError("None type is not allowed")
        if self.size == 0:
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
            return
        
        curr = self.head
        while curr._next != None:
            curr = curr._next
    
        curr._next = Node(data)
        self.tail = curr._next
        self.size += 1
            
        
    def remove(self, data) -> None:
        if data == None:
            raise TypeError("None type is not allowed")
        if self.size == 0:
            raise AttributeError("There is no data")
        if self.size == 1:
            del self.head
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
        if self.size == 0:
            raise AttributeError("There is no data")
        if index > self.size:
            raise IndexError("Desired index is larger than the size")
        if index == 0:
            dummy = self.head
            self.head = Node(data)
            self.head._next = dummy
            dummy = None
            del dummy
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
    
    def find(self, data) -> Node:
        if data == None:
            raise TypeError("None type is not allowed")
        if self.size == 0:
            raise AttributeError("There is no data")
        
        curr = self.head
        while curr._next != None:
            if curr.data == data:
                return curr
            
            curr = curr._next
        
        
        raise ValueError(f"{data} was not found")
    
    def index(self, index: int) -> Node:
        if index < 0:
            ValueError("Invalid Index")
        if index == 0:
            return self.head
        if index == self.size:
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
                    
        self.head = prev
        
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
        values = self.all_data()
        visual = ""
        
        for value in values:
            visual += (str(value) + " " + point + " ")
        
        print(visual)    
        
if __name__ == "__main__":
    linkedlist = LinkedList()
    linkedlist.add(1)
    linkedlist.add(2)
    linkedlist.add(5)
    linkedlist.add("Hello")
    
    linkedlist.remove(5)
    linkedlist.add_index(100.0, 2)
    print(linkedlist.all_data())
    linkedlist.visualization()
    
    linkedlist.reverse()
    linkedlist.visualization()
    print(linkedlist.index(0).data)


