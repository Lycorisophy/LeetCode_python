def computeArea(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    s = (ax2-ax1)*(ay2-ay1)+(bx2-bx1)*(by2-by1)
    if bx1 >= ax2 or bx2 <= ax1 or by1 >= ay2 or by2 <= ay1:
        return s
    xs = [ax1, ax2, bx1, bx2]
    ys = [ay1, ay2, by1, by2]
    xs.sort()
    ys.sort()
    return s - (xs[2] - xs[1]) * (ys[2] - ys[1])


if __name__ == '__main__':
    print(computeArea(ax1=-3, ay1=0, ax2=3, ay2=4, bx1=0, by1=-1, bx2=9, by2=2))
    print(computeArea(ax1=-2, ay1=-2, ax2=2, ay2=2, bx1=-2, by1=-2, bx2=2, by2=2))
