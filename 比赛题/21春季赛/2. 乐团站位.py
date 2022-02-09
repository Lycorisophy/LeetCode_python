def orchestraLayout(num: int, xPos: int, yPos: int) -> int:
    center = (num + 1) / 2 - 1
    if num % 2 == 0:
        circles = num // 2
    else:
        circles = num // 2 + 1
    gap = max(abs(xPos - center), abs(yPos - center))
    which_circle = circles-int(gap)-1
    if xPos == which_circle:
        index = 0
    else:
        if xPos == num-1-which_circle:
            index = 2
        else:
            if yPos == which_circle:
                index = 3
            else:
                index = 1
    n = 0
    for i in range(which_circle):
        n += 4 * (num-1-i*2)
    n += index * (num-1-which_circle*2)
    if index == 0:
        n += yPos - which_circle + 1
    elif index == 1:
        n += xPos - num+which_circle + 2
    elif index == 2:
        n += num-which_circle-yPos
    elif index == 3:
        n += which_circle - xPos + 1
    return n % 9


if __name__ == '__main__':
    print(orchestraLayout(1, 0, 0))
    print(orchestraLayout(4, 1, 1))
