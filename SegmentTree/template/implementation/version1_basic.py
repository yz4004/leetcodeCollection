"""
单点更新
"""

class SegmentTree:

    def __init__(self, nums):
        n = len(nums)
        self.nums = nums
        self.a = [0]*(4*n)
        self.build(1,0, n-1)

    def build(self, i, l, r):
        if l == r:
            self.a[i] = self.nums[l]
            return
        mid = (l+r)//2
        self.build(2*i, l, mid)
        self.build(2*i+1, mid+1, r)
        self.a[i] = self.a[2*i] + self.a[2*i+1]

    def query(self, i, l, r, L, R):
        if L <= l and r <= R:
            return self.a[i]
        res = 0
        # [l,r] [L,R]
        mid = (l+r)//2
        if L <= mid:
            res += self.query(2*i, l, mid, L, R)
        if mid < R:
            res += self.query(2*i+1, mid+1, r, L, R)
        return res

    def add(self, i, l, r, j, v):
        if l == r:
            self.a[i] += v
            return
        mid = (l+r)//2
        if j <= mid:
            self.add(2*i, l, mid, j, v)
        elif mid < j:
            self.add(2*i+1, mid+1, r, j, v)
