def strStr(self, text: str, pattern: str) -> int:
    # p[:i] 的最长匹配前后缀
    m = len(pattern)
    pi = [0]*m # pi[i] - p[:i]
    # cnt = 0
    # for i in range(1, m):
    #     while cnt and pattern[cnt] != pattern[i]:
    #         cnt = pattern[cnt-1]
    #     if pattern[cnt] == pattern[i]:
    #         cnt += 1
    #     pi[i] = cnt
    for i in range(1, m):
        k = i-1
        while pattern[pi[k]] != pattern[i]:
            k = pi[k] - 1


    n = len(text)
    cnt = 0
    for i in range(n):
        while text[i] != pattern[cnt]:
            #              i-1] [i]
            # pattern[0, cnt-1] [cnt]
            cnt = pi[cnt-1]
        if pattern[cnt] == text[i]:
            cnt += 1
        if cnt == m:
            return i-m+1 # [i-m+1, i]
    return -1

