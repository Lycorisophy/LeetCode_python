def findRepeatedDnaSequences(s: str) -> [str]:
    n = s.__len__()
    if n < 11:
        return []
    dna_dict = {}
    for i in range(n-9):
        sequence = s[i:i+10]
        if sequence not in dna_dict:
            dna_dict[sequence] = False
        else:
            dna_dict[sequence] = True
    return [k for k, v in dna_dict.items() if v]


if __name__ == '__main__':
    print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
    print(findRepeatedDnaSequences("AAAAAAAAAAAAA"))

