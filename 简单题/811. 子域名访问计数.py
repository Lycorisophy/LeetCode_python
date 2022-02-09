def subdomainVisits(cpdomains: [str]) -> [str]:
    hashmap = {}
    for cpdomain in cpdomains:
        s = ''
        for cp in cpdomain:
            if cp == ' ':
                count = int(s)
                s = ''
                break
            s += cp
        for cp in cpdomain[::-1]:
            if cp == ' ':
                if s in hashmap:
                    hashmap[s] += count
                else:
                    hashmap[s] = count
                break
            if cp == '.':
                if s in hashmap:
                    hashmap[s] += count
                else:
                    hashmap[s] = count
            s = cp + s
    return [str(v)+' '+k for k, v in hashmap.items()]


if __name__ == '__main__':
    print(subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))

