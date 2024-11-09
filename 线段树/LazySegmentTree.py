class LazySegmentTree:  # sum
    def __init__(self, nums):
        n = len(nums)
        self.nums = nums
        self.t = [0] * (4 * n)  # 区间信息，本例保存区间和，可以替换为更复杂的信息
        self.tag = [0] * (4 * n)  # 懒信息标记
        self.build(1, 0, n - 1)  # 初始化

    def __init__(self, n):
        self.t = [0] * (4 * n)  # info
        self.tag = [0] * (4 * n)  # 懒信息

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
        self.t[p] = self.t[2 * p] + self.t[2 * p + 1] # 更新sum


    def push(self, p, l, r):  # down 通知树节点p 下发懒信息
        if self.tag[p]:
            v = self.tag[p]
            self.apply(2 * p, l, (l + r) // 2, v)         # 懒信息推给左
            self.apply(2 * p + 1, (l + r) // 2 + 1, r, v) # 懒信息推给右
            self.tag[p] = 0 # 清空暂存的懒信息，已经下发
            # 当有update操作自上而下准备更新区间p之前，先下发之前p暂存的懒信息 （本例懒信息只是要加的数值）

    def apply(self, p, l, r, v):  # 下发lazy信息，先更新节点信息，然后暂存懒信息，（不继续下发）
        self.t[p] += (r - l + 1) * v
        self.tag[p] += v

    def add(self, p, l, r, L, R, v):
        # (p,l,r) [L, R] += v
        if L <= l and r <= R: # 当(p,l,r) 为 [L, R] 子区间即停止递归，利用懒信息下发函数更新（不要递归到空，否则失去懒更新意义)
            self.apply(p, l, r, v)
            return
        mid = (l + r) // 2
        self.push(p, l, r) #递归左右之前，先分发懒信息
        if L <= mid:
            self.add(2 * p, l, mid, L, R, v)
        if mid < R:
            self.add(2 * p + 1, mid + 1, r, L, R, v)
        self.pull(p)

    def query(self, p, l, r, L, R):
        if L <= l and r <= R:
            return self.t[p]
        res = 0
        mid = (l + r) // 2
        self.push(p, l, r) #递归左右之前，先分发懒信息，虽然不会更新，但查询部分左右区间也依赖本层懒信息
        if L <= mid:
            res += self.query(2 * p, l, mid, L, R)
        if mid < R:
            res += self.query(2 * p + 1, mid + 1, r, L, R)
        return res
