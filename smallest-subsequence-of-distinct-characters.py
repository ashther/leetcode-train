class Solution:
    def smallestSubsequence(self, text: str) -> str:
        result = []
        for k, v in enumerate(text):
            if v in result:
                continue
            while True:
                if len(result) == 0:
                    break
                if v < result[-1] and result[-1] in text[k + 1:]:
                    result.pop()
                else:
                    break
            result.append(v)
        return ''.join(result)
