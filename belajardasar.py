class Node:
    def __init__(self, element, next=None):
        self.element = element
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def addFirst(self, element):
        if self.isEmpty() :
            self.front = Node(element)
            self.back = self.front
        
        else :
            temp = self.front
            self.front = Node(element, temp)
        
        self.size += 1
    
    def addLast(self, element):
        if self.isEmpty():
            self.front = Node(element)
            self.back = self.front
        
        else : 
            self.back.next = Node(element)
            self.back = self.back.next

        self.size += 1

    def clear(self):
        return self.size == 0

    def printList(self):
        print("Isi Linked List")
        current = self.front
        while current != None :
            print(current.element)
            current = current.next

def main():
    li = LinkedList()

    li.addFirst(10)

    li.addLast(12)

    li.addLast(11)

    li.addFirst(13)

    li.printList()

    li.clear()
    
    li.printList()


if __name__ == "__main__":
    main()
