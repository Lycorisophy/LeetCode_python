def divisorGame(N: int) -> bool:
    return N % 2 == 0


if __name__ == '__main__':
    print(divisorGame(2))
    print(divisorGame(3))
    print(divisorGame(1000))
