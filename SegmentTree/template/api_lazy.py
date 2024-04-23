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

    # 区间更新 - 懒标记
    def add(self, i, l, r, L, R, v):
        """
        标准入参 (i,l,r) 更新信息 (L, R, v) 增加v
        截止条件：节点区间完全位于更新区间，只更改该节点维护值，留下懒标记，不再向下更新
        四段式：
            down传递懒标记
            如更新区间交于左子树 [l,mid]     L <= mid
            如更新区间交于左子树 [mid+1,r]   mid < R
            up合并
        """
        pass

    def down(self, i, l, r):
        """
        标准入参 (i,l,r)
        将父节点lazy tag信息传递给子节点

        三段式：（5段）
        将lazy tag下放到左右子节点
        清空当前节点的lazy tag

        当add/query需要递归进本节点 （如果只是拿本节点全部信息，在上层递归就可以直接调用 a[i] 不需要递归进来）
        """
        pass
    def up(self, i):
        """
        入参 父节点编号
        将左右区间值合并到父节点
        sum[i] = sum[i << 1] + sum[i << 1 | 1];
        """
        pass

    def lazy(self, i, l, r, v):
        """
        标准入参
        改点收到的lazy tag
        当前点维护值 += (r-l+1)*v
        当前点lazy tag += v

        当有重置/修改操作时，优先级不同
        """
        pass
