from typing import Any, Optional, List

class Stack():
    def __init__(self):
        self._items: List[Any] = []

    def push(self, item):
        self._items.append(item)
    
    def is_empty(self):
        return len(self._items) == 0

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._items[-1]

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

# Example

numbers = Stack()
numbers.push(1)
numbers.push(2)
numbers.push(3)

print(numbers)

numbers.pop()

print(numbers)
print(f"At top of the stack {numbers.peek()}")
print(f"Stack size: {numbers.size()}")

while not numbers.is_empty():
    print(numbers.pop())

print(numbers.is_empty())