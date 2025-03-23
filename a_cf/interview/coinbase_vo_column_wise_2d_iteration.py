"""
coinbase vo3 对二维列表进行逐列遍历 （需要维持每一个列的指针）

相关的迭代器问题
1. lc251 按行展开二维向量，只需维持一个全局变量 （row,col) https://leetcode.cn/problems/flatten-2d-vector/description/
2. lc341 嵌套列表迭代器 https://leetcode.cn/problems/flatten-nested-list-iterator/description/
"""
from sortedcontainers import SortedList
class ColumnWiseIterator:
    def __init__(self, nestedList):
        """
        1. 维持所有非空的列 （原nestedList的索引）
        2. 对每个还没遍历完的列，维持其列内索引（hash表）
        3. 如果遍历完一个列，就删掉 [[1-10000], []...[], [1-10000]]

        """
        self.nestedList = nestedList
        self.indices = {i:0 for i in range(len(nestedList)) if nestedList[i]}
        self.keys = SortedList(self.indices.keys())
        self.idx = 0

    def hasNext(self) -> bool:
        return len(self.indices) > 0

    def next(self) -> int:
        nestedList, indices, keys = self.nestedList, self.indices, self.keys

        i = keys[self.idx]

        res = nestedList[i][indices[i]]

        indices[i] = indices[i] + 1
        if indices[i] == len(nestedList[i]):
            del indices[i]
            keys.pop(self.idx)
            if len(keys):
                self.idx = self.idx % len(keys)
        else:
            self.idx = (self.idx + 1) % len(keys)

        return res

nums = [[1,2,3], [], [4,5], [6,7,8,9], [10]]
nums = [[1,2,3], [4,5],[6]]
# 1 4 6 10 2 5 7 3 8 9
it = ColumnWiseIterator(nums)
res = []
while it.hasNext():
    res.append(it.next())
print(res)

class ColumnWiseIterator_cycle:
    def __init__(self, nestedList):
        self.nestedList = nestedList
        self.next_round()
    def next_round(self):
        self.indices = {i:0 for i in range(len(self.nestedList)) if self.nestedList[i]}
        self.keys = SortedList(self.indices.keys())
        self.idx = 0

    def hasNext(self) -> bool:
        return len(self.indices) > 0

    def next(self) -> int:
        nestedList, indices, keys = self.nestedList, self.indices, self.keys

        i = keys[self.idx]

        res = nestedList[i][indices[i]]

        indices[i] = indices[i] + 1
        if indices[i] == len(nestedList[i]):
            del indices[i]
            keys.pop(self.idx)
            if len(keys):
                self.idx = self.idx % len(keys)
        else:
            self.idx = (self.idx + 1) % len(keys)
        return res

nums = [[1,2,3], [], [4,5], [6,7,8,9], [10]]
# nums = [[1,2,3], [4,5],[6]]
# 1 4 6 10 2 5 7 3 8 9
it = ColumnWiseIterator_cycle(nums)
res = []
while it.hasNext():
    res.append(it.next())
it.next_round()
while it.hasNext():
    res.append(it.next())
print(res)