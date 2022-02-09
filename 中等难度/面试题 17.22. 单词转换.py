def findLadders(beginWord: str, endWord: str, wordList: [str]) -> [str]:
    def dfs(begin: str, end: str, N: int) -> bool:
        if begin == end:
            return True

        def isLadder(a: str, b: str) -> bool:
            if len(a) != len(b):
                return False
            n = len(a)
            cnt = 0
            for i in range(n):
                if a[i] != b[i]:
                    cnt += 1
                    if cnt == 2:
                        return False
            return cnt == 1

        for i in range(N):
            word = wordList[i]
            if visited[i] or not isLadder(begin, word):
                continue
            visited[i] = True
            path.append(word)
            if dfs(word, end, N):
                return True
            path.pop(-1)
        return False

    n = len(wordList)
    visited = [False for _ in range(n)]
    path = [beginWord]
    if dfs(beginWord, endWord, n):
        return path
    return []


if __name__ == '__main__':
    print(findLadders(beginWord="hit",
                      endWord="cog",
                      wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
    print(findLadders(beginWord="hit",
                      endWord="cog",
                      wordList=["hot", "dot", "dog", "lot", "log"]))
