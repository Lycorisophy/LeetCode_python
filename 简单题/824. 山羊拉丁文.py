def toGoatLatin(S: str) -> str:
    words = S.split(' ')
    ans = ''
    yy = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i, word in enumerate(words):
        first_letter = word[0]
        if first_letter in yy:
            goat_latin_word = word
        else:
            goat_latin_word = word[1:] + first_letter
        goat_latin_word += 'ma'
        goat_latin_word += 'a' * (i + 1)
        ans += goat_latin_word + ' '
    return ans.rstrip(' ')


if __name__ == '__main__':
    print(toGoatLatin("I speak Goat Latin"))
    print(toGoatLatin("The quick brown fox jumped over the lazy dog"))
    print(toGoatLatin('Oh'))
