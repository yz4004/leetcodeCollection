"""
重置操作，将区间统一重置成某个数，会销毁懒信息

"""
class segmentTree:
    def __init__(self, nums):
        n = len(nums)
        self.nums = nums
        self.t = [0]*(4*n)         # 维护信息 - 累加和
        self.add = [0]*(4*n)       # 加和 lazy tag
        self.change=[0]*(4*n)      # 重置的目标值
        self.reset = [False]*(4*n) # 重置 lazy tag 用于区分是不是change 0的情况

        self.build(1, 0, n-1)

    def build(self,o,l,r):
        if l == r:
            self.t[o] = self.nums[l]
            return
        mid = (l+r)//2
        self.build(2*o, l, mid)
        self.build(2*o+1, mid+1, r)
        self.t[o] = self.t[2*o] + self.t[2*o+1]

    def add(self, o, l, r, L, R, v):
        if L <= l and r <= R:
            pass
            return
        pass

    def change(self, o, l, r, L, R, v):
        if L <= l and r <= R:
            pass
            return
        pass

    def query(self, o, l, r, L, R):
        if L <= l and r <= R:
            pass
            return
        pass

    def lazy_change(self, o, l, r, v):
        pass

    def lazy_add(self, o, l, r, v):
        pass

    def down(self, o, l, r):
        pass

