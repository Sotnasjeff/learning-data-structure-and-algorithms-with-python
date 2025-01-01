# Worst time complexity: O(n log n) 
# Merge sort is excelent to sort linked list

from typing import List

class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
   


def find_middle(list: Node) -> Node:
    start, end = list, list.next

    while end != None and end.next != None:
        start = start.next
        end = end.next
    
    return start

def merge(list1: Node, list2: Node) -> Node:
    merged_list = Node()
    helper_pointer = merged_list

    while list1 != None and list2 != None:
        if list1.value > list2.value:
            helper_pointer.next = list2
            list2 = list2.next
        else:
            helper_pointer.next = list1
            list1 = list1.next
        helper_pointer = helper_pointer.next
    
    if list1:
        helper_pointer.next = list1
    else:
        helper_pointer.next = list2
    
    return merged_list.next

def mergesort(list: Node) -> Node:
    if not list or not list.next:
        return list
    
    middle = find_middle(list)
    after_middle = middle.next
    middle.next = None
    left = mergesort(list)
    right = mergesort(after_middle)

    sorted_list = merge(left, right)

    return sorted_list

def print_linked(my_value: Node) -> List[int]:
    current_node = my_value
    helper = []

    while current_node.next:
        helper.append(current_node.value)
        current_node = current_node.next
    
    return helper


my_linked = Node()

node5 = Node(5)
node2 = Node(2, next=node5)
node15 = Node(15,next=node2)
node19 = Node(19,next=node15)
node3 = Node(3,next=node19)
my_linked = Node(80,next=node3)

print(print_linked(my_linked))
my_linked = mergesort(my_linked)
print(print_linked(my_linked))