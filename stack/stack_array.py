class Stack:
    def __init__(self):
            self.items = []
    
    def push(self, item):
          self.items.append(item)

    def is_empty(self) -> bool:
          return len(self.items) == 0
    
    def pop(self):
          if self.is_empty():
                return IndexError("Empty list")

          return self.items.pop()
    
    def peek(self):
          if self.is_empty():
                raise IndexError("Empty Stack")

          return self.items[-1]

    def size(self):
          return len(self.items)