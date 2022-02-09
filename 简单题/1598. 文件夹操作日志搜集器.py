def minOperations(logs: [str]) -> int:
    res = 0
    for log in logs:
        if log == './':
            continue
        elif log == '../':
            if res > 0:
                res -= 1
        else:
            res += 1
    return res


if __name__ == '__main__':
    print(minOperations(["d1/", "d2/", "../", "d21/", "./"]))
    print(minOperations(["d1/", "d2/", "./", "d3/", "../", "d31/"]))
    print(minOperations(["d1/", "../", "../", "../"]))
