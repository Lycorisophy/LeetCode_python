def topKFrequent(nums: [int], k: int) -> [int]:
    cnt = {}
    for num in nums:
        if num not in cnt:
            cnt[num] = 1
        else:
            cnt[num] += 1
    cnt = [[k, v] for k, v in cnt.items()]
    cnt.sort(key=lambda x: x[1], reverse=True)
    return [c[0] for c in cnt][:k]


if __name__ == '__main__':
    print(topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
    print(topKFrequent(nums=[1], k=1))
