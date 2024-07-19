class Solution:
    def strStr(self, text: str, pattern: str) -> int:
        # pattern + text， 找一个match的 z[i] 长度等于 pattern
        # 中间可以插一个分隔符 防止过长的无效匹配
        m = len(pattern)
        s = pattern + "." + text

        n = len(s)
        z = [0]*n
        l = r = 0
        for i in range(m+1, n):
            if i <= r: # [l, r]  x-0 = i-l
                z[i] = min(z[i-l], r-i+1)
            while i + z[i] < n and s[i + z[i]] == s[z[i]]:
                l, r = i, i + z[i]
                z[i] += 1
            if z[i] == m:
                return i
        return -1


    def z_func(self, s):
        n = len(s)
        z = [0]*n
        l = r = 0
        for i in range(n):
            if i <= r: # [l, r]  x-0 = i-l
                z[i] = min(z[i-l], r-i+1)
            while i + z[i] < n and s[i + z[i]] == s[z[i]]:
                l, r = i, i + z[i]
                z[i] += 1
        return z


