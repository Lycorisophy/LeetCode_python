def distributeCandies(candyType: [int]) -> int:
    return min(len(candyType)//2, len(set(candyType)))


if __name__ == '__main__':
    print(distributeCandies([1,1,2,2,3,3,8,7,0,3]))