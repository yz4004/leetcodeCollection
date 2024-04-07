words = [None]*int(input())
for i in range(len(words)):
    words[i] = str(input())

# words = ["abc1"]
# print(words)
# prefix 第一个字母开头 + surfix 纯非零数字
for word in words:
    if word[0].isalpha():
        i = len(word) - 1
        while i > -1 and word[i] == "0":
            i -= 1
        if i >= 0:
            print(word[:i])
