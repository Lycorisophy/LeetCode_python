from collections import Counter


def uncommonFromSentences(A: str, B: str) -> [str]:
    return [k for k, v in Counter((A + ' ' + B).split(' ')).items() if v == 1]


if __name__ == '__main__':
    print(uncommonFromSentences(A="this apple is sweet", B="this apple is sour"))
    print(uncommonFromSentences(A="apple apple", B="banana"))
