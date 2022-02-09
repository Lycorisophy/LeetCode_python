def romanToInt(s: str) -> int:
    romanBetas = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    nums, preNum = 0, 0
    for beta in s[::-1]:
        num = romanBetas[beta]
        if num >= preNum:
            nums += num
        else:
            nums -= num
        preNum = num
    return nums



if __name__ == '__main__':
    print(romanToInt('III'))
    print(romanToInt('IV'))
    print(romanToInt('IX'))
    print(romanToInt("LVIII"))
    print(romanToInt("MCMXCIV"))