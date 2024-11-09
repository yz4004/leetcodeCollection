from typing import List
mod = 10 ** 9 + 7
"""
单点更新 + 复杂区间信息合并 （打家劫舍，不相邻最大子数列信息，子区间也是类似逻辑）
"""

class SegmentTree:  # 单点更新，维护复杂区间信息
    def __init__(self, nums):
        n = len(nums)
        self.nums = nums
        # self.t = [0] * (4 * n)  # 区间信息，本例保存区间和，可以替换为更复杂的信息
        # 1. 将所有需要维护的情况平铺列出
        # self.tm = [0] * (4 * n)  # 区间max子数组和
        # self.tl = [0] * (4 * n)  # 左端点 (l,r]
        # self.tr = [0] * (4 * n)  # 右端点 [l,r)
        # self.to = [0] * (4 * n)  # 开区间 (l,r)

        # 2. 将所有信息合并到t上，所有区间段维护的信息都在 t[p] 中 t[p][0 1 2 3] 对应上述tm tl tr to
        self.t = [[0,0,0,0] for _ in range(4 * n)]

        self.build(1, 0, n - 1)  # 初始化

    def build(self, p, l, r):
        # (p,l,r) parent 以及管辖区间
        if l == r:
            # self.tm[p] = self.nums[l]
            self.t[p][0] = self.nums[l]
            return
        mid = (l + r) // 2
        self.build(2 * p, l, mid)
        self.build(2 * p + 1, mid + 1, r)
        self.pull(p, l, r)

    def pull(self, p, l, r):  # up
        # 子信息汇总p <- 2*p, 2*p+1
        # self.t[p] = self.t[2 * p] + self.t[2 * p + 1] # 更新sum

        # 2. 将合并过程单独放进merge函数里，包装二元操作，因为merge在区间查询里也用得到
        self.t[p] = self.merge(self.t[2*p], self.t[2*p+1])

        # 1. 按照初始思路，将平铺信息合并，四种区间，tm不考虑边界的子序列最大值; tl (l,r] 区间子序列最大值; tr [l,r);  to (l,r)
        # # [l, mid] [mid+1, r]
        # self.tm[p] = max(self.tr[2*p] + self.tm[2*p+1], self.tm[2*p] + self.tl[2*p+1]) # [l,mid] (mid+1, r], [l,mid) [mid+1, r]
        # self.tl[p] = max(self.tl[2*p] + self.tl[2*p+1], self.to[2*p] + self.tm[2*p+1]) # (l,mid] (mid+1, r], (l,mid) [mid+1, r]
        # self.tr[p] = max(self.tr[2*p] + self.tr[2*p+1], self.tm[2*p] + self.to[2*p+1]) # [l,mid] [mid+1, r), [l,mid] (mid+1, r)
        # self.to[p] = max(self.tl[2*p] + self.to[2*p+1], self.to[2*p] + self.tr[2*p+1]) # (l,mid) [mid+1, r), (l,mid] (mid+1, r)

    def merge(self, left, right):
        # 更复杂的合并左右区间逻辑；用在pull/query里 self.t[p] = self.t[2 * p] + self.t[2 * p + 1]
        # [l, mid] [mid+1, r]
        tm1, tl1, tr1, to1 = left
        tm2, tl2, tr2, to2 = right

        tm = max(tr1 + tm2, tm1 + tl2)
        tl = max(tl1 + tl2, to1 + tm2)  # (l,mid] [mid+1, r]
        tr = max(tr1 + tr2, tm1 + to2)  # [l,mid] [mid+1, r)
        to = max(tl1 + to2, to1 + tr2)  # (l,mid] [mid+1, r)
        return [tm, tl, tr, to]

    def update(self, p, l, r, i, v):
        # if L <= l and r <= R: 区间更新条件
        #     self.apply(p, l, r, v)
        #     return
        if l == r:  # 单点更新条件
            # self.tm[p] = v  # 注意tm内是区间编号p
            self.t[p][0] = v
            return

        mid = (l + r) // 2
        # self.push(p, l, r) #无分发懒信息
        if i <= mid:
            self.update(2 * p, l, mid, i, v)
        if mid < i:
            self.update(2 * p + 1, mid + 1, r, i, v)
        self.pull(p, l, r)

    def query(self, p, l, r, L, R):
        if L <= l and r <= R:
            return self.t[p]
        mid = (l + r) // 2
        # self.push(p, l, r) #无分发懒信息

        left = [0]*4
        right = [0]*4
        if L <= mid:
            left = self.query(2 * p, l, mid, L, R)
        if mid < R:
            right = self.query(2 * p + 1, mid + 1, r, L, R)
        return self.merge(left, right) #区间查询合并左右信息，也需要合并操作



class Solution_3156:
    # LC3156:  https://leetcode.cn/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/description/?envType=daily-question&envId=2024-10-31
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        tree = SegmentTree(nums)
        ans = 0
        n = len(nums)
        for i, v in queries:
            tree.update(1, 0, n - 1, i, v)
            # ans = (ans + max(tree.tm[1], 0)) % mod  # 允许空数组
            ans = (ans + max(tree.t[1][0], 0)) % mod  # 允许空数组
        return ans