import heapq


def nthSuperUglyNumber(n: int, primes: [int]) -> int:
    seen = {1}
    heap = [1]

    for i in range(n - 1):
        curr = heapq.heappop(heap)
        for prime in primes:
            if (nxt := curr * prime) not in seen:
                seen.add(nxt)
                heapq.heappush(heap, nxt)

    return heapq.heappop(heap)


if __name__ == '__main__':
    print(nthSuperUglyNumber(n = 12, primes = [2,7,13,19]))

