class DisjointSet:
    def __init__(self, n):
        self.S = list(range(n + 1))

    def find(self, X):
        return self.S[X] if self.S[X] == X else self.find(self.S[X])

    def union(self, X, Y):
        self.S[self.find(X)] = self.find(Y)
