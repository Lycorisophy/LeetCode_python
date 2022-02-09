import collections


class DisjointSet:
    def __init__(self, n):
        self.S = list(range(n + 1))

    def find(self, X):
        return self.S[X] if self.S[X] == X else self.find(self.S[X])

    def union(self, X, Y):
        self.S[self.find(X)] = self.find(Y)


def accountsMerge(accounts: [[str]]) -> [[str]]:
    emailToIndex = dict()
    emailToName = dict()

    for account in accounts:
        name = account[0]
        for email in account[1:]:
            if email not in emailToIndex:
                emailToIndex[email] = len(emailToIndex)
                emailToName[email] = name

    uf = DisjointSet(len(emailToIndex))
    for account in accounts:
        firstIndex = emailToIndex[account[1]]
        for email in account[2:]:
            uf.union(firstIndex, emailToIndex[email])

    indexToEmails = collections.defaultdict(list)
    for email, index in emailToIndex.items():
        index = uf.find(index)
        indexToEmails[index].append(email)

    ans = list()
    for emails in indexToEmails.values():
        ans.append([emailToName[emails[0]]] + sorted(emails))
    return ans


if __name__ == '__main__':
    print(accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                         ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]))
    print(accountsMerge(
        [["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"], ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
         ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"], ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
         ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]))
