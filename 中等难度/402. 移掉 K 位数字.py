def removeKdigits(num: str, k: int) -> str:
    stack = []
    remain = len(num) - k
    for digit in num:
        while k and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    return ''.join(stack[:remain]).lstrip('0') or '0'



if __name__ == '__main__':
    print(removeKdigits(num="112", k=1))
    print(removeKdigits(num="10", k=2))
    print(removeKdigits(num="100200", k=1))
    print(removeKdigits(num="1432219", k=3))
