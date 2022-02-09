def slowestKey(releaseTimes: [int], keysPressed: str) -> str:
    res = 0
    res_list = [0]
    max_time = releaseTimes[0]
    pre = max_time
    n = releaseTimes.__len__()
    for i in range(1, n):
        tmp = releaseTimes[i]
        time = releaseTimes[i] - pre
        pre = tmp
        if time > max_time:
            max_time = time
            res = i
            res_list = [i]
        elif time == max_time:
            res_list.append(i)
    if res_list.__len__() == 1:
        return keysPressed[res]
    ans = [keysPressed[i] for i in res_list]
    return max(ans)


if __name__ == '__main__':
    print(slowestKey(releaseTimes = [9,29,49,50], keysPressed = "cbcd"))
    print(slowestKey(releaseTimes = [12,23,36,46,62], keysPressed = "spuda"))

