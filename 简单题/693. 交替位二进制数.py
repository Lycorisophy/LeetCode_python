def hasAlternatingBits(n: int) -> bool:
    nums = [1, 2, 5, 10, 21, 42, 85, 170, 341, 682, 1365, 2730, 5461, 10922, 21845, 43690,
            87381, 174762, 349525, 699050, 1398101, 2796202, 5592405, 11184810, 22369621,
            44739242, 89478485, 178956970, 357913941, 715827882, 1431655765, 2863311530]
    for num in nums:
        if num < n:
            pass
        elif num == n:
            return True
        else:
            return False
        

if __name__ == '__main__':
    print(hasAlternatingBits(5))
