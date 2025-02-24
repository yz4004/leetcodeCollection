"""
LC3356
https://leetcode.cn/problems/zero-array-transformation-ii/


差分问题，但是希望使用尽量少的区间，而且只允许前k个
- 二分+差分
- 双指针+差分，视角在nums上，为了删除当前nums[i] 上面前k个区间需要取到哪里？
- lazy线段树直接维护区间值 - 区间减法 + 区间最大值
"""
from typing import List
import math


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        # 线段树区间更新 - lazy线段树
        # - 通过减法使得区间归0. - min(nums[i], v)
        # - 其实只需要维护最大值，然后再应用区间减法减去最大值
        # - lazy 线段树只需要修改 apply/pull 的主要逻辑
        n = len(nums)
        tree = SegmentTree_max_interval_subtraction(nums)
        if tree.query(1, 0, n - 1, 0, n - 1) <= 0:
            return 0

        for i, (l, r, t) in enumerate(queries):
            tree.update(1, 0, n - 1, l, r, t)
            if tree.query(1, 0, n - 1, 0, n - 1) <= 0:
                return i + 1
        return -1

        ############ 二分 + 差分
        n = len(nums)

        def check(k):
            d = [0] * (n + 1)
            for l, r, t in queries[:k]:
                # [l,r]
                d[l] += t
                d[r + 1] -= t

            for i in range(1, n + 1):
                d[i] += d[i - 1]

            for x, y in zip(nums, d):
                if x > y:
                    return False
            return True

        queries.append([0, 0, 0])  #
        l, r = 0, len(queries)
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l if l < len(queries) else -1


class SegmentTree_max_interval_subtraction:  # 只修改两处位置
    def __init__(self, nums):
        n = len(nums)
        self.nums = nums
        self.t = [0] * (4 * n)  # 区间信息，本例保存区间max，可以替换为更复杂的信息
        self.tag = [0] * (4 * n)  # 懒信息标记
        self.build(1, 0, n - 1)  # 初始化

    # def __init__(self, n):
    #     self.t = [inf] * (4 * n)  # info
    #     self.tag = [0] * (4 * n)  # 懒信息

    def build(self, p, l, r):
        # (p,l,r) parent 以及管辖区间
        if l == r:
            self.t[p] = self.nums[l]
            return
        mid = (l + r) // 2
        self.build(2 * p, l, mid)
        self.build(2 * p + 1, mid + 1, r)
        self.pull(p)

    def pull(self, p):  # up
        # 子信息汇总p <- 2*p, 2*p+1
        ##########################################
        ##########################################
        self.t[p] = max(self.t[2 * p], self.t[2 * p + 1])  # 更新max
        ##########################################
        ##########################################

    def push(self, p, l, r):  # down 通知树节点p 下发懒信息
        if self.tag[p]:
            v = self.tag[p]
            self.apply(2 * p, l, (l + r) // 2, v)  # 懒信息推给左
            self.apply(2 * p + 1, (l + r) // 2 + 1, r, v)  # 懒信息推给右
            self.tag[p] = 0  # 清空暂存的懒信息，已经下发
            # 当有update操作自上而下准备更新区间p之前，先下发之前p暂存的懒信息 （本例懒信息只是要加的数值）

    def apply(self, p, l, r, v):  # 下发lazy信息，先更新节点信息，然后暂存懒信息，（不继续下发）
        ##########################################
        ##########################################
        self.t[p] -= v
        self.tag[p] += v  # 不是 =v 而是 += v 不能重置0 @@@
        ##########################################
        ##########################################

    def update(self, p, l, r, L, R, v):
        # (p,l,r) [L, R] += v
        if L <= l and r <= R:  # 当(p,l,r) 为 [L, R] 子区间即停止递归，利用懒信息下发函数更新（不要递归到空，否则失去懒更新意义)
            self.apply(p, l, r, v)
            return
        mid = (l + r) // 2
        self.push(p, l, r)  # 递归左右之前，先分发懒信息
        if L <= mid:
            self.update(2 * p, l, mid, L, R, v)
        if mid < R:
            self.update(2 * p + 1, mid + 1, r, L, R, v)
        self.pull(p)

    def query(self, p, l, r, L, R):
        if L <= l and r <= R:
            return self.t[p]
        res = -math.inf
        mid = (l + r) // 2
        self.push(p, l, r)  # 递归左右之前，先分发懒信息，虽然不会更新，但查询部分左右区间也依赖本层懒信息
        if L <= mid:
            res = max(res, self.query(2 * p, l, mid, L, R))
        if mid < R:
            res = max(res, self.query(2 * p + 1, mid + 1, r, L, R))
        return res