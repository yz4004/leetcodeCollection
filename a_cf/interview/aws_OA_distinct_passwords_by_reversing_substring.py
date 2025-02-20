import random
import string
from collections import defaultdict, Counter

"""
给定一个由小写字母组成的字符串 password，
可以通过反转该字符串的任意一个子串来生成新的字符串。求在所有可能的操作下，可以形成的不同字符串的数量。

例1
input = "abaa"
output = 4
说明 - 可能形成的字符串："abaa", "aaba", "baaa", "aaab"

1 <= n <= 1e5
password: a-z

- 初见会考虑回文子串，（发现一个回文子串则计数-1) 但他其实考虑的是整个字符串，不同位置的子串翻转可能会生成同一实例
  例如上面 整体翻转 abaa -> aaba 和中间 ba 翻转最后生成了同一个实例

- 其实是计数问题
    两个相同的a之间
    a [...] a 中心翻转和算上两边的a翻转，都只会生成一个同一个例子

    考虑所有a  
    a [...] a [...] a ...
    c(n,2) 任意两个a之间的子串翻转和算上a翻转都生成同一个实例, 重复计数应该减去 c(n,2)-1 

"""

def solve(s):
    n = len(s)
    cnt = Counter(s)
    duplicates = 0
    for v in cnt.values():
        t = v * (v - 1) // 2  # 其实就是 comb(v,2)
        duplicates += t
    # 说明 上面所有的 a [...] a 两次翻转都会生成原字符串. 所以原串只计1，然后duplicate都减去
    total = (n + 1) * n // 2
    return total - duplicates - n + 1  # 再减去n - 每个单字符翻转也会生成原串

def check(s):
    # 暴力检查，翻转字符串会生成多少个实例
    n = len(s)
    st = set()
    for i in range(n):
        for j in range(i, n):
            st.add(s[:i] + s[i:j + 1][::-1] + s[j + 1:])
    return len(st)

def generate_random_string(length):
    # 定义字母表 a-z
    letters = string.ascii_lowercase
    # 随机选择指定长度的字母
    return ''.join(random.choices(letters, k=length))



s = "abaa"
print(solve(s), check(s))
# s = "abc"
# print(solve(s))

# for _ in range(100):
#     length = random.randint(100,1000) #随机生成100 - 1000以内的字符串
#     s = generate_random_string(length)
#     assert check(s) == solve(s)
