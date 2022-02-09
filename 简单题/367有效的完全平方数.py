def isPerfectSquare(num: int) -> bool:
    if num <= 100:
        return True if num in [0,1,4,9,16,25,36,49,64,81,100] else False
    else:
        l = (len(str(num))-1)*5
        isMul = True
        while True:
            t = l**2
            if t < num:
                if isMul:
                    l *= 2
                else:
                    return False
            elif t > num:
                isMul = False
                l -= 1
            else:
                return True

if __name__ == '__main__':
    print(isPerfectSquare(num=8723**2+1))