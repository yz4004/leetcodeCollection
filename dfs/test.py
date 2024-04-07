from functools import cache
from math import inf
from collections import Counter


if __name__ == '__main__':

    graph = [[], [2, 3], [4, 5], [2, 4, 5], [5], []]
    w = {(1, 2): 10, (1, 3): 3, (3, 2): 6, (3, 4): 3, (2, 4): 1, (2, 5): 1, (3, 5): 10, (4, 5): 6}

    # counter = 0
    counter = [0]


    # @cache
    def dfs(i, visited):
        # nonlocal counter
        counter[0] += 1
        print(i, [str(j) if visited >> j & 1 == 1 else "_" for j in range(1, 6)])

        if i == 5:
            return 0

        res = inf
        for j in graph[i]:
            if visited >> j & 1 == 0:
                edge = (i, j)
                res = min(res, dfs(j, visited | (1 << j)) + w[edge])
        return res


    res = dfs(1, 0)
    print(res, counter[0])

    counter = [0]
    cache = [-1]*(6)
    cache[5] = 0
    def dfs(i, visited):

        if cache[i] != -1:
            return cache[i]
        counter[0] += 1
        print(i, [str(j) if visited >> j & 1 == 1 else "_" for j in range(1, 6)])

        # if i == 5: return 0
        res = inf
        for j in graph[i]:
            if visited >> j & 1 == 0:
                edge = (i, j)
                res = min(res, dfs(j, visited | (1 << j)) + w[edge])
        cache[i] = res
        return res

    res = dfs(1, 0)
    print(res, counter[0])





    graph = [[], [2, 3], [4, 5], [5,4,2], [5], []]
    w = {(1, 2): 10, (1, 3): 3, (3, 2): 6, (3, 4): 3, (2, 4): 1, (2, 5): 1, (3, 5): 10, (4, 5): 6}

    # counter = 0
    counter = [0]

    # @cache
    def dfs(i, visited):
        # nonlocal counter
        counter[0] += 1
        print(i, [str(j) if visited >> j & 1 == 1 else "_" for j in range(1, 6)])

        if i == 5:
            return 0

        res = inf
        for j in graph[i]:
            if visited >> j & 1 == 0:
                edge = (i, j)
                res = min(res, dfs(j, visited | (1 << j)) + w[edge])
        return res


    res = dfs(1, 0)
    print(res, counter[0])



    cache = [-1]*6
    counter = [0]

    def dfs(i, visited):

        if cache[i] != -1:
            return cache[i]
        counter[0] += 1
        print(i, [str(j) if visited >> j & 1 == 1 else "_" for j in range(1, 6)])

        # if i == 5: return 0
        res = inf
        for j in graph[i]:
            if visited >> j & 1 == 0:
                edge = (i, j)
                res = min(res, dfs(j, visited | (1 << j)) + w[edge])
        cache[i] = res
        return res

    res = dfs(1, 0)
    print(res, counter[0])



    cache = [inf]*6
    cache[1] = 0
    counter = [0]

    def dfs(i, visited, path):

        counter[0] += 1
        print(i, [str(j) if visited >> j & 1 == 1 else "_" for j in range(1, 6)])

        if i == 5:
            return

        for j in graph[i]:
            edge = (i, j)
            if cache[j] > path + w[edge]:
                cache[j] = path + w[edge]
                dfs(j,  visited | (1 << j), path + w[edge])

    dfs(1, 0, 0)
    print(cache[5], counter[0])
    print(cache)

    x = Counter()

