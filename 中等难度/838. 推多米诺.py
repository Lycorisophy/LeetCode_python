def pushDominoes(dominoes: str) -> str:
    dominoes = list(dominoes)
    n = len(dominoes)
    for i, dominoe in enumerate(dominoes):
        if dominoe == 'L':
            if i != 0:
                cnt = 1
                j = i - 1
                while j >= 0 and dominoes[j] == '.':
                    dominoes[j] = str(cnt)
                    j -= 1
                    cnt += 1
    i = 0
    while i < n:
        if dominoes[i] == 'R':
            cnt = 1
            i += 1
            while i < n and not dominoes[i].isalpha():
                if dominoes[i] == '.':
                    dominoes[i] = 'R'
                else:
                    num = int(dominoes[i])
                    if num < cnt:
                        dominoes[i] = 'L'
                    elif num > cnt:
                        dominoes[i] = 'R'
                    else:
                        dominoes[i] = '.'
                i += 1
                cnt += 1
        else:
            i += 1
    for i, dominoe in enumerate(dominoes):
        if dominoe.isnumeric():
            dominoes[i] = 'L'
    return ''.join(dominoes)


if __name__ == '__main__':
    print(pushDominoes("RR.L"))
    print(pushDominoes(".L.R...LR..L.."))


