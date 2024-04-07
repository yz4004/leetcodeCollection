"""
binary index tree 树状数组

英文名比较显然，index/二进制关系的数结构
"""
import bisect


class BIT:
    def __init__(self, n):
        self.a = [0]*(n+1) #(1,n)

    """ 单点更新 [i] + x """
    def update(self, i, x):
        n = len(self.a)
        while i < n:
            self.a[i] += x  # 任何具有差分/可加性质的操作
            i += i & -i     # i = i + lowbit(i)

    """ 前缀查询 [:i] """
    def getSum(self, i):
        # i 的全部管辖区间 [i-lowbit(i)+1, i] 然后接力
        ans = 0
        while i > 0:
            ans += self.a[i]
            i -= i & -i
        return ans

    """ 区间查询 [l,r] """
    def getSum(self,i,j):
        return self.getSum(j) - self.getSum(i-1)



    # def 