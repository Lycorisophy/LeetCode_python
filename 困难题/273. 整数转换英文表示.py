def numberToWords(num: int) -> str:
    singles = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
             "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["Thousand", "Million", "Billion"]
    if num == 0:
        return 'Zero'
    res = []

    def sub2Words(S: int, index: int) -> [str]:
        tmp = []
        if S == 0:
            return []
        elif S < 10:
            tmp += [singles[S]]
        elif S < 20:
            tmp += [teens[S - 10]]
        elif S < 100:
            tmp += [tens[S // 10]]+sub2Words(S % 10, 0)
        else:
            tmp += [singles[S // 100], 'Hundred']+sub2Words(S % 100, 0)
        if index == 0:
            return tmp
        return tmp + [thousands[index-1]]

    i = 0
    while num > 0:
        s = num % 1000
        res = sub2Words(s, i) + res
        i += 1
        num //= 1000
    return ' '.join(res)


if __name__ == '__main__':
    print(numberToWords(123))
    print(numberToWords(12345))
    print(numberToWords(1234567))
    print(numberToWords(1234567891))
    print(numberToWords(1234000891))
