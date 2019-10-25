class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        result = []
        n = len(set(pattern))
        for w in words:
            if len(set(w)) != n:
                continue
            d = dict(zip(pattern, w))
            for k, v in enumerate(pattern):
                if w[k] != d[v]:
                    break
            else:
                result.append(w)
        return result
