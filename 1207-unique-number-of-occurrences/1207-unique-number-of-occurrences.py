class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        my_dict = Counter(arr)
        return len(my_dict.values()) == len(set(my_dict.values()))
        