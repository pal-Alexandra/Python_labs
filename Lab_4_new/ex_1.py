# Write a Python class that simulates a Stack.
# The class should implement methods like
# push, pop, peek (the last two methods should return None
# if no element is present in the stack).

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]


stack = Stack()
stack.push(1)
stack.push([2, 3])
stack.push("Ana")
print("THE STACK")
print(stack.stack)

print("pop OPERATION")
print(stack.pop())
print("THE STACK AFTER pop OPERATION")
print(stack.stack)

print("peek OPERATION")
print(stack.peek())
print("THE STACK AFTER peek OPERATION")
print(stack.stack)


