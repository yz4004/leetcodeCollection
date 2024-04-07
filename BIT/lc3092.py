"""

树状数组动态维护当前的最大值 支持减小一个值重新后计算全局最大值

"""
from collections import Counter
from typing import List

class BIT:
    def __init__(self, n):
        self.a = [0]*(n+1) # a[i] = max( b[i-lb+1, i] ) i的管辖区间: [i-lb+1, i]
        self.b = [0]*(n+1) # b[i] 原数组的值


    def update(self, i, x): # 这个代码能过但是很慢，因为如果是增大操作没必要再跑一遍内部while
        n = len(self.a)
        prev = self.b[i]
        self.b[i] = x
        # 如果更新值比原数值大，则直接沿着路径max上去即可，同一般的模板
        if prev < x:
            while i < n:
                self.a[i] = max(self.a[i], x)
                i += i & -i
            return
        """
        更新的值比原数值小，自底向上可能有一些节点原先维护的最大值会被破坏
        假如更新了节点a[i] （比以前小了） 传导到其parent节点，如果它曾经的值也是parent的值，即它也是这段区间的最大值
        那现在减小了它, 需要重新计算parent的值，即遍历parent 个 log(lb(parent)) 子节点 
        所以update时间复杂度约 logN*logN
        """
        while i < n:
            # if self.a[i] > x:  break # 当遍历到某个节点超过了x 则不必继续更新
            # 遍历i的子节点 i-k  k~[1, lb)
            k, lb = 1, i & -i
            self.a[i] = self.b[i] # 先重置 a[i], a[i] 的管辖区间 [i-lb+1, i]
            while k < lb:
                self.a[i] = max(self.a[i - k], self.a[i])
                k += k & -k
            i += i & -i

    # def update(self, i, x): #第一版代码 冗余多
    #     n = len(self.a)
    #     pre = self.b[i]
    #     self.b[i] = x
    #     if x < self.a[i]: # 将i减小
    #         while i < n:
    #             if self.a[i] == pre:
    #                 self.a[i] = x
    #                 k = 1
    #                 lb = i & -i
    #                 new = 0
    #                 while k < lb:
    #                     new = max(self.a[i-k], new)
    #                     k += k & -k
    #                 new = max(self.b[i], new)
    #                 self.a[i] = new
    #             i += i & -i
    #     else:
    #         # 如频次增加 更新的值只可能更大 直接沿路径max上去就行了
    #         while i < n:
    #             self.a[i] = max(self.a[i], x)
    #             i += i & -i

    # def update(self, i, x): # 这个代码能过但是很慢，因为如果是增大操作没必要再跑一遍内部while
    #     n = len(self.a)
    #     self.b[i] = x
    #     # 考虑每次重新计算节点的最大值 因为可能有减小操作
    #     while i < n:
    #         k, lb = 1, i & -i
    #         self.a[i] = max(self.a[i], x)
    #         new = 0
    #         while k < lb:
    #             new = max(self.a[i - k], new)
    #             k += k & -k
    #         new = max(self.b[i], new)
    #         self.a[i] = new
    #         i += i & -i


    def search(self, i):
        res = 0
        while i > 0:
            res = max(res, self.a[i])
            i -= i & -i
        return res

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        n = len(nums)

        mx = max(nums)  # 10 ** 5
        t = BIT(mx)
        ans = [0]*n
        cnt = Counter()
        for i in range(n):
            cnt[nums[i]] += freq[i]
            t.update(nums[i], cnt[nums[i]] )
            ans[i] = t.search(mx)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.mostFrequentIDs([2,3,2,1], [3,2,-3,1]))
    # [5, 5, 3], freq = [2, -2, 1]
    #
    # print(s.mostFrequentIDs([5, 5, 3], [2, -2, 1]))