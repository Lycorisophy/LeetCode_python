def smallestK(arr: [int], k: int) -> [int]:
    def qs(left, right):
        if left >= right:
            return
        pivot, i, j = arr[left], left, right
        while i < j:
            while i < j and arr[j] >= pivot:
                j -= 1
            arr[i] = arr[j]
            while i < j and arr[i] <= pivot:
                i += 1
            arr[j] = arr[i]
        arr[i] = pivot
        if i == k - 1:
            return
        elif i < k - 1:
            qs(i + 1, right)
        else:
            qs(left, i - 1)

    qs(0, len(arr) - 1)
    return arr[:k]


if __name__ == '__main__':
    print(smallestK(arr=[1, 3, 5, 7, 2, 4, 6, 8], k=4))
