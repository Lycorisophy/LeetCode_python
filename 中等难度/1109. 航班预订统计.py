def corpFlightBookings(bookings: [[int]], n: int) -> [int]:
    tmp = [[0 for _ in range(2)] for _ in range(n+1)]
    for booking in bookings:
        s, e, c = booking
        tmp[s][0] += c
        tmp[e][1] += c
    res = [0] * (n + 1)
    for i in range(1, n+1):
        res[i] = res[i-1] + tmp[i][0] - tmp[i-1][1]
    return res[1:]


if __name__ == '__main__':
    print(corpFlightBookings(bookings=[[1, 2, 10], [2, 3, 20], [2, 5, 25]], n=5))
    print(corpFlightBookings(bookings=[[1, 2, 10], [2, 2, 15]], n=2))
