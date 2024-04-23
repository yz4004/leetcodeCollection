"""
api
"""

class SegmentTree:

    def __init__(self, nums):
        """
        原数组   self.nums
        维护数组 self.a / self.t
        build
        """
        pass


    def build(self, i, l, r):
        """
        标准入参 i, l, r  (节点编号，维护区间左右端点）
        截止条件：叶子节点/区间长度为单点，nums值填到a上
        三段式：
            左子树
            右子树
            up 合并左右子树结果到当前节点
        """
        pass

    def query(self, i, l, r, L, R):
        """
        标准入参 (i,l,r) 查询区间 (L,R)
        截止条件：当前区间完全落在查询区间内，返回
        三段式：
            [0]. down 将当前区间懒标记下传
            如查询区间交于左子树 [l,mid]   和 [L,R] 有交集 L <= mid
            如查询区间交于右子树 [mid+1,r] 和 [L,R] 有交集 mid < R
            (不需要up合并）
        """
        pass

    # 单点更新
    def add(self, i, l, r, index, v):
        """
        标准入参 (i,l,r) 更新信息 (index, v) 增加v
        截止条件：叶子节点/区间长度为单点，nums值填到a上
        三段式：
            如更新坐标位于左子树 [l,mid]     index <= mid
            如更新坐标位于左子树 [mid+1,r]   mid < index
            up合并
        """
        pass
