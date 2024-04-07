
def calculateMaxMatchingLength(pattern:str):
    n = len(pattern)
    maxMatchingLength = [0]*len(pattern)
    maxLength = 0

    for i in range(1, n):
        # 考虑前缀 [0:i] 的匹配前后缀的最大长度
        # 可以从之前累计的最大匹配开始
        # patterns[:maxLength] 匹配 pattern[:i]
        # [0:maxLength] 匹配 [i-maxLength:i]
        # 上一次有   [0:maxLength] 匹配 [i-maxLength-1:i-1] 成功匹配
        # 累积到这次 [0:maxLength] maxLength --  [i-maxLength-1:i] i
        #
        while maxLength > 0 and pattern[maxLength] != pattern[i]:
            maxLength = maxMatchingLength[maxLength - 1]

        if pattern[maxLength] == pattern[i]:
            maxLength += 1
        maxMatchingLength[i] = maxLength
    return maxMatchingLength

"""
maxMatchingLength[i]

pattern[:i] 中 它自己的前缀和自己的后缀 中 能匹配的最长
"""

def search(text, pattern):
    n = len(text)
    positions = []
    maxMatchingLength = calculateMaxMatchingLength(pattern)
    cnt = 0

    for i in range(n): # pattern[:cnt] 匹配 test[:i]
        while cnt > 0 and pattern[cnt] != text[i]:
            cnt = maxMatchingLength[cnt - 1]

        if pattern[cnt] == text[i]:
            cnt += 1

        if cnt == len(pattern):
            positions.append(i - len(pattern) + 1)
            cnt = maxMatchingLength[cnt - 1]
    return positions

