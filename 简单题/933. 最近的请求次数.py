class RecentCounter:

    def __init__(self):
        self.count = 0
        self.requests = []
        self.base = 0

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.count += 1
        for i in range(self.base, self.requests.__len__()-1):
            if t - self.requests[i] > 3000:
                self.count -= 1
                self.base += 1
        return self.count
    

if __name__ == '__main__':
    rc = RecentCounter()
    I = [1, 100, 3001, 3002, 3100, 3101, 8000]
    for i in I:
        print(rc.ping(i))
