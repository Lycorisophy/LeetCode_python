def peakIndexInMountainArray(arr: [int]) -> int:
    def binarySearch(arr, l, r):
        mid = int(l + (r - l) / 2)
        lv, mv, rv = arr[mid-1], arr[mid], arr[mid+1]
        if mv > lv and mv > rv:
            return mid
        elif lv < mv < rv:
            return binarySearch(arr, mid + 1, r)
        return binarySearch(arr, l, mid - 1)
    return binarySearch(arr, 0, len(arr)-1)


if __name__ == '__main__':
    print(peakIndexInMountainArray([18,29,38,59,98,100,99,98,90]))
