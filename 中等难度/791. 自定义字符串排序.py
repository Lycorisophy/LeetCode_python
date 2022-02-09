def customSortString(order: str, s: str) -> str:
    dic = {o: i for i, o in enumerate(order)}
    s = list(s)

    def quick_sort(left: int, right: int) -> None:
        if left < right:
            i = left
            j = right
            pivot = s[left]
            if pivot in dic:
                while i != j:
                    while j > i and s[j] in dic and dic[s[j]] > dic[pivot]:
                        j -= 1
                    if j > i:
                        s[i] = s[j]
                        i += 1
                    while i < j and s[i] in dic and dic[s[i]] < dic[pivot]:
                        i += 1
                    if i < j:
                        s[j] = s[i]
                        j -= 1
            s[i] = pivot
            quick_sort(left, i - 1)
            quick_sort(i + 1, right)

    quick_sort(0, len(s)-1)
    return ''.join(s)


if __name__ == '__main__':
    print(customSortString("bca", "abcdaabbccddabc"))
    print(customSortString("ca", "abcd"))
    print(customSortString("cbad", "abcd"))
