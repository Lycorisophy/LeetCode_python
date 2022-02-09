def checkRecord(s: str) -> bool:
    cntA, cntL = 0, 0
    for S in s:
        if S == 'A':
            cntA += 1
            if cntA == 2:
                return False
            cntL = 0
        elif S == 'L':
            cntL += 1
            if cntL == 3:
                return False
        else:
            cntL = 0
    return True


if __name__ == '__main__':
    print(checkRecord("PPALL"))