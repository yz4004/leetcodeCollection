from typing import List

class BIT:
    def __init__(self, n):
        self.a = [0]*(n+1)

    def add(self, i, x):
        n = len(self.a)
        while i < n:
            self.a[i] += x
            i += i & -i
    def search(self, i):
        res = 0
        while i > 0:
            res += self.a[i]
            i -= i & -i
        return res

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        n = len(nums1)
        t1 = BIT(n)
        t2 = BIT(n)

        posi2 = {n2 : i for i, n2 in enumerate(nums2)}
        res = 0
        for i, x in enumerate(nums1):
            #
            p2 = posi2[x]
            res += t2.search(p2 + 1)
            num_tuple = t1.search(p2 + 1)
            t2.add(p2 + 1, num_tuple)
            t1.add(p2 + 1, 1)
        return res

if __name__ == "__main__":
    s = Solution()
    r = s.goodTriplets([4,0,1,3,2], [4,1,0,2,3])
    print(r)
