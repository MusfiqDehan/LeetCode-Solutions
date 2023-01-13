class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        check_set = set(allowed)
        for word in words:
            if set(word) - check_set == set():
                result += 1
        return result
