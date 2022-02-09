import re
from collections import Counter


def mostCommonWord(paragraph: str, banned: [str]) -> str:
    paragraph = re.sub('[^\w\s]', ' ', paragraph).lower()
    words = paragraph.split(sep=' ')
    a = lambda x: re.sub('[^A-Za-z]', '', x)
    words = [a(word) for word in words]
    ok_words = [word for word in words if word not in banned and word]
    words_counter = Counter(ok_words)
    return words_counter.most_common(1)[0][0]


if __name__ == '__main__':
    print(mostCommonWord("Bob. hIt, baLl", ["bob", "hit"]))
