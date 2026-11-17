class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = Node(0)
        self.size = 0

    def get(self, index: int) -> int:
        curr = self.head.next
        if index < self.size and index>=0:
            for i in range(index):
                curr = curr.next
            return curr.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        self.size+=1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        curr = self.head
        while(curr.next):
            curr = curr.next
        curr.next = node
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
        elif index > self.size:
            return
        else:
            curr = self.head
            for i in range(index):
                curr = curr.next
            node = Node(val)
            node.next = curr.next
            curr.next = node
            self.size+=1   

    def deleteAtIndex(self, index: int) -> None:
        if index>=0 and index<self.size:
            curr = self.head
            for i in range(index):
                curr = curr.next
            curr.next = curr.next.next
            self.size-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)