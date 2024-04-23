"""
懒更新模板
"""
from SegmentTree.template.api_lazy import SegmentTree


class SegmentTree(SegmentTree):

    def __init__(self, nums):
        n = len(nums)
        self.nums = nums
        self.a = [0]*(4*n)
        # self.tag=[0]*(4*n) 懒更新标记
        self.build(1,0, n-1)

    def build(self, i, l, r):
        if l == r:
            self.a[i] = self.nums[l]
            return
        mid = (l+r)//2
        self.build(2*i, l, mid)
        self.build(2*i+1, mid+1, r)
        self.a[i] = self.a[2*i] + self.a[2*i+1] # up 操作

    def query(self, i, l, r, L, R):
        if L <= l and r <= R:
            return self.a[i]
        res = 0
        # [l,r] [L,R]
        mid = (l+r)//2
        # down 操作
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
        # down 操作
        if j <= mid:
            self.add(2*i, l, mid, j, v)
        elif mid < j:
            self.add(2*i+1, mid+1, r, j, v)



    """ 向下传递api: 父节点，及其管辖区间"""
    def down(self, i, l, r):
        if self.tag[i] != 0:
            mid = (l+r)//2
            self.lazy(2*i, self.tag[i], mid-l+1)
            self.lazy(2*i+1, self.tag[i], r-mid)
            self.tag[i] = 0

    """ 懒更新api: 节点i 单点修改值v, 区间单点数n. 给当前区间范围和整体增加，增加节点i的懒标记，（用于向下传递）"""
    def lazy(self, i, v, n):
        self.a[i] += v * n
        self.tag[i] += v

    """
    处于节点i，当add/query 需要向下精细操作，则积攒的懒更新需要向下传递。
    1. 懒标记分别传递给左右区间，并结合其区间长度，更新维护值
    2. 父节点传递后，删除懒标记
    """