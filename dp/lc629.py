"""
1-n 的排列，要求逆序对数量为k，求所有排列数量
n和任何人都能组成逆序对，所以我们可以控制n参与构成的逆序对的数量，然后从k中剔除，就能考虑子问题 1-n-1

f[i][j] = sum(f[i-1][j] + f[i-1][j-1] ... f[i-1][j-p] ... f[i-1][0])  p = [0, j]
从 i 提供 0 个逆序对 直到 i 提供全部的 逆序对

上面的下界并不好，在优化时就会注意到，一个更严格的下界：
f[i][j] = sum(f[i-1][j] + f[i-1][j-1] ... f[i-1][j-p] ... f[i-1][j-(i-1)])  p = [0, i-1]
从 i 提供 0 个逆序对 直到 i 提供他最多能提供的 i-1 个逆序对

如果j大于i所能提供的逆序对 上面的下界是严格的
如果j小于i能提供的，下面会出现负索引 就取0

而对上面的来说，i提供不了所有j个逆序对，取到0是无意义的，这个项本身就无意义。

下面就接着第二个写
f[i][j] <- f[i-1][j] + f[i-1][j-1] ... f[i-1][j-p] ... f[i-1][j-(i-1)])  p = [0, i-1]
对比两个转移
f[i][j-1] <- f[i-1][j-1] + f[i-1][j-2] ... f[i-1][j-p] ... f[i-1][j-1-(i-1)]) p = [1, i]

ij 依赖的 i-1 j
和
ij-1 依赖的 i-1 j
有交集
（因为都依赖于i-1这一行, f[i-1][j] <- f[i-2][j] + f[i-2][j-1] ... 依赖于i-2行 就没有用了）

所以利用f[i][j-1]的结果，可以o1的得到 f[i][j]
f[i][j] = f[i][j-1] + f[i-1][j] - f[i-1][j-i])

这个转移在边界可能失效，即负数索引情况
当f[i][j-1] i能提供超过j-1个逆序对时，累加下界是 f[i-1][0] = 1
假如 f[i][j] i也能提供超过j个逆序对，则直接计右侧的 f[i][j-1] 即可 不需要减去什么

将视角从变量p 转换为q
f[i][j] <- f[i-1][j] + f[i-1][j-1] ... f[i-1][j-p] ... f[i-1][j-(i-1)])  p = [0, i-1]

f[i][j] <- f[i-1][j] + f[i-1][j-1] ... f[i-1][q] ... f[i-1][j-(i-1)])  q = [j-i+1, j]
"""
MOD = 1000_000_000 + 7
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:

        f = [[0] * (k + 1) for _ in range(n)]
        for i in range(n): f[i][0] = 1
        for i in range(1, n):  # 1
            for j in range(1, k + 1):
                if j - i > 0:
                    f[i][j] = (f[i][j - 1] + f[i - 1][j] - f[i - 1][j - i - 1]) % MOD
                else:
                    f[i][j] = (f[i][j - 1] + f[i - 1][j]) % MOD
        return f[n - 1][k]

        # f[i][j] 1-i 提供 j 个逆序对的所有排列, 其中i映射到 i-1
        f = [[0]*(k+1) for _ in range(n+1)]
        # f[i][0] = 1 对于任何i 只有一种单增排列
        # f[n-1][k] 目标值
        # 先更新i行，再更新下一行
        f[0][0] = 1
        for i in range(1, n+1):
            for j in range(k+1): # [1, [0
                if j - i >= 0:
                    f[i][j] = (f[i][j-1] + f[i-1][j] - f[i-1][j-i]) % MOD
                else:
                    f[i][j] = (f[i][j - 1] + f[i - 1][j])%MOD
        return f[n][k]

""" 比较两个写法

        f = [[0]*(k+1) for _ in range(n+1)]
        f[0][0] = 1
        for i in range(1, n+1):
            for j in range(k+1): # [1, [0
                if j - i >= 0:
                    f[i][j] = (f[i][j-1] + f[i-1][j] - f[i-1][j-i]) % MOD
                else:
                    f[i][j] = (f[i][j - 1] + f[i - 1][j])%MOD
        return f[n][k]


        f = [[0]*(k+1) for _ in range(n)]
        f[0][0] = 1 # for i in range(n): f[i][0] = 1
        for i in range(1, n): # 1
            for j in range( k+1):
                if j - i >= 0:
                    f[i][j] = (f[i][j-1] + f[i-1][j] - f[i-1][j-i]) % MOD
                else:
                    f[i][j] = (f[i][j - 1] + f[i - 1][j])%MOD
        return f[n-1][k]

        f = [[0]*(k+1) for _ in range(n)]
        for i in range(n): f[i][0] = 1
        for i in range(1, n): # 1
            for j in range(1, k+1):
                if j - i > 0:
                    f[i][j] = (f[i][j-1] + f[i-1][j] - f[i-1][j-i-1]) % MOD
                else:
                    f[i][j] = (f[i][j - 1] + f[i - 1][j])%MOD
        return f[n-1][k]
"""

