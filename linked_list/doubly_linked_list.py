from typing import List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, value):
        new_node = Node(value=value)
        new_node.next = self.head

        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        
        self.head = new_node

    def append(self, value):
        new_node = Node(value=value)
        new_node.prev = self.tail

        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def remove_last_value(self) -> int:
        if not self.head:
            return None
        deleted_value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        
        return deleted_value

    def remove_first_value(self) -> int:
        if not self.tail:
            return None
        deleted_value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        
        return deleted_value
    
    def print_linked_list_from_head(self) -> List[int]:
        value = self.head
        my_list = []
        while value != None:
            my_list.append(value.value)
            value = value.next
        
        return my_list

dll = DoublyLinkedList()

dll.append(5)
dll.append(4)
dll.append(8)
dll.append(9)
dll.append(7)
dll.prepend(15)
dll.prepend(17)

print(dll.print_linked_list_from_head())

print(dll.remove_first_value())
print(dll.remove_last_value())

print(dll.print_linked_list_from_head())
