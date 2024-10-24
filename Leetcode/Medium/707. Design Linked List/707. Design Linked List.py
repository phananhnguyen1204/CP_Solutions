class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head, self.tail = Node(0), Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index >= self.size: return -1
        curr_node = self.head
        prev_node = None
        for i in range(0, index + 1):
            prev_node = curr_node
            curr_node = curr_node.next
        return curr_node.val
        

    def addAtHead(self, val: int) -> None:
        next_node = self.head.next
        new_node = Node(val)
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = next_node
        next_node.prev = new_node
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        prev_node = self.tail.prev
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = self.tail
        self.tail.prev = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: return
        curr_node = self.head
        prev_node = None
        for i in range(0, index + 1):
            prev_node = curr_node
            curr_node = curr_node.next
        new_node = Node(val)
        prev_node.next = new_node
        new_node.prev = prev_node
        curr_node.prev = new_node
        new_node.next = curr_node
        self.size += 1


        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size: return
        curr_node = self.head
        prev_node = None
        for i in range(0, index + 1):
            prev_node = curr_node
            curr_node = curr_node.next
        next_node = curr_node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)