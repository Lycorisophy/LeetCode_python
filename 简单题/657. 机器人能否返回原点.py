def judgeCircle(moves: str) -> bool:
    x, y = 0, 0
    for move in moves:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'R':
            x += 1
        else:
            x -= 1
    return True if x==0 and y==0 else False

if __name__ == '__main__':
    print(judgeCircle("UD"))
    print(judgeCircle("LL"))
    print(judgeCircle("LLLL"))
    print(judgeCircle("RLUD"))
    print(judgeCircle("UUDD"))
    print(judgeCircle(""))
