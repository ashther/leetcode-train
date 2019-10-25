from itertools import chain

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        for x in A:
            if x & 1:
                odd.append(x)
            else:
                even.append(x)
        return list(chain(*zip(even, odd)))
