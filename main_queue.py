class Queue: #очередь
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item): #добавление элементов в конец очереди
        self.items.insert(0, item)

    def dequeue(self): #удаление первого элемента очереди
        return self.items.pop()

    def size(self):
        return len(self.items)


stack = Queue()
print(stack.is_empty())

stack.enqueue('Действие 1')
stack.enqueue('Действие 2')
stack.enqueue('Действие 3')
stack.enqueue('Действие 4')

print(stack.is_empty())
print(stack.size())
print(stack.dequeue())
print(stack.size())
