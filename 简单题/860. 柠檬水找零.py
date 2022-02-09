def lemonadeChange(bills: [int]) -> bool:
    five, ten = 0, 0
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five == 0:
                return False
            five -= 1
            ten += 1
        else:
            if ten == 0:
                if five < 3:
                    return False
                five -= 3
            else:
                if five == 0:
                    return False
                ten -= 1
                five -= 1
    return True


if __name__ == '__main__':
    print(lemonadeChange([5,5,5,10,20]))
    print(lemonadeChange([5, 5, 10]))
    print(lemonadeChange([10,10]))
    print(lemonadeChange([5,5,10,10,20]))
    print(lemonadeChange([]))

