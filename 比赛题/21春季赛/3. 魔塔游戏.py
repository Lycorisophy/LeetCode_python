class MinHeap(object):

    def __init__(self):
        self._data = []
        self._count = len(self._data)

    def size(self):
        return self._count

    def isEmpty(self):
        return self._count == 0

    def add(self, item):
        # 插入元素入堆
        if self._count >= len(self._data):
            self._data.append(item)
        else:
            self._data[self._count] = item

        self._count += 1
        self._shiftup(self._count - 1)

    def pop(self):
        # 出堆
        if self._count > 0:
            ret = self._data[0]
            self._data[0] = self._data[self._count - 1]
            self._count -= 1
            self._shiftDown(0)
            return ret

    def _shiftup(self, index):
        # 上移self._data[index]，以使它不大于父节点
        parent = (index - 1) >> 1
        while index > 0 and self._data[parent][0] > self._data[index][0]:
            # swap
            self._data[parent], self._data[index] = self._data[index], self._data[parent]
            index = parent
            parent = (index - 1) >> 1

    def _shiftDown(self, index):
        # 上移self._data[index]，以使它不小于子节点
        j = (index << 1) + 1
        while j < self._count:
            # 有子节点
            if j + 1 < self._count and self._data[j + 1][0] < self._data[j][0]:
                # 有右子节点，并且右子节点较大
                j += 1
            if self._data[index][0] < self._data[j][0]:
                # 堆的索引位置已经大于两个子节点，不需要交换了
                break
            self._data[index], self._data[j] = self._data[j], self._data[index]
            index = j
            j = (index << 1) + 1


def magicTower(nums: [int]) -> int:
    if sum(nums) < 0:
        return -1
    res = 0
    hp = 1
    n = nums.__len__()
    i = 0
    monsters = MinHeap()
    while i < n - 1:
        tmp = nums[i]
        if tmp >= 0:
            hp += tmp
            i += 1
        else:
            hp += tmp
            monsters.add([tmp, i])
            if hp > 0:
                i += 1
            else:
                if monsters.isEmpty():
                    return -1
                val, index = monsters.pop()
                nums.pop(index)
                nums.append(val)
                res += 1
                hp -= val
    return res


if __name__ == '__main__':
    print(magicTower(nums=[-100]))
    print(magicTower([-200, -300, 400, 0]))
