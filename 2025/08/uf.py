class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        return True

    # ----- requested features -----
    def __getitem__(self, x):
        """uf[x] returns the root of x"""
        return self.find(x)

    def values(self) -> list[int]:
        return [ self[i] for i in range(self.n) ]
