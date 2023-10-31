# Write a Python class that simulates a Queue.
# The class should implement methods
# like push, pop, peek
# (the last two methods should return None
# if no element is present in the queue).

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, element):
        self.queue.append(element)

    def pop(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[0]

queue = Queue()
queue.push(1)
queue.push('a')
queue.push([2, 3])
print("THE QUEUE")
print(queue.queue)

print("pop OPERATION")
print(queue.pop())
print("THE QUEUE AFTER pop OPERATION")
print(queue.queue)

print("peek OPERATION")
print(queue.peek())
print("THE QUEUE AFTER peek OPERATION")
print(queue.queue)