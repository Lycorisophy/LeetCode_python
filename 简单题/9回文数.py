def isPalindrome(x: int) -> bool:
    s = str(x)
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True


if __name__ == '__main__':
    print(isPalindrome(121))
    print(isPalindrome(-121))
    print(isPalindrome(10))
    print(isPalindrome(0))
    print(isPalindrome(9489381742))