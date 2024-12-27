from typing import List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value: int):
        new_node = Node(value= value)

        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
    
    def append(self, value: int):
        new_node = Node(value= value)

        if not self.head:
            self.prepend(value=value)
        else:
            current_node = self.__traverse_linked_list(self.head)
            current_node.next = new_node
        
    def remove_last_value(self) -> int:
        current_node = self.head

        while current_node.next != None and current_node.next.next:
            current_node = current_node.next
        
        removed_value = current_node.next.value
        current_node.next = None

        return removed_value

    def remove_first_value(self) -> int:
        next_head = self.head.next
        removed_value = self.head.value
        self.head = next_head
        return removed_value
    

    def __traverse_linked_list(self, node) -> Node:
        current_node = node
        while current_node.next != None:
            current_node = current_node.next
        
        return current_node
    
    
    def print_linked_list_from_head(self) -> List[int]:
        value = self.head
        my_list = []
        while value != None:
            my_list.append(value.value)
            value = value.next
        
        return my_list
    
    def reverse_linked_list(self):
        current_node = self.head
        previous = None
        
        while current_node != None:
            next = current_node.next
            current_node.next = previous
            previous = current_node
            current_node = next
        
        self.head = previous

    def find_middle_node(self) -> int:
        ahead = self.head

        while ahead != None and ahead.next != None:
            ahead = ahead.next.next
            self.head = self.head.next

        return self.head.value
    
    def verify_if_it_has_cycle(self) -> bool:
        start, end = self.head, self.head

        while end != None and end.next != None:
            end = end.next.next
            start = start.next
            if start == end:
                return True
            
        return False
    
    def mergeTwoLists(self, list1, list2) -> Node:
        merged_list = LinkedList()
        current_node = merged_list
        
        while list1 != None and list2 != None:
            if list1.val > list2.val:
                current_node.next = list2
                list2 = list2.next
            else:
                current_node.next = list1
                list1 = list1.next

            current_node = current_node.next
        
        if list1 != None:
            current_node.next = list1
        else:
            current_node.next = list2

        
        return merged_list.next

ll = LinkedList()

ll.append(5)
ll.append(4)
ll.prepend(15)
ll.prepend(17)

print(ll.print_linked_list_from_head())
ll.reverse_linked_list()
print(ll.print_linked_list_from_head())
print(ll.find_middle_node())

