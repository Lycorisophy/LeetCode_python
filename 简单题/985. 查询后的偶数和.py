def sumEvenAfterQueries(A: [int], queries: [[int]]) -> [int]:
    even = []
    even_sum = 0
    for a in A:
        if a % 2 == 0:
            even_sum += a
            even.append(1)
        else:
            even.append(0)
    res = []
    for v, i in queries:
        if v % 2 == 0:
            if even[i] == 1:
                even_sum += v
                A[i] += v
            else:
                A[i] += v
        else:
            if even[i] == 1:
                even_sum -= A[i]
                A[i] += v
                even[i] = 0
            else:
                even[i] = 1
                A[i] += v
                even_sum += A[i]
        res.append(even_sum)
    return res


if __name__ == '__main__':
    print(sumEvenAfterQueries([5,4,0,2]
,[[1,1],[3,1],[3,3],[5,1]]))
