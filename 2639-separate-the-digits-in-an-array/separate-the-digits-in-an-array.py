class Solution:
    def separateDigits(self, a: List[int]) -> List[int]:
        return [*map(int,''.join(map(str,a)))]