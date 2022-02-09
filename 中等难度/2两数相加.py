class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class List:
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        return self.length == 0

    def append(self, dataOrNode):
        if isinstance(dataOrNode, ListNode):
            item = dataOrNode
        else:
            item = ListNode(dataOrNode)

        if not self.head:
            self.head = item
            self.length += 1

        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = item
            self.length += 1

    # 删除一个节点之后记得要把链表长度减一
    def delete(self, index):
        if self.isEmpty():
            print("this chain table is empty.")
            return

        if index < 0 or index >= self.length:
            print('error: out of index')
            return
        # 要注意删除第一个节点的情况
        # 如果有空的头节点就不用这样
        # 但是我不喜欢弄头节点
        if index == 0:
            self.head = self.head._next
            self.length -= 1
            return

        # prev为保存前导节点
        # node为保存当前节点
        # 当j与index相等时就
        # 相当于找到要删除的节点
        j = 0
        node = self.head
        prev = self.head
        while node.next and j < index:
            prev = node
            node = node.next
            j += 1

        if j == index:
            prev.next = node.next
            self.length -= 1

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        count = 0
        ret = ListNode()
        tmp = ret
        while l1 or l2 or count:
            num = 0
            if l1:
                num += l1.val
                l1 = l1.next
            if l2:
                num += l2.val
                l2 = l2.next
            if count:
                num += count
                count -= 1
            count, num = divmod(num, 10)
            tmp.next = ListNode(num)
            tmp = tmp.next
        return ret.next

if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    L1 = List()
    L2 = List()
    for i1 in l1:
        L1.append(i1)
    for i2 in l2:
        L2.append(i2)
    solution = Solution()
    L3 = solution.addTwoNumbers(L1.head, L2.head)
    print(L3)


