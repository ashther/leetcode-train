class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        result = [0] * (l1 + l2)
        num1 = list(reversed(num1))
        num2 = list(reversed(num2))
        if l1 > l2:
            num1, num2 = num2, num1
        
        for i, x in enumerate(num1):
            for j, y in enumerate(num2):
                result[i + j] += int(x) * int(y)
        
        for k, v in enumerate(result):
            if v >= 10:
                result[k] = v % 10
                result[k + 1] += v // 10
        
        result = ''.join([str(x) for x in reversed(result)])
        
        return str(int(result))
