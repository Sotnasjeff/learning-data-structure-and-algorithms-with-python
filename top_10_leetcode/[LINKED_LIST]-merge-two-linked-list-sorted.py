from typing import List

class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

def merge_two_linked_list(list1: Node, list2: Node) -> Node:
    dummy = Node()
    current_node = dummy
    
    while list1 != None and list2 != None:
        if list1.value > list2.value:
            current_node.next = list2
            list2 = list2.next
        else:
            current_node.next = list1
            list1 = list1.next
        current_node = current_node.next
    
    if list1:
        current_node.next = list1
    else:
        current_node.next = list2
    
    return dummy.next   


def printLinked(list: Node) -> List[int]:
    result = []
    
    while list != None:
        result.append(list.value)
        list = list.next
    
    return result

my_linked_final = Node(25)
my_linked_what = Node(20, my_linked_final)
mi_lista_ligada = Node(15, my_linked_what)
my_lista_linked = Node(3, mi_lista_ligada)

my_linked_listed = Node(24)
muy_ligada = Node(17, my_linked_listed)
mi_list_ligada = Node(5, muy_ligada)

my_merged_list = merge_two_linked_list(my_lista_linked, mi_list_ligada)
print(printLinked(my_merged_list))

