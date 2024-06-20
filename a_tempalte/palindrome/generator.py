"""
按大小生成 10^5以内的 palindrome [1 - 99999]

- 枚举回文的左半部分, 同时生成 2*k-1, 2*k 的回文数
    123 -> 12321, 123321
- 下次考虑 k+1 的左半部分，会同时生成 2*k+1, 2*k+2, 这正好是位数从小到大
- 利用base作为左半部分每次循环的出发元素，考虑 [base, base*10] （base每次是最小的k位元素 1/10/100..。）
"""
######################### 模板框架
"""
pal = []
base = 1 # 每次循环节生成 [base, base*10]
while base < 10 ** 5: # 枚举长度上限，即我们接受5及以下的回文数

    for i in range(base, base*10):
        ## 将左半部分(i) 反转拼接
        pass
    # 偶数
    for i in range(base, base * 10):
        pass
    base *= 10
"""
########################### 实现
pal = []
base = 1  # 每次循环节生成 [base, base*10]
while base < 10 ** 5:  # 枚举长度上限，即我们接受5及以下的回文数

    for i in range(base, base * 10):
        x = i       #左半部分，每次对下面的t求个位数然后拼到x后面
        t = i // 10 #奇数要跳过中间的数
        while t:
            x = 10 * x + (t % 10)
            t //= 10
        pal.append(x)

    if base > 10000: break
    # 偶数
    for i in range(base, base * 10):
        x = i  # 同上，只是不跳过第一个个位了
        while t:
            x = 10 * x + (t % 10)
            t //= 10
        pal.append(x)
    base *= 10
print(pal[:100])

####################### 题目
"""
906. 超级回文数 - 力扣（LeetCode）
2967. 使数组成为等数数组的最小代价 - 力扣（LeetCode）


"""