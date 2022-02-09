def distanceBetweenBusStops(distance: [int], start: int, destination: int) -> int:
    if start == destination:
        return 0
    if start > destination:
        start, destination = destination, start
    res1, res2 = 0, 0
    ss = False
    for i, d in enumerate(distance):
        if i == start:
            ss = True
        elif i == destination:
            ss = False
        if ss:
            res1 += d
        else:
            res2 += d
    return res1 if res1 < res2 else res2


if __name__ == '__main__':
    print(distanceBetweenBusStops(distance=[1, 2, 3, 4], start=0, destination=1))
    print(distanceBetweenBusStops(distance=[1, 2, 3, 4], start=2, destination=1))
    print(distanceBetweenBusStops([1, 2, 3, 4], start=0, destination=3))
