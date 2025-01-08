from typing import List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0
    
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size +=1
    
    def pop(self):
        if self.top is None:
            raise IndexError("Empty Stack")
        
        popped_node = self.top
        self.top = popped_node.next
        self._size -=1

        return popped_node.value

    def peek(self):
        if self.top is None:
            raise IndexError("Empty Stack")
        
        return self.top.value

    def size(self):
        return self._size

def is_valid(s: str) -> bool:
    hash = {")":"(", "]":"[", "}":"{"}
    stack = []
    for char in s:
        if char in hash:
            if stack and stack[-1] == hash[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    
    return not len(stack)

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    result = [0] * len(temperatures)
    stack = []

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            index = stack.pop()
            result[index] = i - index
        stack.append(i)
    
    return result

#print(is_valid("[()]"))
print(dailyTemperatures([73,74,75,71,69,72,76,73]))
