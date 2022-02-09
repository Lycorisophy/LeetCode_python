def kWeakestRows(mat: [[int]], k: int) -> [int]:
    mat = [[m, i] for i, m in enumerate(mat)]
    mat.sort(key=lambda x: sum(x[0]))
    return [m[1] for m in mat[:k]]


if __name__ == '__main__':
    print(kWeakestRows(mat=
                       [[1, 1, 0, 0, 0],
                        [1, 1, 1, 1, 0],
                        [1, 0, 0, 0, 0],
                        [1, 1, 0, 0, 0],
                        [1, 1, 1, 1, 1]],
                       k=3
                       ))
    print(kWeakestRows(mat=
                       [[1, 0, 0, 0],
                        [1, 1, 1, 1],
                        [1, 0, 0, 0],
                        [1, 0, 0, 0]],
                       k=2))
