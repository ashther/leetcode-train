class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:
        result = 0
        for k, v in enumerate(guess):
            if v == answer[k]:
                result += 1
        return result
