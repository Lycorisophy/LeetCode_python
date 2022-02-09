def nextGreatestLetter(letters: [str], target: str) -> str:
    res = [letter for letter in letters if letter > target]
    return min(res) if res else min(letters)


if __name__ == '__main__':
    print(nextGreatestLetter(letters = ["c", "f", "j"],
target = "k"))
    print(nextGreatestLetter(letters = ["c", "f", "j"],
target = "d"))
    print(nextGreatestLetter(letters = ["c", "f", "j"],
target = "g"))
