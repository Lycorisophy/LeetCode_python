def diStringMatch(S: str) -> [int]:
    S = [1 if s == 'I' else 0 for s in S]
    n = S.__len__()
    if S[0] == 1:
        res = [i for i in range(n+1)]
    else:
        res = [i for i in range(n, -1, -1)]

    def bubble_sort(array: [], relations: [], len_arr: int) -> []:
        for i in range(1, len_arr):
            tmp = array.copy()
            for j in range(1, len_arr - i):
                if relations[j] == 1:
                    if array[j] > array[j + 1]:
                        array[j], array[j + 1] = array[j + 1], array[j]
                else:
                    if array[j] < array[j + 1]:
                        array[j], array[j + 1] = array[j + 1], array[j]
            if tmp == array:
                break
        return array

    return bubble_sort(res, S, n+1)


if __name__ == '__main__':
    print(diStringMatch("IDID"))
    print(diStringMatch("III"))
    print(diStringMatch("DDI"))
