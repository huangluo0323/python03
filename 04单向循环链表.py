class SingleCycleNode():
    '''单向循环链表的节点'''

    def __init__(self, item):
        self.item = item
        self.next = None


class SingleCycleLinkList:
    '''单向循环链表'''

    def __init__(self):
        self.__head = None

    def is_empty(self):
        '''判断链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表长度'''
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        '''遍历链表'''
        if self.is_empty():
            return
        cur = self.__head
        print(cur.item)
        while cur.next != self.__head:
            cur = cur.next
            print(cur.item)

    def insert(self, pos, item):
        '''在指定位置插入元素'''
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = SingleCycleNode(item)
            count = 0
            pre = self.__head
            while count < pos - 1:
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def add(self, item):
        # 头部添加节点
        node = SingleCycleNode(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            # 要添加的节点的next指向原来的第一个节点
            node.next = self.__head
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 最后一个节点的next 指向要插入的节点
            cur.next = node
            # head 指向了要插入的节点
            self.__head = node

    def append(self, item):
        '''尾部添加节点'''
        node = SingleCycleNode(item)
        if self.is_empty():
            self.__head = node
            node.next = self.__head
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            # 将尾节点指向node
            cur.next = node
            # 将node的next指向第一个节点
            node.next = self.__head

    def search(self, item):
        '''查找节点是否存在'''
        if self.is_empty():
            return False

        cur = self.__head

        if cur.item == item:
            return True
        while cur.next != self.__head:
            cur = cur.next
            if cur.item == item:
                return True
        return False

    def remove(self, item):
        '''删除节点'''
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.item == item:
                # 判断是否是头节点
                if cur == self.__head:
                    # 如果是头节点，则找到尾节点
                    tail = self.__head
                    while tail.next != self.__head:
                        tail = tail.next
                    # 将head指向头结点的下一个节点
                    self.__head = cur.next
                    # 将尾部的节点的next 指向头结点
                    tail.next = self.__head
                else:
                    # 要删除节点不是头节点
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        # cur 指向了尾节点
        if cur.item == item:
            # 只有一个节点
            if cur == self.__head:
                self.__head = None
            else:
                pre.next = self.__head

if __name__ == '__main__':
    L2 = SingleCycleLinkList()
    L2.add(11)
    L2.add(22)
    L2.add(33)
    L2.travel()
    print('----------------------------')
    L2.append('haha')
    L2.travel()
    print('----------------------------')
    L2.insert(1,2333)
    L2.travel()
    print(L2.length())
    print('----------------------------')
    print(L2.search(2333))
    L2.remove('haha')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    L2.travel()

