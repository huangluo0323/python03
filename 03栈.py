class Stack:
    '''栈'''
    def __init__(self):
        self.items = []

    def is_empty(self):
        #判断是否为空
        return self.items == []

    def push(self,item):
        #加入元素
        self.items.append(item)

    def pop(self):
        '''弹出元素'''
        return self.items.pop()

    def peek(self):
        '''返回栈顶元素'''
        return self.items[len(self.items)-1]

    def size(self):
        '''栈的大小'''
        return len(self.items)

    def __str__(self):
        return f'{self.items}'

if __name__ == '__main__':
    s = Stack()

    s.push('hello')
    s.push('world')
    s.push('python')
    print(s)
    print(s.size())
    print(s.peek())
    print(s.pop())
    print(s.pop())
    print(s.pop())