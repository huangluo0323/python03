class Queue:
    '''队列'''

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def put(self, item):
        self.items.insert(0, item)

    def get(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
        return f'{self.items}'

if __name__ == '__main__':
    q = Queue()
    q.put('hello')
    q.put('world')
    q.put('python')
    print(q)
    print(q.size())
    print(q.get())
    print(q.get())
    print(q.get())
