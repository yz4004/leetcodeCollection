import bisect
from typing import List

class BIT:
    def __init__(self, n):
        self.a = [-1]*(n+1)
        self.b = [-1]*(n+1)
    def update(self, i, x):
        n = len(self.a)
        self.b[i] = max(self.b[i], x)
        while i < n:
            self.a[i] = max(self.a[i], x)
            i += i & -i

    # def search(self, i):
    #     res = 0
    #     while i > 0:
    #         self.a[i] = max(self.a[i], res)
    #         i -= i & -i
    #     return res

    def search(self, i): # [i: ] 的最大值
        print(i)
        print(self.b)
        res = self.b[i]
        n = len(self.a)-1
        k = n
        # print(n,)
        while k > i:
            # [k-lb+1, k]
            if k - (k & -k) + 1 >= i:
                print("k", k)
                res = max(self.a[k], res)
                k -= k & -k
            else:
                res = max(self.b[k], res)
                k -= 1
        return res

class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        a = sorted((n1, n2) for n1, n2 in zip(nums1, nums2))
        for j, q in enumerate(queries):
            q.append(j)
        queries.sort(key=lambda q:-q[0])

        index = sorted(list(set(nums2)))

        n = len(nums1)
        i = n-1
        s1 = s2 = 0
        t = BIT(len(index))
        ans = [0]*len(queries)
        for (x, y, j) in queries:
            #
            while i >= 0 and a[i][0] >= x:
                n1, n2 = a[i]
                print(a[i], n1, n2)
                idx = bisect.bisect_left(index, n2) + 1
                t.update(idx, n2 + n1)
                s1 += n1
                s2 += n2
                i -= 1
            print("query", x, y, j, i)
            print(t.a)
            idx_y = bisect.bisect_left(index, y) + 1 # find first index in nums2 > y (from right to left)
            print("y", idx_y)

            if idx_y > len(index):
                ans[j] = -1
                continue
            r = t.search(idx_y)
            ans[j] = r
            print(j,x,y, "-", r)
            print()
        return ans

if __name__ == '__main__':
    s = Solution()
    # r = s.maximumSumQueries([4,3,1,2], [2,4,9,5], [[4,1],[2,5],[1,3]])
    # r = s.maximumSumQueries([3,2,5], [2,3,4], [[4,4],[3,2],[1,1]])

    r = s.maximumSumQueries([61,60,33,36,63,18], [49,28,49,20,32,84], [[22,8],[16,29],[13,54]])
    # r = s.maximumSumQueries([31], [17], [[1,79]])

    print(r)