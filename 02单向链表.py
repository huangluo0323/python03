class SingleNode():
    def __init__(self, item):
        self.item = item
        self.next = None


class SingleLinkList:
    '''单向链表'''
    def __init__(self):
        self.__head = None

    def is_empty(self):
        '''判断链表是否为空'''
        return self.__head == None

    def length(self):
        '''链表的长度'''
        cur = self.__head
        count = 0
        while cur != None:
            cur = cur.next
            count += 1
        return count

    def travel(self):
        '''遍历链表'''
        cur = self.__head
        while cur != None:
            print(cur.item)
            cur = cur.next

    def add(self, item):
        '''头部添加数据'''
        node = SingleNode(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        '''在尾部插入数据'''
        if self.is_empty():
            self.add(item)
            return
        node = SingleNode(item)
        cur = self.__head
        while cur.next != None:
            cur = cur.next
        cur.next = node

    def insert(self, pos, item):
        '''在指定位置插入元素'''
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0
            pre = self.__head
            while count < pos - 1:
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        cur = self.__head
        pre = None
        while cur != None:
            if cur.item == item:
                if not pre:
                    # 如果第一个就是要删除的节点
                    self.__head = cur.next
                else:
                    # 如果不是第一个节点
                    pre.next = cur.next
                break
            else:
                # 往后移动
                pre = cur
                cur = cur.next

    def search(self, item):
        '''查找元素是否存在'''
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


if __name__ == '__main__':
    L1 = SingleLinkList()
    L1.add(1)
    L1.add(2)
    L1.add(3)
    L1.travel()
    print(L1.length())
    print('-------------------------------------')
    L1.append('hahaa')
    L1.insert(1,'xixi')
    L1.travel()
    print(L1.search('1'))
    print(L1.search(1))
    L1.remove('xixi')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    L1.travel()