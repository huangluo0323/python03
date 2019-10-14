class DoubleNode:
    # 双向链表的节点
    def __init__(self, item):
        self.item = item
        self.next = None
        self.pre = None


class DoubleLinkList:
    def __init__(self):
        self.__head = None

    def is_empty(self):
        # 判断链表是否为空
        return self.__head == None

    def length(self):
        # 链表的长度
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # 遍历链表
        cur = self.__head
        while cur:
            print(cur.item)
            cur = cur.next

    def search(self, item):
        # 查找元素
        cur = self.__head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def add(self, item):
        '''头部添加元素'''
        node = DoubleNode(item)
        if self.is_empty():
            self.__head = node
        else:
            # 将node的next指向第一个节点            
            node.next = self.__head
            # 将原第一个节点的pre 指向node
            self.__head.pre = node
            # 将self.__head 指向node
            self.__head = node

    def append(self,item):
        '''尾部添加节点'''
        node = DoubleNode(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node
            node.pre = cur

    def insert(self,pos,item):
        '''在指定位置插入元素'''
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            node = DoubleNode(item)
            count = 0
            pre = self.__head
            while count < pos - 1:
                count += 1
                pre = pre.next
            #将node的pre指向pre
            node.pre = pre
            #将node的next指向插入位置的后一个节点
            node.next = pre.next
            #将pre的下一个节点的pre指向node
            pre.next.pre = node
            #将pre的next 指向node
            pre.next = node

    def remove(self,item):
        '''删除元素'''
        cur = self.__head
        while cur != None:
            if cur.item == item:
                #判断是否是头节点
                if cur == self.__head:
                    self.__head = cur.next
                    #不止一个节点，删除头结点之后，元素的pre为None
                    if cur.next:
                        cur.next.pre = None
                else:
                    cur.pre.next = cur.next
                    #要删除的节点不是最后一个节点
                    if cur.next:
                        cur.next.pre = cur.pre
                break
            else:
                cur = cur.next


if __name__ == '__main__':
    L3 = DoubleLinkList()
    L3.add(6)
    L3.add(7)
    L3.add(8)
    L3.append('haha')
    L3.append('xixi')
    L3.append('heihei')
    L3.insert(1,'python')
    # L3.remove('python')
    L3.remove('haha')
    L3.travel()
