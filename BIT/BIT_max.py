'''
bit_sum 的基础函数
def update(self, i, x):
    a = self.a
    n = len(a)
    while i < n:
        a[i] += x
        i += i & -i

def getSum(self, i):
    a = self.a
    res = 0
    while i > 0:
        res += a[i]
        i -= i & -i

因为max不具差分性质，所以相比sum 不能用两个前缀查询的差 O(logN)
O(logN * logN)
思路是
考虑每个节点的管辖区间，如果被包含在查询范围中，max上去即可，然后缩减问题
如果超过了查询范围，则划分成两部分,
假如 j 是当前查询点 查询区间 [i,j] 而 j管辖 [j-lb(j)+1, j] 已经超过 [i,j]
则单独剥离j 和 [i,j-1]

具象化的想像区间结构
j管辖长度是lb，j-1 造成 lb位消失，剩下的全是1
10000
01111
参考oi wiki的证明 很巧妙
https://next.oi-wiki.org/ds/fenwick#%E5%8C%BA%E9%97%B4%E6%9F%A5%E8%AF%A2-1

questions
https://leetcode.cn/problems/longest-increasing-subsequence-ii/description/
对x 查询 [x-k, x] 范围内的最大值 （前面遍历过的元素）
'''
from math import inf
from typing import List


class BIT:
    def __init__(self, n):
        self.a = [0] * (n + 1) # 储存 max nums[:i] 前缀的值
        self.b = [0] * (n + 1) # 储存原数组 nums[i] 的值

    def update(self, i, x):
        a = self.a
        n = len(a)
        self.b[i] = x
        while i < n:
            a[i] = max(a[i], x)
            i += i & -i

    """ 计算 nums[i,j] 的max值 """
    def check(self, i, j):
        # [i,j]
        if i > j:
            return 0
        a, b = self.a, self.b
        lb = j & -j
        if i <= j - lb:
            #  i [j-lb+1, j]
            return max(self.check(i, j - lb), a[j])
        else:
            return max(self.check(i, j - 1), b[j])

class BIT:
    def __init__(self, n):
        self.a = [inf] * (n + 1) # 储存 min nums[:i] 前缀的值
        self.b = [0] * (n + 1)   # 储存原数组 nums[i] 的值

    def update(self, i, x):
        a = self.a
        n = len(a)
        self.b[i] = x
        while i < n:
            a[i] = min(a[i], x)
            i += i & -i

    """ 计算 nums[i,j] 的max值 """
    def check(self, i, j):
        # [i,j]
        if i > j:
            return 0
        a, b = self.a, self.b
        lb = j & -j
        if i <= j - lb:
            #  i [j-lb+1, j]
            return min(self.check(i, j - lb), a[j])
        else:
            return min(self.check(i, j - 1), b[j])
print("a".title())
"""
查询 大于x的数中，最小的数对和

"""
class Solution:

    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)

        mi = [inf]*n
        res = m = inf
        for i, x in enumerate(nums):
            for j in range(i):
                if nums[j] > x:
                    res = min(res, mi[j] + nums[j] + x)
            if m < x:
                mi[i] = m
            else:
                m = x
        return res if res < inf else -1