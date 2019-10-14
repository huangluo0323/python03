class Deque:
    '''双端队列'''

    def __init__(self):
        self.items = []

    def is_empty(self):
        #判断是否为空
        return self.items == []

    def add_front(self,item):
        #队列头部添加元素
        self.items.insert(0,item)

    def add_rear(self,item):
        #队列尾部添加元素
        self.items.append(item)

    def get_front(self):
        #从头部删除元素
        return self.items.pop(0)

    def get_rear(self):
        #从尾部删除元素
        return self.items.pop()

    def size(self):
        #返回队列的大小
        return len(self.items)

    def __str__(self):
        return f'{self.items}'


if __name__ == '__main__':
    d =Deque()
    d.add_front(1)
    d.add_front(2)
    d.add_rear(3)
    d.add_rear(4)
    print(d)
    print(d.size())
    print(d.get_front())
    print(d.get_front())
    print(d.get_rear())
    print(d.get_rear())