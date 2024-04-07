"""
排序后求排名，去重或者根据根据相同数的出现次序决定
https://oi-wiki.org/misc/discrete/

本质是一种哈希，保存全序/偏序后映射到更小的集合
"""
from bisect import  bisect_left
from functools import cmp_to_key

nums = [1,3,5,5,7]

# nums 排好序后，对nums每个元素，二分求其在排好序的tmp中的index即为分位数/rank 也可以用hashmap 但二分也差不多 简洁
# tmp = sorted(list(set(nums)))
# discrete_nums = [bisect_left(tmp, x) for x in nums]
# print(discrete_nums)
# [0, 1, 2, 2, 3]


# 额外规定先出现的数rank较大
n = len(nums)
""" 自定义比较器， 先保证大小，同大小，让后出现的元素排序比较大 """
def cmp(x,y):
    if x[0] != y[0]:
        return 1 if x[0] > y[0] else -1
    return 1 if x[1] < y[1] else -1
    # x[1] 对应 index 一定不相等
    # 注意 T/F 对应 1/0 不对应 1/-1

tmp = sorted(list((x,i) for i, x in enumerate(nums)), key=cmp_to_key(cmp))
res = [-1]*n
for i, x in enumerate(tmp):
    res[x[1]] = i
print(res)
# [0, 1, 3, 2, 4]

