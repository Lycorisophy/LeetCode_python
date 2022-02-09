class KthLargest:

    def __init__(self, k: int, nums: [int]):
        self.values = sorted(nums, reverse=True)
        self.length = len(nums)
        self.key = k - 1

    def _binarySearch(self, arr, l, r, x):
        if r >= l:
            mid = int(l + (r - l) / 2)
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                return self._binarySearch(arr, l, mid - 1, x)
            else:
                return self._binarySearch(arr, mid + 1, r, x)
        else:
            return l

    def add(self, val: int) -> int:
        self.values.insert(self._binarySearch(self.values, 0, self.length-1, val), val)
        self.length += 1
        return self.values[self.key]


if __name__ == '__main__':
    obj = KthLargest(3, [4, 5, 8, 2])
    print(obj.add(3))
    print(obj.add(5))
    print(obj.add(10))
    print(obj.add(9))
    print(obj.add(4))

