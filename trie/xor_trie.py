from collections import  defaultdict
from typing import List


class Solution:
    def maxXor(self, n: int, edges: List[List[int]], values: List[int]) -> int:
        g = defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        A = [0]*n
        def dfs(u,f):
            A[u] = sum(dfs(v,u) for v in g[u] if v!=f)+values[u]
            return A[u]
        dfs(0,-1)
        L = A[0].bit_length()
        T = [set() for _ in range(L)]
        self.res = 0
        def dfs(u,f):
            x, y = A[u], 0
            for j in range(L-1,-1,-1):
                y *= 2
                y += (y+1)^(x>>j) in T[j]
            self.res = max(self.res,y)
            for v in g[u]:
                if v!=f:
                    dfs(v,u)
            for j in range(L):
                T[j].add(x>>j)
        dfs(0,-1)
        return self.res