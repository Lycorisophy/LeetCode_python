def uniqueMorseRepresentations(words: [str]) -> int:
    res = []
    t = ''
    oa = ord('a')
    ms = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
          "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
          "..-","...-",".--","-..-","-.--","--.."]
    for word in words:
        for letter in word:
            t += ms[ord(letter)-oa]
        res.append(t)
        t = ''
    return len(set(res))


if __name__ == '__main__':
    print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))

