def convert(s: str, numRows: int) -> str:
    if numRows < 2:
        return s
    res = ['' for _ in range(numRows)]
    s = list(s)
    ssz = True
    row = 0
    for char in s:
        res[row] += char
        if ssz:
            row += 1
            if row == numRows - 1:
                ssz = False
        else:
            row -= 1
            if row == 0:
                ssz = True
    return ''.join(res)

if __name__ == '__main__':
    print(convert(s = "PAYPALISHIRING", numRows = 3))
    print(convert(s = "PAYPALISHIRING", numRows = 4))
    print(convert(s = "A", numRows = 1))
