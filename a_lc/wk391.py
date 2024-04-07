import heapq
from typing import List


class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        # points.sorted()


        n = len(points)
        a = [None]*n
        for i, (px, py) in enumerate(points):
            mx = cnt = 0
            for (qx, qy) in points:
                if px == qx and py == qy: continue
                d = abs(px - qx) + abs(py - qy)
                if d > mx:
                    mx = d
                    cnt = 0
                if d == mx:
                    cnt += 1
            a[i] = [mx, cnt]

        count = defaultdict(int)
        for (mx, cnt) in a:
            count[mx] += cnt
        p = []
        for k in count:
            p.append(-k, count[k])

        heapq.heapify(p)
        res = inf
        for (mx, cnt) in a:
            top = p[0]
            if -p[0][0] == mx and p[0][1] == cnt:
                heapq.heappop(p)
                res = min(res, -p[0][0])
                heapq.heappush(p, top)
            else:
                res = min(res, -p[0][0])
        return res

        # s = defaultdict(list)
        # for (x,y) in points:
        #     s[x].append(y)
        #
        # c = {}
        # for x in s.keys():
        #     s[x].sorted()
        #     l = 0 #第二长
        #     if len(s[x]) > 2:
        #         l = max(s[-2]-s[0], s[-1]-s[1])
        #     c[x] = [s[x][0], s[x][-1], l]
        # # print(c)
        #
        # # global max count
        # cnt = defaultdict(int)
        # for x in c.keys():
        #     mi_x, mx_x = c[x][0], c[x][1]
        #     for y in c.keys():
        #         mi_y, mx_y = c[y][0], c[y][1]
        #         cnt[abs(y - x) + max(abs(mx_x - mi_y), abs(mx_y - mi_x))] += 1
        #
        # mx = max(cnt.keys())
        # mx_cnt = cnt[mx] // 2
        # for x in cnt:
        #     cnt[x] //= 2
        #
        #
        # for x in c.keys():
        #     mi_x, mx_x, l = c[x][0], c[x][1], c[x][2]
        #     t = c[x][2]
        #     for z in c.keys:
        #         mi_z, mx_z =
        #         t = max(s[z][0])