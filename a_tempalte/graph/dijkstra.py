import heapq
from math import inf
from typing import List

#############
# 输入
#############
n: int
edges: List[List[int]]

#############
# 建图 边+weight
#############
g = [[] for _ in range(n)]
for a, b, c in edges:
    g[a].append((b, c))
    g[b].append((a, c))

#############
# 不计入前驱的简单dijkstra
#############
q = [(0, 0)]
dist = [inf] * n
dist[0] = 0 #出发点
while q:
    w, x = heapq.heappop(q)
    if w > dist[x]: continue  # (O(mn) -> O(mlogm + n)) 提前剪枝 避免空转 x之前出堆过
    for y, c in g[x]:
        if dist[y] > w + c:
            dist[y] = w + c
            heapq.heappush(q, (dist[y], y))
# dist
# pred


#############
# 计入前驱的dijkstra
#############
q = [(0, 0)]
dist = [inf] * n
dist[0] = 0
pred = [[] for _ in range(n)]  # 前驱
while q:
    w, x = heapq.heappop(q)
    if w > dist[x]: continue  # (O(mn) -> O(mlogm + n)) 提前剪枝 避免空转 x之前出堆过
    for y, c in g[x]:
        if dist[y] > w + c:
            dist[y] = w + c
            heapq.heappush(q, (dist[y], y))
            pred[y] = [x]
        elif dist[y] == w + c:
            pred[y].append(x)
# dist
# pred







