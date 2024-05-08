
pattern = "abc"
text = "ababc"

m, n = len(pattern), len(text)
pi = [0]*m # pi[i] - pattern[:i] 长i前缀 的最大匹配前后缀长度, 不算每个前缀本身
cnt = 0 # 上一个/当前匹配的最长前后缀长度
for i in range(1, m): # 考虑前缀 [0,i] 以i为结尾
    v = pattern[i]
    while cnt and v != pattern[cnt]: # [0,cnt-1]cnt vs  [...]v 如果失配，则cnt会退到 [0,cnt-1] 该前缀的最长匹配部分
        cnt = pi[cnt-1]
    if pattern[cnt] == v: # 如果毫无匹配，即v=pattern[i] != pattern[0]，则cnt为0
        cnt += 1
    pi[i] = cnt

ans = cnt = 0 # cnt -- pattern指针，上一个/当前匹配长度 - pattern 下一个要匹配的索引
for i, x in enumerate(text): # 外层循环匹配当前文本指针x 不会退
    while cnt and x != pattern[cnt]: # 当失配的时候，利用pi回退pattern的指针到上一个匹配长度 cnt=0时退出 否则无限循环
        cnt = pi[cnt-1]
    if pattern[cnt] == x:
        cnt += 1
    if cnt == m:
        # 如果返回第一个匹配位置 return i-m+1
        ans += 1
        cnt = pi[cnt - 1]
# return ans

