import itertools
def nextGreaterElement(n: int) -> int:
    s = str(n)
    l = len(s)
    for i in range(l):
        sub = s[-i-1:]
        print(sub)


if __name__ == '__main__':
    print(nextGreaterElement(12))
    # print(nextGreaterElement(21))
    # print(nextGreaterElement(123))
    # print(nextGreaterElement(456))
    # print(nextGreaterElement(0))