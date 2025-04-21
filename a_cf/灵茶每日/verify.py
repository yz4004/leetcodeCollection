import random
from collections import deque
from typing import List, Tuple

Edge = Tuple[int, int, int]        # (u, v, w)

mx = lambda x, y: x if x > y else y
mn = lambda x, y: y if x > y else x
def solve(edges, queries):
    n = len(edges)+1
    g = [[] for _ in range(n)]
    for a,b,w in edges:
        g[a].append((b, w))
        g[b].append((a, w))

    pa = [-1] * n
    depth = [None] * n  # depth[i] i-子树最大次大枝条
    o_diameter = [0]

    def dfs(i, p) -> int:
        pa[i] = p

        m1 = m2 = 0
        for j, wj in g[i]:
            if j == p: continue
            r = dfs(j, i) + wj
            if r >= m1:
                m1, m2 = r, m1
            elif r > m2:
                m2 = r
        o_diameter[0] = mx(o_diameter[0], m1 + m2)
        depth[i] = (m1, m2)
        return m1

    dfs(0, -1)

    # 换根dp 处理来自父节点的
    convex1 = [None] * n
    convex2 = [None] * n
    sub = lambda x, y: (x[0] - y[0], x[1] - y[1])
    cross = lambda x, y: x[0] * y[1] - x[1] * y[0]

    def get_upper_convex(pts):
        pts.sort()
        st = []
        for cur in pts:
            # (st[-2], st[-1], cur)
            while len(st) >= 2 and cross(sub(st[-2], st[-1]), sub(st[-1], cur)) > 0:
                st.pop()
            st.append(cur)
        return st

    def dfs(i, p, wp, dp) -> (int, int):
        # dp 父节点传来的最大枝条 (不算临近边)
        # wp 最大枝条对应的临近边

        pts = []
        if i != 0:
            pts.append((wp, dp))

        # 1. 收集所有点集 (wi, di), di是子节点最大枝条，wi是到达子节点对应边
        # 2.1 整理最大次大di
        for j, wj in g[i]:
            if j == p: continue
            pts.append((wj, depth[j][0]))

        # print(i, wp, dp, pts)

        # 2.2 根据最大次大进行换根, 递归进j传入父节点i除了j分支的最大分支 （含上层传来）
        tmp = sorted((depth[i][0], depth[i][1], dp + wp))  # 最大次大子树枝条
        d1, d2 = tmp[-1], tmp[-2]
        for j, wj in g[i]:
            if j == p: continue
            branch = depth[j][0] + wj
            if branch == d1:
                dfs(j, i, wj, d2)
            else:
                dfs(j, i, wj, d1)

        # 3. 整理外层上凸包 去掉外层后的内层点集的上凸包 - 内层上凸包
        convex1[i] = get_upper_convex(pts)
        pts2 = [p for p in pts if p not in set(convex1[i])]
        convex2[i] = get_upper_convex(pts2)

    dfs(0, -1, 0, 0)
    # print(convex1)
    # print(convex2)

    # f(x,y) = y + k*x
    dot = lambda p, k: p[1] + p[0] * k

    def query(x, k):
        # x所有临边 * k
        hull1, hull2 = convex1[x], convex2[x]

        def check(hull):
            l, r = 0, len(hull) - 1
            while r - l > 2:
                m1 = l + (r - l) // 3
                m2 = r - (r - l) // 3
                if dot(hull[m1], k) < dot(hull[m2], k):
                    l = m1
                else:
                    r = m2
            best = l
            for i in range(l + 1, r + 1):
                if dot(hull[i], k) > dot(hull[best], k):
                    best = i
            return best  # hull[best]

        b1 = check(hull1)
        b2 = check(hull2)

        m1 = dot(hull1[b1], k)
        m2 = dot(hull2[b2], k) if hull2 else 0

        for b in (b1 - 1, b1 + 1):
            if 0 <= b < len(hull1) and dot(hull1[b], k) > m2:
                m2 = dot(hull1[b], k)

        return m1 + m2

    # print("__"*10)
    res = []
    for x,k  in queries:
        r = query(x, k)
        # print(x-1, k, r)
        # print(mx(o_diameter[0], r))
        res.append(mx(o_diameter[0], r))
    return res


# /* ---------- 1. 随机树生成 ---------- */
def random_tree(n: int,
                w_min: int = 1,
                w_max: int = 10**9,
                seed: int | None = None) -> List[Edge]:
    """
    生成 n 个节点的随机无向树（节点编号 0..n-1），
    边权均匀随机落在 [w_min, w_max]。
    """
    if seed is not None:
        random.seed(seed)

    parent = [random.randrange(i) for i in range(1, n)]     # Prufer-like
    edges: List[Edge] = []
    for child, par in enumerate(parent, start=1):
        w = random.randint(w_min, w_max)
        edges.append((child, par, w))
    return edges


# /* ---------- 2. 暴力求树直径 ---------- */
def diameter(n: int, edges: List[Edge]) -> int:
    """两次 BFS 求树直径，O(n)"""
    g = [[] for _ in range(n)]
    for u, v, w in edges:
        g[u].append((v, w))
        g[v].append((u, w))

    def farthest(src: int) -> Tuple[int, int]:
        dist = [-1] * n
        dist[src] = 0
        q = deque([src])
        while q:
            u = q.popleft()
            for v, w in g[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + w
                    q.append(v)
        far = max(range(n), key=dist.__getitem__)
        return far, dist[far]

    a, _ = farthest(0)
    b, d = farthest(a)
    return d


# /* ---------- 3. 单条询问的暴力答案 ---------- */
def query_diameter(n: int,
                   edges: List[Edge],
                   x: int,
                   k: int) -> int:
    """
    把所有与 x 相连的边权乘以 k，然后返回新树直径。
    """
    scaled = []
    for u, v, w in edges:
        if u == x or v == x:
            scaled.append((u, v, w * k))
        else:
            scaled.append((u, v, w))
    return diameter(n, scaled)


# /* ---------- demo: 随机测试你自己的算法 ---------- */
if __name__ == "__main__":
    N = 10_000             # 节点数
    Q = 1_0000              # 询问数

    edges = random_tree(N, 10**7, 10**9, seed=42)

    # 假设 your_answer(x,k) 是你写的高效算法
    # from your_module import your_answer   # ← 自己实现
    queries = [(random.randrange(N),random.randint(1, 10**4)) for _ in range(Q)]
    res = solve(edges, queries)
    #print(res)

    for q in range(Q):
        # x = random.randrange(N)
        # k = random.randint(1, 10**4)
        x, k = queries[q]
        brute = query_diameter(N, edges, x, k)
        # fast  = your_answer(edges, x, k)  # 需保持 O(log n) 级别
        fast = res[q]
        assert brute == fast, f"Mismatch @ x={x}, k={k}: {brute=}, {fast=}"
    print("All random tests passed ✓")