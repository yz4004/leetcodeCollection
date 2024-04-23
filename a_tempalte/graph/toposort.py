"""
核心思想：每次挑indegree=0的元素入队, 有环则不会入队
如果是普通bfs 则无法区分环与多入度 后者是toposort支持的
而入度做法能区分环与多入度
"""
import collections
from typing import List

###### 输入 ######
#################
n: int
prerequisites: List[List[int]]

###### 建图 + 整理入度为0的初始 ######
##################################
graph = [[] for _ in range(n)]
indegree = [0] * n
for b, a in prerequisites:
    graph[a].append(b)
    indegree[b] += 1

res = [i for i in range(n) if indegree[i] == 0] # 记录顺序 先放入入度0的初始人
q = collections.deque(res)
while q:
    cur = q.popleft() #q 始终保存0入度元素，即将从图上删除
    for j in graph[cur]:
        indegree[j] -= 1
        if indegree[j] == 0:
            q.append(j)
            res.append(j)  # indegree置0 则这是新图的source节点 其所有的入边被标记完，是符合拓扑排序的
        # 如果有环，indegree是不会被置0的，所以压根不会进入queue

if all(x == 0 for x in indegree):
    print("一个拓扑排序：", res)
print("无拓扑排序/有环", [])